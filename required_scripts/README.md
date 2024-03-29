# Required Scripts
This directory contains scripts for at least one of the following reasons
 - From a private source with no intention of being made public
 - Scripts where making a module does not make sense.

### Example 1
runIchorCNA
 - External R library distributed by CRAN but is executed from a provided RunIchorCNA.R file, that is not executable/detect within R session
### Example 2
plotCNVplus
 - This is a stand alone script with two R library dependencies (optparse, data.table). Making a module for this script that would put it in the users path would be wasteful of institutional resources.  
## Development Guidelines
 - Copy file into the external_scripts directory with the git commit ID embedded into the filename.
 - Clearly update the Documentation section of this README.md with the following information about the script.
    - How was the script acquired (git clone path, wget path)
    - What the Commit id is (git rev-parse --short HEAD)

## Documentation
### plotCNVplus
```
$ git clone git@github.com:tgen/plotCNVplus.git
$ cd plotCNVplus
$ git rev-parse --short HEAD
4d89cb4
$ cp plotCNVplus.R /path/to/phoenix/required_scripts/plotCNVplus_4d89cb4.R
```

## Script Source Locations
[Process_Assembled_BAM_277eed7.py](https://github.com/tgen/GaMMiT/commit/277eed728712fa8e636858055ecbf1be270cc114)  
[manta_prepare_sv_vcf_f94bcc1.py](https://github.com/tgen/jetstream_resources/commit/f94bcc13c826f7d5a4088347e305ffcb49ae6a8e)  
[mm_igtx_pairoscope_calling_b38_356362b.py](https://github.com/tgen/mm_IgTx_Calling/commit/356362b03f13181f2762ab468f9b4f222439ea69)  
[plotCNVplus_4d89cb4.R](https://github.com/tgen/plotCNVplus/commit/4d89cb4d8f35e48b916d660c82c52b8725ade16f)  
[runIchorCNA_47ce8db.R](https://github.com/broadinstitute/ichorCNA/commit/47ce8db4d81ada2d3ce09280661d1240f3dcd530#diff-79cb887cc56cef135b77c5b7a725975c)  
[samStats2json_2f64a79.py](https://github.com/tgen/samStats2json/commit/2f64a79a484916e304ad003ea486098f7b253bd4)  
[sigprofiler_7595614.py](https://github.com/tgen/jetstream_resources/commit/7595614ea08fdf9306b52af69e44b7b61b628925)  
[seg_extend_229b8c7.py](https://github.com/tgen/jetstream_resources/commit/229b8c7641dd505789664aab88c1662d1f97e429)  
[summarize_samstats_8c45d63.R](https://github.com/tgen/plot_samstats/commit/8c45d63dbd7f5037d7bb658ac91647898bf7509f)  
[summarize_Ig_875a823.R](https://github.com/tgen/jetstream_resources/commit/875a823202ba698d7adc1f25db86290b67d19028)  
[uploadStats2Lims_1ace81f.py](https://github.com/tgen/uploadStats2Lims/pull/2/commits/1ace81faaea5f894b9f618d86b1d2d9b8149cdc6)  
