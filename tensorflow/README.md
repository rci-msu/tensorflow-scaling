## Make TensorFlow Mamba Enviroment 

run the below lines to make tensorflow gpu mamab env

```bash
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
export CONDA_OVERRIDE_CUDA="11.2"
mamba env create -f tensorflow-gpu.yaml # create env based on file
```
now run the slurm file by `sbatch run-tensorflow-gpu.slurm`

run the below lines to make tensorflow cpu mamab env

```bash
module load Mamba/4.14.0-0 # load the Mamba module
source ~/.bashrc # tell Mamba where to put envs
mamba env create -f tensorflow-cpu.yaml # create env based on file
```
now run the slurm file by `sbatch run-tensorflow-cpu.slurm`
