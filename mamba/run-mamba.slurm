#!/bin/bash
##
## Lines starting with #SBATCH are read by Slurm. Lines starting with ## are comments.
## All other lines are read by the shell.
##
#SBATCH --job-name=mamba             # job name
#SBATCH --partition=test             # queue partition to run the job in
#SBATCH --nodes=1                    # number of nodes to allocate
#SBATCH --ntasks-per-node=1          # number of discrete tasks - keep at one except for MPI
#SBATCH --cpus-per-task=2            # number of logical processors to allocate
#SBATCH --mem=2G                     # 2000 MB of Memory allocated; set --mem with care
#SBATCH --time=0-00:01:00            # Maximum job run time
#SBATCH --output=mamba-%j.out
#SBATCH --error=mamba-%j.err

## Run 'man sbatch' for more information on the options above.

date                              # print out the date
echo "Hello from $(hostname -s)"  # print a message from the compute node

module load Mamba/4.14.0-0
source ~/.bashrc # tells mamba where envs are

# mamba env python
mamba activate test-env # actiavte env
which python3 
python3 --version

python3 hello.py # run a python program

date                              # print the date again

