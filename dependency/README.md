## Job Dependecy 

To run `./submit-jobs.sh` from the directory where the .slurm files are.

Files and what they do
 -  run-slurm-array.slurm - launches job array that makes output from python
 -  run-concat-results.slurm - concatenates all the .python-out files that were made
 -  submit-jobs.sh - launches the job array and set the concat-results to be dependency
 -  in_out.py - print first input argument for python (data generator)
 -  clean-up.sh - deletes files in current directory that ends in .out , .err or .python-out (files no longer needed)
 -  concat_python - file where all the python-out output went (may not be there until jobs ran)
 -  *.out - the output from the jobs (may not be there until jobs ran)
 -  *.err - the error from the jobs (may not be there until jobs ran)
 -  *.python-out - output from each python instance (may not be there until jobs ran)

If you a need anymore help or explanation please let me know. We can schedule a meeting if you want.
P.S. NIH has a good tutorial [HERE](https://hpc.nih.gov/docs/job_dependencies.html) if you want learn some more

