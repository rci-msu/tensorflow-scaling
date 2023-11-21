## Make Mamba Env 

run the below line or run the bash script make-mamba-env.sh by `bash make-mamba-env.sh`

```bash
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
mamba env create -f tensorflow-gpu.yaml # create env based on file
```

make sure to add the this line in the slurm job file
```bash
export CONDA_OVERRIDE_CUDA="11.2"
mamba activate tf-gpu-2_13# activate test-env
```

now run the slurm file by `sbatch run-tensorflow.slurm`
