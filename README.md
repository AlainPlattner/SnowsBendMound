# Data, processing, and plotting routines for the research article "Multi-method geophysical investigation at Snow's Bend, a Mississippian Platform Mound"

All software required for processing and plotting is freely available

## Software requirements

### Software required for processing

#### ERT and TDIP

Python 3 with BERT/GIMLi installed. The easiest way for installing
both is to install python 3 through Anaconda:
https://www.anaconda.com/products/individual and then install BERT and
GIMLi following the instructions here: http://resistivity.net/bert/install.html

#### GPR

Python 3 with GPRPy installed. The easiest way to install both is to
install python 3 through Anaconda (same as for ERT and TDIP):
https://www.anaconda.com/products/individual and then install GPRPy
following the instructions here: https://nsgeophysics.github.io/GPRPy/


### Software required for plotting

#### ERT, TDIP, and GPRPy

Same as the software required for processing.

#### Surface Resistance Mapping

GMT 6: https://www.generic-mapping-tools.org/



## Instructions for processing

### ERT and TDIP

In an Anaconda console, in the directory `processing/ERTTDIP`, run

`python invertDataMerged.py`

These calculations may take a while.


### GPR

In an Anaconda console, in the directory `processing/GPR`, run

`python script_100MHz.py`

There is also a script for the 200MHz data, in case you are interested.

The processing also creates some of the figures in the article.


## Instructions for plotting

### Surface Resistance Mapping

In a GMT 6 console (terminal / command prompt, perhaps Anaconda console, depending on how you installed it), in the directory `plotting/SurfaceRes/` run

`./ResPT.sh`


### ERT and TDIP

To reproduce the ERT figure without interpretation,  in an Anaconda console, in the directory `plotting/ERTTDIP`, run

`python ERT_paperFigs.py`

To reproduce the ERT figure with interpretation,  in an Anaconda console, in the directory `plotting/ERTTDIP`, run

`python ERT_interpFigure.py`


To reproduce the TDIP figure without interpretation,  in an Anaconda console, in the directory `plotting/ERTTDIP`, run

`python TDIP_paperFigs.py`


To reproduce the TDIP figure with interpretation,  in an Anaconda console, in the directory `plotting/ERTTDIP`, run

`python TDIP_interpFigure.py`


### GPR


To reproduce the GPR figure with interpretation,  in an Anaconda console, in the directory `plotting/GPR`, run

`python interpFigureGPR_lines.py`

### Interpretation

To reproduce the interpretation figure,  in an Anaconda console, in the directory `plotting/interpretation`, run

`python interpFigure.py`

### Map

In a GMT 6 console (terminal / command prompt, perhaps Anaconda console, depending on how you installed it), in the directory `plotting/Map/` run

`./ResPT.sh`