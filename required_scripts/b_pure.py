#! /usr/bin/env python

#Bpure
# Author: Felix Madrid

import pandas as pd
import numpy as np
import argparse
import subprocess
import json
import math
import sys
import io
import os
import re

#using subprocess to push commands to command line
def call_subprocess(subprocess_argument, column_names):
    arg1 = subprocess.check_output(subprocess_argument)
    subprocess_df = pd.read_csv(io.BytesIO(arg1),
                                sep = '\t',
                                header = None,
                                names = column_names)
    return subprocess_df

#calling samtools bedcov to get read counts for specified region. Returns dataframe with 5 columns.
def call_bedcov(bed_file, sample_file, reference_file):
    if reference_file:
            bedcov_arg = ["samtools", "bedcov", "-c", "-G", "READ2", "--reference", reference_file, bed_file, sample_file]
    else:
            bedcov_arg = ["samtools", "bedcov", "-c", "-G", "READ2", bed_file, sample_file]

    bedcov_output = call_subprocess(bedcov_arg, ['contig', 'start', 'end', 'coverage', 'reads'])

    return bedcov_output

def g_mean(input):
    #cannot have a zero value when calculating geometric mean
    abs_input = [abs(i) or 0.001 for i in input]
    g_output = np.log(abs_input)
    return np.exp(g_output.mean())

#calculate log2 fold change, returns log2, standard deviation, reads ratio
def calculate_log2(reads_of_interest, neutral_reads):
    output_list = []
    for reg_x in reads_of_interest:
        list1 = []
        for cn_neut in neutral_reads:
            try:
                list1.append(reg_x/cn_neut)
            except:
                #cannot divide by zero
                pass
            
        to_output = g_mean(list1)
        output_list.append(to_output)
        
    output = g_mean(output_list)

    return(math.log2(output), output)

#Main code
def run(args):
    args_dictionary = {'--bam-file':'input_bam','--seg-file':'input_seg','--region-file':'region_file','--reference-file':'ref_file',
                       '--header-prefix':'header_prefix','--log2-column':'log2_col','--cn-cutoff':'cn_cutoff','--num-bins':'num_bins',
                       '--bin-size':'bin_size','--temp-dir':'temp_dir','--output-dir':'output_dir','--sample_name':'sample_name',
                       '--output-prefix':'output_pref','--json-out':'json_out','--library':'library'}
    
    command = ''
    
    for k, v in args.__dict__.items():
        try:
            kk = [a for a, v in args_dictionary.items() if v == k]
            command = command + f"{kk[0]} {v} "
        except:
            pass

    print(f'Arguments: {command}')
    
    sample_name =  os.path.basename(args.input_bam).split('.')[0] if args.sample_name is None  else args.sample_name

    if args.seg_res:
        seg_resolution = 'PURITY_' + args.seg_res.upper() + '_RES' if (args.seg_res and args.seg_res.lower() == 'high' or 'low') else sys.exit(f'Incorrect value: "{args.seg_res}" passed through --seg-resolution, only values "high" or "low" accepted as input')
        output_prefix = args.output_dir+'/'+sample_name+'_'+args.seg_res.lower()+'_res' if args.output_pref is None else args.output_dir+'/'+args.output_pref
    
    else:
        seg_resolution = 'PURITY'
        output_prefix = args.output_dir+'/'+sample_name if args.output_pref is None else args.output_dir+'/'+args.output_pref

    log2_col = -1 if args.log2_col is None else int(args.log2_col - 1)

    seg_name = os.path.basename(os.path.splitext(args.input_seg)[0])

    #Determining if source of seg file provided is iChor or not
    if 'ichorCNA.cna' in seg_name:
        seg_df = pd.read_csv(args.input_seg, sep='\t', header=0, comment=args.header_prefix,
                             names=['contig', 'start', 'end', 'CN', 'event', 'logR', 'subclone_status', 'corrected_CN', 'corrected_call', 'logR_CN'])
    else:
        seg_df = pd.read_csv(args.input_seg, sep='\t', header=0, comment=args.header_prefix)
        seg_df = seg_df.rename(columns={seg_df.columns[1]:'contig', seg_df.columns[2]:'start', seg_df.columns[3]:'end', seg_df.columns[log2_col]:'logR'})
    
    #first filter to subset to CN neutral segments. can be user defined, default is 0.1
    cn_neut_region = seg_df[(seg_df['logR'] >= -args.cn_cutoff) & (seg_df['logR'] <= args.cn_cutoff)].reset_index(drop=True).dropna()

    #making sure there are enough copy number neutral regions to process sample
    if len(cn_neut_region) > 0:

        #if there are enough regions to subset further to a fraction of a standard deviation away from geometric mean
        if len(cn_neut_region) > 10:
            cn_stdv = np.std(cn_neut_region['logR'])
            one_away = g_mean(cn_neut_region['logR']) + abs(0.5*cn_stdv)
            neut_region_stdv = cn_neut_region[(cn_neut_region['logR'] > -one_away) & (cn_neut_region['logR'] < one_away)]

            if len(neut_region_stdv) == 0:
                neut_region_stdv = cn_neut_region

        elif 0 <= len(cn_neut_region) <= 10:
            neut_region_stdv = cn_neut_region

        temp_bed_name = args.temp_dir+'/'+sample_name+'.temp.bed'

        cn_bed_input = neut_region_stdv.loc[:, ('contig', 'start', 'end')]
        cn_bed_input.to_csv(temp_bed_name, sep='\t', index=False, header=False)

        #creating smaller windows to compare to region of interest 
        bed_arg = ['bedtools', 'makewindows', '-b', temp_bed_name, '-w', str(args.bin_size)]
        bed_output = call_subprocess(bed_arg, ['contig', 'start', 'end'])
        
        os.remove(temp_bed_name)

        #grabbing number of defined windows(bins) from CN neutral regions 
        try:
            subset_bed = bed_output.sample(n=args.num_bins, random_state=53287)
        #if number of available windows does not match value provided, error message will print and script will exit
        except ValueError:
            sys.exit(f'Insufficient CN neutral windows available. {len(bed_output)} windows of length {args.bin_size} bp, user requested {args.num_bins}.')

        subset_bed.to_csv(temp_bed_name, sep='\t', index=False, header=False)

        sort_arg = ['sort', '-V', '-k1,1', '-k2,2', temp_bed_name]
        sort_df = call_subprocess(sort_arg, ['contig', 'start', 'end'])
        
        sorted_bed = args.temp_dir+'/'+sample_name+'.sorted.bed'
        sort_df.to_csv(sorted_bed, sep='\t', index=False, header=False)

        #extracting read counts for CN neutral regions and input (DJ) region of IGH locus
        bedcov_neutral = call_bedcov(sorted_bed, args.input_bam, args.ref_file) 
        bedcov_dj = call_bedcov(args.region_file, args.input_bam, args.ref_file)

        #calculating log2, standard deviation, and reads ratio
        out_list = list(calculate_log2(bedcov_dj['reads'], bedcov_neutral['reads']))

        #calculating b-cell purity
        out_list.append(abs(1 - out_list[1]))

        #adding sample name to output list
        out_list.insert(0,sample_name)

        df_out = pd.DataFrame([out_list],
                              columns =['sample', 'log2', 'reads_ratio','bcell_purity'])
        df_out.to_csv(output_prefix +'_b_cell_purity.tsv', sep='\t', index=False)

        #Defining .json output
        if args.json_out == 'True':
            libraries = [x.strip(' ') for x in args.library.split(',')] if args.library else [sample_name]

            for LB in set(libraries):
                myList = {
                    'COMMAND':command,
                    'SAMPLES':[
                        {
                            'LIBRARIES':[
                                {
                                    'READGROUPS':[
                                        {}
                                    ],
                                    'LB':LB,
                                    seg_resolution:out_list[3],
                                }
                            ],
                            'SM':sample_name,
                            seg_resolution:out_list[3],
                        }
                    ]
                }

                jsonFile = (output_prefix+ '_' + LB + '_b_cell_purity.json') if len(set(libraries)) > 1 else (output_prefix + '_b_cell_purity.json')
                
                jsonString = json.dumps(myList, sort_keys=False, indent=4)

                with open(jsonFile, 'w') as outfile:
                    outfile.write(jsonString)
        else:
            pass

        os.remove(temp_bed_name)
        os.remove(sorted_bed)

    #if number of available windows does not match value provided, error message will print and script will exit
    else:
        sys.exit('No viable copy number neutral regions discovered')

def main():
    parser=argparse.ArgumentParser(description='Calculate estimated b-cell purity of sample')
    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument('--bam-file', metavar='FILE', type=str, dest='input_bam', help='Input BAM/CRAM file', required=True)
    required.add_argument('--seg-file', metavar='FILE', type=str, dest='input_seg', help='Input corresponding seg file, assumes first four columns as track name, chromosome, start location, and end location', required=True)
    required.add_argument('--region-file', metavar='FILE', type=str, dest='region_file', help='Region of interest seg file with only chr, start, and stop', required=True)

    optional.add_argument('--reference-file', metavar='FILE', type=str, dest='ref_file', help='Reference sequence FASTA FILE', required=False)
    optional.add_argument('--header-prefix', metavar='STR', type=str, dest='header_prefix', default='#', help='Header lines begin with this string (Default: "#")', required=False)
    optional.add_argument('--log2-column', metavar='INT', type=int, dest='log2_col', help='Column index number containing log2 values (Default: last column in seg file)', required=False)
    optional.add_argument('--cn-cutoff', metavar='INT', type=int, dest='cn_cutoff', default=0.1, help='Cutoff value on either side of 0 to define CN neutral region (Default: 0.1)', required=False)
    optional.add_argument('--num-bins', metavar='INT', type=int, dest='num_bins', default=500, help='Number of CN windows to compare to region of interest (Default: 500)', required=False)
    optional.add_argument('--bin-size', metavar='INT', type=int, dest='bin_size', default=1000, help='Size of CN windows (bp) for comparison (Default: 1000 (1kb))', required=False)
    optional.add_argument('--temp-dir', metavar='PATH', type=str, dest='temp_dir', default=os.getcwd(), help='Temp directory (Default: current directory)', required=False)
    optional.add_argument('--output-dir', metavar='PATH', type=str, dest='output_dir', default=os.getcwd(), help='Final directory (Default: current directory)', required=False)
    optional.add_argument('--sample-name', metavar='STR', type=str, dest='sample_name', help='Sample name (Default: entire file name without extension)', required=False)
    optional.add_argument('--output-prefix', metavar='STR', type=str, dest='output_pref', help='Output file naming prefix (Default: sample_name_seg_resolution)', required=False)
    optional.add_argument('--json-out', metavar='TRUE/FALSE', type=str, dest='json_out', default=False, help='Output .json file in addition to .tsv (Default: False)', required=False)
    optional.add_argument('--seg-resolution', metavar='STR', type=str, dest='seg_res', help='Input seg file resolution (high/low)', required=False)
    optional.add_argument('--library', metavar='STR', type=str, dest='library', help='Individual or list of comma separated libraries for .json output (Default: None)', required=False)
    
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()