# DTI Toolkits 

DTI Toolkits are python based NIRAL pipeline software including DTIPrep (dtiprep), DTIAtlasBuilder (dtiab), DTIFiberTract Analyzer (dtifa)

### DTIPrep Usage (dtiprep)

DTIPrep is a tool that performs quality control over diffusion weighted images. Quality control is very essential preprocessing where the bad gradients with artifacts is to be excluded or corrected using various computational methods. The software and library provides a module based package in which users can make his own QC pipeline as well as new pipeline modules.

#### CLI Mode :

1. **init** - Initialize configuration (default: $HOME/.niral-dti/dtiprep)

**init** command generates the configuration directory and files with following command. One just needs to execute this command only once unless a different configuration is needed.
```
    $ dtiprep init 
```
If you want to set different directory other than default one :
```
    $ dtiprep init --config-dir my/config/dir
```
Once run, config.yml and environment.yml will be in the directory. 

2. **update** - Update if config.yml has been changed (e.g. in case of adding user module directory).
Changing `config.yml` file shoule be followed by updating `environment.yml` with running update command :
```
    $ dtiprep update [--config-dir my/config/dir]
```
This will update module-specific informations such as binary locations or package location used by the corresponding module. It simply updates environment.yml

3. **make-protocols** - Generating a default protocol file

The first thing to do QC is to generate default protocol file that has pipeline information.
```
    $ dtiprep make-protocols -i IMAGE_FILENAME [-o OUTPUT_FILENAME_] [-l MODULE1 MODULE2 ... ]
```
if `"-o"` option is omitted, the output protocol will be printed on terminal.`"-l"` option specifies the list of modules for the QC, with which command will generate the default pipeline and protocols of the sequence. Same module can be used redundantly. If `"-l"` option is not specified, the default pipeline will be generated. You can change the default pipeline in `protocol_template.yml` file

4. **run** - Running pipeline 
To run with default protocol generated by dtiprep:

```
    $ dtiprep run -i IMAGE_FILE -o OUTPUT_DIR -d [-l MODULE1 MODULE2 ... ]
```
`"-l"` option only works with `"-d"` option (default protocol) as described in **make-protocols** command.

To run with existing protocol file:
```
    $ dtiprep run -i IMAGE_FILE -p PROTOCOL_FILE -o output/directory/
```

#### GUI Mode :
```
    $ dtiprep image_file -p protocol --gui
```

#### Server Mode:
```
    $ dtiprep --server --port 4000
```


### Supported Images

- NRRD 
- NIFTI

### DTIAtlasBuilder Usage (dtiab)

DTIAtlasBuilder is a software to make an atlas from multiple diffusion weighted images. It performs affine/diffeomorphic registrations and finally generates the atlas for all the reference image. 

### DTIFiberAnalyzer Usage (dtifa)

DTIFiberAnalyzer performs statistical computation over the extracted fibers. This enables researchers to get the information of the fiber images easily and fast.

### Developement 

#### Main developer



#### References

- [Quality Control of Diffusion Weighted Images - Zhexing Liu, et al](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864968/)


#### Acknowlegements

DTI Toolkits are funded by National Institute of Health (NIH)

#### LICENSE

MIT

#### Requirements

##### Application required

- Python >= 3.6 
- FSL >= 6.0 (Required for the eddy tools which perform eddymotion/suceptibility correction)

##### Python libraries
- pynrrd==0.4.2
- dipy==1.4.0
- pyyaml==5.3.1

### Todos
- Docker distribution with NIRAL toolchain and FSL 
- Distributed computing - Celery 
- Server mode - Flask 
- GUI client (Single page web app) - Vuejs, React, ...
- FSL integration
- Multi threading
- Output generations for DTIPrepModule
- Abstract one more level for dtiprep.module.postProcess (Currently baseline averaging module override the postProcess method due to the forced writing which makes the next module load the file after first run. In the first run, object id is passed.) - Done (2021-04-21)

### Change Log

##### 2021-04-21
- DTIPrep : Baseline average implemented (DirectAverage, BaselineOptimized)
- DTIPrep : Optionalized pipeline implemented 
- DTIPrep : dtiprep cli implemented
- DTIPrep : initial configuration directory management (default $HOME/.niral-dti/dtiprep)
- DTIPrep : Minor bug fixed

##### 2021-04-18
- DTIPrep : Slicewise check implemented
- DTIPrep : Interlace check implemented
- DTIPrep : Continuation from stopped point has been implemented , but if image itself is deformed it won't work. It only has ability to track exclusion of gradients yet.
- DTIPrep : Colored output is enabled with the logger. (dtiprep.Color.WARNING, dtiprep.Color.OK ... thingks like that look in __init__.py of dtiprep module)

##### 2021-04-15
- DTIPrep : Sequential Pipelining implemented

##### 2021-04-09
- DTIPrep : New protocol format (YAML)
- DTIPrep : New protocol template (YAML)

##### 2021-04-01
- DTIPrep : Deveopement initiated
