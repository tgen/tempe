---
title: Usage
nav_order: 3
---

## Running from command line

In order to run from the command line, we need to create a config file for our
project. The general format is as follows:

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
  "tasks": {}
}
```

Here is a larger example with actual data for running the Tempe pipeline on a
NA12878 project:

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

Looking at the block of objects between the datafiles and the tasks one might
notice some objects not mentioned in the minimal example provided in the
general example. Some of these might be specific to the project and your
environment. The common ones that we use in our primary use case are:

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

Once we have a config file for the project we're ready to initialize and launch
the project. We can initialize a project via

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

This creates a jetstream project with the title of GIAB. Now in order to run
the Tempe pipeline on this project, we need to use:

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

---

## Required Configuration Variables

For each of our data files/fastqs we have some required data, many of which are
self explained, but we will explain the more unique variables. Here is an
example:

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

There are restrictions on what some of these variables can be assigned to,
these will be denoted in the [ ]'s. If the attribute isn't strictly required
then it is not included in this list.

- _assayCode_  
  Genome: [*] We are not concerned about the assayCode for genomes.  
  _Note: We have a number of bed files supporting our exome captures, these are
  the shortened capture codes_  
  Exome: [*AG2 | *E61 |*S5U | *S5X |*S6U | *S6X |*S7X | *ST2 |*STL ]  
  Used for determining if the sample is DNA/RNA/etc. and adding the corresponding
  tasks to the final workflow. Each sample discovered will take this attribute from
  the first file encountered for that sample in the config file.

- _dnaRnaMergeKey_  
  Used during DNA/RNA integrations steps. It defines the pairing of DNA and RNA
  samples as a project might have multiple DNA and RNA pairs, for instance it can
  be used to ensure the diagnosis exome and RNA are paired together and the
  relapse exome is not paired with the diagnosis RNA.

- _fastqCode_ [R1|R2]  
  Assigns the read number of the fastq following standard Illumina paired-end nomenclature.

- _fastqPath_  
  Assigns the path to the fastq.

- _fileType_  
  Assigns the file type.

- _glPrep_ [genome|capture|rna|matepair]  
  Used for determining the prep used to create the sample and then modifying
  how the pipeline runs depending on the prep.

- _glType_ [genome|genomephased|exome|rna|matepair]  
  Used for determining if the sample is DNA/RNA/etc. and adding the corresponding
  tasks to the final workflow. Each sample discovered will take this attribute from
  the first file encountered for that sample in the config file.

- _numberOfReads_  
  Used for validating the number of chunks created during alignment.

- _read1Length / read2Length_  
  Used to select the correct STAR indexes.

- _readOrientation_ [inward|outward]  
  Used to set the strand orientation of RNA assays. Used in conjunction with rnaStrandDirection and rnaStrandType.

- _rg values_  
  These are standards set in the [SAM/BAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf):  
  rgcn - Name of sequencing center producing the read  
  rgid - Read group identifier.  
  rgbc - Barcode sequence identifying the sample or library.  
  rglb - Unique identifier for the library.  
  rgpl - Platform/technology used to produce the reads.  
  rgpm - Platform model. Used to configure platform duplicate marking thresholds. Free-form text providing further details of the platform/technology used.  
  rgpu - Platform unit (e.g., flowcell-barcode.lane for Illumina or slide for SOLiD). Unique identifier.  
  rgsm - Sample. Use pool name where a pool is being sequenced.

- _fraction_  
  Relevant to the TGen naming scheme. See TGen Naming Convention.

- _rnaStrandDirection_ [notapplicable|forward|reverse]  
  Used during STAR alignment of RNA.

- _rnaStrandType_ [unstranded|stranded]  
  Assigns the strand orientation of an RNA library

- _sampleMergeKey_  
  This is the expected BAM filename and is used to merge data from multiple sequencing
  lanes or flowcells for data from the same specimen (rgsm) tested with the same assay

- _sampleName_  
  This is the expected base FASTQ filename.

- _subGroup_  
  Sets where the data file is for tumour or constitutional, changes the analysis of the data file as well as sets
  the distinction of files during somatic analysis.

## TGen Naming Convention

Many of the naming structures used are defined by the standardize naming structure used at TGen that ensures all files
have a unique but descriptive name. It is designed to support serial collection and multiple collections from
difference sources on a single day. Furthermore, sample processing methods can be encoded.

STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement_ASSAY_LIBRARY

Patient_ID = STUDY_PATIENT<br/>
Visit_ID = STUDY_PATIENT_VISIT<br/>
Specimen_ID = STUDY_PATIENT_VISIT_SOURCE<br/>
Sample_ID = STUDY_PATIENT_VISIT_SOURCE_FRACTION<br/>
RG.SM = STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement (VCF file genotype column header)<br/>
sampleMergeKey = STUDY_PATIENT_VISIT_SOURCE_FRACTION_SubgroupIncrement_ASSAY (BAM filename, ensures different assays are not merged together)<br/>
