#!/bin/bash
##
## Lines starting with #SBATCH are read by Slurm. Lines starting with ## are comments.
## All other lines are read by the shell.
##
#SBATCH --job-name=hello             # job name
#SBATCH --partition=test             # queue partition to run the job in
#SBATCH --nodes=1                    # number of nodes to allocate
#SBATCH --ntasks-per-node=1          # number of discrete tasks - keep at one except for MPI
#SBATCH --cpus-per-task=2            # number of logical processors to allocate
#SBATCH --mem=2G                     # 2000 MB of Memory allocated; set --mem with care
#SBATCH --time=0-00:01:00            # Maximum job run time
#SBATCH --output=hello-%j.out
#SBATCH --error=hello-%j.err

## Run 'man sbatch' for more information on the options above.

date                              # print out the date
echo "Hello from $(hostname -s)"  # print a message from the compute node
# system python
which python 
python --version 

module load Mamba/4.14.0-0
source ~/.bashrc # tells mamba where envs are
mamba activatpe test-env # actiavte env

# mamba env python
which python 
python --version

python hello.py # run a python program

date                              # print the date again

