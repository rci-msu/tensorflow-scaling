#!/bin/bash
##
## Lines starting with #SBATCH are read by Slurm. Lines starting with ## are comments.
## All other lines are read by the shell.
##
#SBATCH --job-name=tf-cpu            # job name
#SBATCH --account=priority-rci          # account name
#SBATCH --partition=priority             # queue partition to run the job in
#SBATCH --nodes=1                    # number of nodes to allocate
#SBATCH --ntasks-per-node=1          # number of discrete tasks - keep at one except for MPI
#SBATCH --cpus-per-task=32            # number of logical processors to allocate
#SBATCH --mem=60G                    # 2000 MB of Memory allocated; set --mem with care
#SBATCH --time=0-01:00:00            # Maximum job run time
#SBATCH --output=tf-cpu-%A-%3a.out
#SBATCH --error=tf-cpu-%A-%3a.err
#SBATCH --array 0-9

## Run 'man sbatch' for more information on the options above.

date # print out the date
echo "Hello from $(hostname -s)"  # print a message from the compute node
module load Mamba/4.14.0-0
source ~/.bashrc # tells mamba where envs are
mamba activate tf-cpu-2_13 # actiavte env
time -p python mnist.py # run a python program
date # print the date again

