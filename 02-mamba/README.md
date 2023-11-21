## Make Mamba Env 

run

```bash
module load Mamba/4.14.0-0 # load the Mamba module
mamba init # only needs to be ran once on Tempest
source ~/.bashrc # tell Mamba where to put envs
mamba create -n test-env # create new env called test-env
mamba activate test-env # activate test-env
mamba install python=3.10 # install python 3.10 into test-env
```

make sure to add the 3 lines in the slurm job file
```
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
mamba activate test-env # activate test-env
```
