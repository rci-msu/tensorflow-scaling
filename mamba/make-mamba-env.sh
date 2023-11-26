#!/bin/bash
module load Mamba/4.14.0-0
mamba init # only needs to be done once
source ~/.bashrc # tells mamba where envs are
mambe create -n test-env # create mamba env call test-env
mamba activate test-env # actiavte env
mamba install python=3.10 # install python 3.10

