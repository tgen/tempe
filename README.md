
![TGEN](images/TGen_Color_LOGO_medium.png)

# Tempe Workflow - A Container-Focused JetStream Workflow

This workflow supports the analysis of human sequencing samples against the GRCh38 reference genome using
ensembl version 103 gene models. The workflow is designed to support project level analysis that can include
one or multiple types of data. Though not required the expectation is a project contains data from a single
individual thus centralizing all data types in a standardized output structure. The workflow template supports
a diverse array of analysis methods required to analyze DNA, RNA, and single cell data. Based on standardized
variables it also supports integrated analysis between data types. For some processes multiple options are
provided that can be individually enabled or disabled by configuration parameters. Like all [JetStream](https://github.com/tgen/jetstream)
workflows developed at TGen this workflow is designed to facilitate our dynamic and time sensitive analysis
needs while ensuring compute and storage resources are used efficiently. The primary input is a JSON record
from the TGen LIMS but hand created inputs in the form of a JSON or EXCEL worksheet can also be provided when
run manually or by submission to the related [JetStream Centro](https://github.com/tgen/jetstream_centro)
web portal. All required files defined the the `pipeline.yaml` can be created using code provided in the
[JetStream Resources repository](https://github.com/tgen/jetstream_resources).

## Output Folder Structure

All final output files are placed in a standardized folder structure that generally reflects the relationship of files or
the processing order.
```
Project
|--GeneralLibaryType
|  |--AnalysisType
|  |  |--Tool
|  |  |  |--SampleName
|  |  |     |--ResultFiles
|  |  |--Tool
|  |--AnalysisType
|--GeneralLibaryType
```

<details>
  <summary><b>Project Folder Example</b></summary>

```
# Only Directories are Shown
MMRF_1499
├── exome
│   ├── alignment
│   │   └── bwa
│   │       ├── MMRF_1499_1_BM_CD138pos_T2_KAS5U
│   │       │   └── stats
│   │       └── MMRF_1499_2_PB_Whole_C7_KHS5U
│   │           └── stats
│   ├── constitutional_structural_calls
│   │   └── manta
│   │       └── MMRF_1499_2_PB_Whole_C7_KHS5U
│   ├── constitutional_variant_calls
│   │   ├── deepvariant
│   │   │   └── MMRF_1499_2_PB_Whole_C7_KHS5U
│   │   └── haplotypecaller
│   │       └── MMRF_1499_2_PB_Whole_C7_KHS5U
│   ├── somatic_copy_number
│   │   └── gatk
│   │       └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│   ├── somatic_structural_calls
│   │   ├── manta
│   │   │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│   │   └── pairoscope
│   │       └── MMRF_1499_1_BM_CD138pos_T2_KAS5U
│   └── somatic_variant_calls
│       ├── lancet
│       │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│       ├── mutect2
│       │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│       ├── octopus
│       │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│       ├── strelka2
│       │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│       ├── vardict
│       │   └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
│       └── vcfmerger2
│           └── MMRF_1499_2_PB_Whole_C7_KHS5U-MMRF_1499_1_BM_CD138pos_T2_KAS5U
├── genome
│   ├── alignment
│   │   └── bwa
│   │       ├── MMRF_1499_1_BM_CD138pos_T2_KAWGL
│   │       │   └── stats
│   │       └── MMRF_1499_2_PB_Whole_C1_KAWGL
│   │           └── stats
│   ├── constitutional_structural_calls
│   │   └── manta
│   │       └── MMRF_1499_2_PB_Whole_C1_KAWGL
│   ├── constitutional_variant_calls
│   │   ├── deepvariant
│   │   │   └── MMRF_1499_2_PB_Whole_C1_KAWGL
│   │   └── haplotypecaller
│   │       └── MMRF_1499_2_PB_Whole_C1_KAWGL
│   ├── copy_number_analysis
│   │   └── ichorCNA
│   │       ├── MMRF_1499_1_BM_CD138pos_T2_KAWGL
│   │       └── MMRF_1499_2_PB_Whole_C1_KAWGL
│   ├── somatic_copy_number
│   │   └── gatk
│   │       └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│   ├── somatic_structural_calls
│   │   ├── manta
│   │   │   └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│   │   └── pairoscope
│   │       └── MMRF_1499_1_BM_CD138pos_T2_KAWGL
│   └── somatic_variant_calls
│       ├── mutect2
│       │   └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│       ├── octopus
│       │   └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│       ├── strelka2
│       │   └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│       ├── vardict
│       │   └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
│       └── vcfmerger2
│           └── MMRF_1499_2_PB_Whole_C1_KAWGL-MMRF_1499_1_BM_CD138pos_T2_KAWGL
├── igv_symbolic_links
├── jetstream
│   ├── history
│   └── logs
├── qc
│   └── multiqc_data
└── rna
    ├── alignment
    │   └── star
    │       └── MMRF_1499_1_BM_CD138pos_T1_TSMRU
    │           └── stats
    ├── fusions
    │   └── starfusion
    │       └── MMRF_1499_1_BM_CD138pos_T1_TSMRU
    └── quant
        ├── salmon
        │   └── MMRF_1499_1_BM_CD138pos_T1_TSMRU
        └── star
            └── MMRF_1499_1_BM_CD138pos_T1_TSMRU
```

</details>

## Required Software

All tools are available as OCI images [here](https://github.com/orgs/tgen/packages)
_Last Updated Sept 29th, 2022_  

| Tool | Version Implemented |
| :---: | :---: |
| [bcftools](https://github.com/samtools/bcftools/releases) | [1.16](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fbcftools) |
| [bedtools](https://github.com/arq5x/bedtools2/releases) | [2.29.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fbedtools) |
| [bwa-mem2](https://github.com/lh3/bwa/releases) | [2.2.1](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fbwa_mem2_samtools) |
| [deepvariant-cpu](https://github.com/google/deepvariant/releases) | [1.4.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fdeepvariant) |
| [deepvariant-gpu](https://github.com/google/deepvariant/releases) | [1.4.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fdeepvariant) |
| [expansion_hunter](https://github.com/Illumina/ExpansionHunter/releases) | [4.0.2](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fexpansion_hunter) |
| [freebayes](https://github.com/ekg/freebayes/releases) | [1.3.1](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Ffreebayes) |
| [gatk](https://github.com/broadinstitute/gatk//releases) | [4.1.8.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fgatk) |
| [hmmcopyutils](https://github.com/shahcompbio/hmmcopy_utils) | [1.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fhmmcopy-utils) |
| [htslib](https://github.com/samtools/htslib/releases) | [1.16](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fhtslib) |
| [ichor](https://github.com/broadinstitute/ichorCNA/releases) | [0.2.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fichorcna) |
| [lancet](https://github.com/nygenome/lancet/releases) | [1.1.x](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Flancet) |
| [manta](https://github.com/Illumina/manta/releases) | [1.6.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fmanta) |
| [msisensor](https://github.com/xjtu-omics/msisensor-pro) | [1.1.a](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fmsisensor) |
| [multiQC](https://github.com/ewels/MultiQC/releases) | [1.13](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fmultiqc) |
| [octopus](https://github.com/luntergroup/octopus/releases) | [0.7.4](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Foctopus) |
| [python3](https://www.python.org/downloads/) | [3.7.2](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fpython) |
| [parabricks](https://docs.nvidia.com/clara/#parabricks) | [4.0.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fclara-parabricks) |
| [R](https://www.r-project.org/) | [3.6.1](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fr-with_modules) |
| [thred](https://github.com/tgen/tHReD) | [1.1.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fthred) |
| [salmon](https://github.com/COMBINE-lab/salmon/releases) | [1.9.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fsalmon) |
| [samtools](https://github.com/samtools/samtools/releases) | [1.16.1](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fsamtools) |
| [snpSniffer](https://github.com/tgen/snpSniffer/releases) | [7.0.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fsnpsniffer) |
| [star-fusion](https://github.com/STAR-Fusion/STAR-Fusion/releases) | [1.11.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fstar_fusion) |
| [strelka](https://github.com/Illumina/strelka/releases) | [2.9.10](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fstrelka) |
| [subread](https://sourceforge.net/projects/subread/) | [2.0.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fsubread) |
| [tgen_mutation_burden](https://github.com/tgen/tgen_mutation_burden/releases) | [1.2.3](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fmutation-burden) |
| [vardictJava](https://github.com/AstraZeneca-NGS/VarDictJava/releases) | [1.7.9](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fvardict) |
| [vcfmerger2](https://github.com/tgen/vcfMerger2/releases) | [0.9.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fvcfmerger2) |
| [vep](https://github.com/Ensembl/ensembl-vep/releases) | [107.0](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fensembl-vep) |
| [verifybamid2](https://github.com/Griffan/VerifyBamID/releases) | [2.0.1](https://github.com/orgs/tgen/packages/container/package/jetstream_containers%2Fverify-bam-id2) |

## Install Guide

Please see the [wiki](https://github.com/tgen/tempe/wiki) for a detailed install guide

## Running from command line

In order to run from the command line, we need to create a config file for our project. The general format is as follows:

```json
{
    "project": "",
    "study": "",
    "email": "",
    "hpcAccount": "",
    "isilonPath": "",
    "pipeline": "tempe",
    "dataFiles": [],
    "dnaAlignmentStyle": "tgen",
    "email": "somebody@tgen.org",
    "isilonPath": "",
    "pipeline": "tempe@version",
    "project": "Project_Name",
    "submitter": "somebody",
    "tasks": {},
}
```

Here is a larger example with actual data for running the tempe pipeline on a NA12878 project:
<details><summary>NA12878 Example</summary>
  <p>

  **Some of this data has been modified to hide the identity of the original submitter(s)**

  ```json
  {
    "cram": true,
    "dataFiles": [
        {
            "assayCode": "TPFWG",
            "dnaRnaMergeKey": "GIAB_NA12878_1_CL_Whole",
            "fastqCode": "R1",
            "fastqPath": "/home/tgenref/homo_sapiens/control_files/giab/fastq/NA12878_140407_D00360_0016_ASUPERFQS01/Project_GIAB_NA12878_1_TPFWG/Sample_GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01/GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01_NoIndex_L001_R1_001.fastq.gz",
            "fileType": "fastq",
            "fraction": "Whole",
            "glPrep": "Genome",
            "glType": "Genome",
            "index1Length": 6,
            "index2Length": 0,
            "limsLibraryRecordId": 64391,
            "numberOfReads": 228228468,
            "read1Length": 148,
            "read2Length": 148,
            "readOrientation": "Inward",
            "rgcn": "TGen",
            "rgid": "SUPERFQS01_1_K18088",
            "rgbc": "ATCACG",
            "rglb": "K18088",
            "rgpl": "ILLUMINA",
            "rgpm": "HiSeq2500",
            "rgpu": "SUPERFQS01_1",
            "rgsm": "GIAB_NA12878_1_CL_Whole_C1",
            "rnaStrandDirection": "NotApplicable",
            "rnaStrandType": "NotApplicable",
            "sampleMergeKey": "GIAB_NA12878_1_CL_Whole_C1_TPFWG",
            "sampleName": "GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088",
            "subGroup": "Constitutional",
            "umiInLine": "false",
            "umiLength": 0,
            "umiRead": false
        },
        {
            "assayCode": "TPFWG",
            "dnaRnaMergeKey": "GIAB_NA12878_1_CL_Whole",
            "fastqCode": "R2",
            "fastqPath": "/home/tgenref/homo_sapiens/control_files/giab/fastq/NA12878_140407_D00360_0016_ASUPERFQS01/Project_GIAB_NA12878_1_TPFWG/Sample_GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01/GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01_NoIndex_L001_R2_001.fastq.gz",
            "fileType": "fastq",
            "fraction": "Whole",
            "glPrep": "Genome",
            "glType": "Genome",
            "index1Length": 6,
            "index2Length": 0,
            "limsLibraryRecordId": 64391,
            "numberOfReads": 228228468,
            "read1Length": 148,
            "read2Length": 148,
            "readOrientation": "Inward",
            "rgcn": "TGen",
            "rgid": "SUPERFQS01_1_K18088",
            "rgbc": "ATCACG",
            "rglb": "K18088",
            "rgpl": "ILLUMINA",
            "rgpm": "HiSeq2500",
            "rgpu": "SUPERFQS01_1",
            "rgsm": "GIAB_NA12878_1_CL_Whole_C1",
            "rnaStrandDirection": "NotApplicable",
            "rnaStrandType": "NotApplicable",
            "sampleMergeKey": "GIAB_NA12878_1_CL_Whole_C1_TPFWG",
            "sampleName": "GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088",
            "subGroup": "Constitutional",
            "umiInLine": "false",
            "umiLength": 0,
            "umiRead": false
        }
    ],
    "dnaAlignmentStyle": "tgen",
    "email": "example@tgen.org",
    "ethnicity": "Caucasian",
    "familyCode": "",
    "holdConfig": false,
    "hpcAccount": "tgen-#####",
    "isilonPath": "/example/giab/",
    "matchedNormal": true,
    "matchedNormalToUse": "",
    "maternalID": "",
    "patCode": "NA12878",
    "paternalID": "",
    "pipeline": "tempe",
    "project": "GIAB_NA12878",
    "sex": "Female",
    "study": "GIAB",
    "submitter": "user",
    "submitterEmail": "examplet@tgen.org",
    "varDB": false
}
```

Looking at the block of objects between the datafiles and the tasks one might notice some objects not mentioned in the minimal example provided in the general example. Some of these might be specific to the project and your environment. The common ones that we use in our primary use case are:

```json
    "dnaAlignmentStyle": "",
    "email": "",
    "ethnicity": "",
    "familyCode": "",
    "holdConfig": false,
    "hpcAccount": "",
    "isilonPath": "",
    "matchedNormal": true,
    "matchedNormalToUse": "",
    "maternalID": "",
    "patCode": "",
    "paternalID": "",
    "pipeline": "",
    "project": "",
    "sex": "",
    "study": "",
    "submissionSource": "",
    "submitter": "",
```

  </p>
</details>

Once we have a config file for the project we're ready to initialize and launch the project. We can initialize a project via

```console
$ jetstream init -h
usage: jetstream init [-h] [-l] [-p PROJECT] [-f] [--project-id PROJECT_ID]
                      [-c TYPE:KEY VALUE] [-C PATH]
                      [path]

Create or reinitialize a project This command is used to create a new
Jetstream project directory. If no path is given, the current directory will
be initialized. If config data options are given (-c/--config/--config-file),
they will be added to the project config file.

positional arguments:
  path                  Path to a initialize a project

optional arguments:
  -h, --help            show this help message and exit
  -l , --logging        set the logging profile
  -p PROJECT, --project PROJECT
                        path to a Jetstream project directory
  -f, --force           Force overwrite of project.yaml
  --project-id PROJECT_ID
                        Force a project ID instead of using letting it be
                        generated automatically

template variables:
  These options are used to add data that is available for rendering
  templates. These arguments should follow the syntax "-c <[type:]key>
  <value>". They can be used multiple times.

  -c TYPE:KEY VALUE, --config TYPE:KEY VALUE
                        add a single template variable
  -C PATH, --config-file PATH
                        load template variables from a file

$ jetstream init GIAB -C GIAB_NA12878_24582bb3f7.json
```

This creates a jetstream project with the title of GIAB. Now in order to run the Tempe pipeline on this project, we need to use:

```console
$ jetstream pipelines -h
usage: jetstream pipelines [-h] [-l] [-p PROJECT] [-o OUT] [-b] [-r]
                           [--backend {local,slurm}]
                           [--format {template,module,workflow}]
                           [--reset-method {retry,resume,reset}]
                           [--existing-workflow EXISTING_WORKFLOW]
                           [--template-dir [SEARCH_PATH]] [-c TYPE:KEY VALUE]
                           [-C PATH] [--pipelines-home PIPELINES_HOME] [-L]
                           [path]

Run a pipeline. Pipelines are Jetstream templates that have been documented
with version information and added to the jetstream pipelines directory. This
command allows pipelines to be referenced by name and automatically includes
the pipeline scripts and constants in the run. Run Jetstream from a template,
module, or workflow

positional arguments:
  path                  path to a template, module, or workflow file. (if
                        using "pipelines" command, the name of the pipeline)

optional arguments:
  -h, --help            show this help message and exit
  -l , --logging        set the logging profile
  -p PROJECT, --project PROJECT
                        path to a Jetstream project directory
  -o OUT, --out OUT     path to save the workflow progress (this will be set
                        automatically if working with a project) [None]
  -b, --build-only      just render the template, build the workflow, and stop
  -r, --render-only     just render the template and stop
  --backend {local,local_docker,local_singularity,slurm,slurm_singularity,dnanexus}
                        runner backend name used for executing tasks [slurm]
  --format {template,module,workflow}
                        workflow format - if this is None, it will be inferred
                        from the extension of the path [None]
  --reset-method {retry,resume,reset}
                        controls which tasks are reset prior to starting the
                        run - "retry": pending and failed, "resume": pending,
                        or "reset": all [retry]
  --existing-workflow EXISTING_WORKFLOW
                        path to an existing workflow file that will be merged
                        into run (this will be set automatically if working
                        with a project)
  --template-dir [SEARCH_PATH]
                        directory to add to search path for loading templates,
                        this can be used multiple times

template variables:
  These options are used to add data that is available for rendering
  templates. These arguments should follow the syntax "-c <[type:]key>
  <value>". They can be used multiple times.

  -c TYPE:KEY VALUE, --config TYPE:KEY VALUE
                        add a single template variable
  -C PATH, --config-file PATH
                        load template variables from a file

pipeline options:
  --pipelines-home PIPELINES_HOME
                        override path to the pipelines home
  -L, --list            show a list of all the pipelines installed

$ jetstream pipelines tempe -p GIAB
```

Now we wait for the pipeline to finish!

___

## Required Configuration Variables

For each of our data files/fastqs we have some required data, many of which are self explained,
but we will explain the more unique variables. Here is an example:

```json
"dataFiles": [
    {
        "assayCode": "TPFWG",
        "dnaRnaMergeKey": "GIAB_NA12878_1_CL_Whole",
        "fastqCode": "R1",
        "fastqPath": "/home/tgenref/homo_sapiens/control_files/giab/fastq/NA12878_140407_D00360_0016_ASUPERFQS01/Project_GIAB_NA12878_1_TPFWG/Sample_GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01/GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088_SUPERFQS01_NoIndex_L001_R1_001.fastq.gz",
        "fileType": "fastq",
        "fraction": "Whole",
        "glPrep": "Genome",
        "glType": "Genome",
        "index1Length": 6,
        "index2Length": 0,
        "limsLibraryRecordId": 64391,
        "numberOfReads": 228228468,
        "read1Length": 148,
        "read2Length": 148,
        "readOrientation": "Inward",
        "rgcn": "TGen",
        "rgid": "SUPERFQS01_1_K18088",
        "rgbc": "ATCACG",
        "rglb": "K18088",
        "rgpl": "ILLUMINA",
        "rgpm": "HiSeq2500",
        "rgpu": "SUPERFQS01_1",
        "rgsm": "GIAB_NA12878_1_CL_Whole_C1",
        "rnaStrandDirection": "NotApplicable",
        "rnaStrandType": "NotApplicable",
        "sampleMergeKey": "GIAB_NA12878_1_CL_Whole_C1_TPFWG",
        "sampleName": "GIAB_NA12878_1_CL_Whole_C1_TPFWG_K18088",
        "subGroup": "Constitutional",
        "umiInLine": "false",
        "umiLength": 0,
        "umiRead": false
    }
```

## Data file attributes

There are restrictions on what some of these variables can be assigned to, these will be denoted in the [ ]'s.
If the attribute isn't strictly required then it is not included in this list.

  - *assayCode*  
    Genome: [*] We are not concerned about the assayCode for genomes.  
    *Note: We have a number of bed files supporting our exome captures, these are the shortened capture codes*  
    Exome: [ *AG2 | *E61 | *S5U | *S5X | *S6U | *S6X | *S7X | *ST2 | *STL | *STX | *TS1 | *V6C ]   
    Used for determining if the sample is DNA/RNA/etc. and adding the corresponding
    tasks to the final workflow. Each sample discovered will take this attribute from
    the first file encountered for that sample in the config file.

  - *dnaRnaMergeKey*  
    Used during DNA/RNA integrations steps. It defines the pairing of DNA and RNA samples as a project might have
    multiple DNA and RNA pairs, for instance it can be used to ensure the diagnosis exome and RNA are paired together
    and the relapse exome is not paired with the diagnosis RNA.

  - *fastqCode* [R1|R2]  
    Assigns the read number of the fastq following standard Illumina paired-end nomenclature.

  - *fastqPath*   
    Assigns the path to the fastq.

  - *fileType*  
    Assigns the file type.

  - *glPrep* [genome|capture|rna|singlecellrna|singlecellenrichment|singlecellcdna|singlecelltargetamp|matepair|chip]  
    Used for determining the prep used to create the sample and then modifying how the
    pipeline runs depending on the prep. This is used to configure single cell as well as CHIP preps.

  - *glType* [genome|genomephased|exome|rna|singlecellrna|singlecelldna|matepair|chip]  
    Used for determining if the sample is DNA/RNA/etc. and adding the corresponding
    tasks to the final workflow. Each sample discovered will take this attribute from
    the first file encountered for that sample in the config file.

  - *limsLibraryRecordId*  
    Generated by our LIMS, this allows for the input of data back into the LIMS via a REST-API.

  - *numberOfReads*  
    Used for validating the number of chunks created during alignment.

  - *read1Length / read2Length*   
    Used to select the correct STAR indexes.

  - *readOrientation* [inward|outward]  
    Used to set the strand orientation of RNA assays. Used in conjunction with rnaStrandDirection and rnaStrandType.

  - *rg values*  
    These are standards set in the [SAM/BAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf):  
    rgcn - Name of sequencing center producing the read  
    rgid - Read group identifier.  
    rgbc - Barcode sequence identifying the sample or library.  
    rglb - Unique identifier for the library.  
    rgpl - Platform/technology used to produce the reads.  
    rgpm - Platform model. Used to configure platform duplicate marking thresholds. Free-form text providing further details of the platform/technology used.  
    rgpu - Platform unit (e.g., flowcell-barcode.lane for Illumina or slide for SOLiD). Unique identifier.  
    rgsm - Sample. Use pool name where a pool is being sequenced.  

  - *fraction*  
    Relevant to the TGen naming scheme. See TGen Naming Convention.

  - *rnaStrandDirection* [notapplicable|forward|reverse]  
    Used during STAR alignment of RNA.

  - *rnaStrandType* [unstranded|stranded]  
    Assigns the strand orientation of an RNA library

  - *sampleMergeKey*   
    This is the expected BAM filename and is used to merge data from multiple sequencing
    lanes or flowcells for data from the same specimen (rgsm) tested with the same assay

  - *sampleName*  
    This is the expected base FASTQ filename.

  - *subGroup*   
    Sets where the data file is for tumour or constitutional, changes the analysis of the data file as well as sets
    the distinction of files during somatic analysis.

## TGen Naming Convention
Many of the naming structures used are defined by the standardize naming structure used at TGen that ensures all files
have a unique but descriptive name. It is designed to support serial collection and multiple collections from
difference sources on a single day.  Furthermore, sample processing methods can be encoded.

STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement_ASSAY_LIBRARY

Patient_ID = STUDY_PATIENT<br/>
Visit_ID = STUDY_PATIENT_VISIT<br/>
Specimen_ID = STUDY_PATIENT_VISIT_SOURCE<br/>
Sample_ID = STUDY_PATIENT_VISIT_SOURCE_FRACTION<br/>
RG.SM = STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement (VCF file genotype column header)<br/>
sampleMergeKey = STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement_ASSAY (BAM filename, ensures different assays are not merged together)<br/>
