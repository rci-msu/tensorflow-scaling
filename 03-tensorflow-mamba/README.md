## Make Mamba Env 

run the below line or run the bash script make-mamba-env.sh by `bash make-mamba-env.sh`

```bash
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
mamba env create -f tf-gpu.yaml # create env based on file
```

make sure to add the 3 lines in the slurm job file
```bash
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
mamba activate tf-gpu-2_13# activate test-env
```

now run the slurm file by `sbatch run-mamba.slurm`
