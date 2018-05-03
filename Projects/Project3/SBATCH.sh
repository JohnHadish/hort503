#!/bin/sh
#SBATCH --partition=ficklin
#SBATCH --account=ficklin
#SBATCH --job-name=Project03_John_Hadish
#SBATCH --output=Out.out   ### File in which to store job output
#SBATCH --error=Error.err  ### File in which to store job error messages
#SBATCH --time=2-00:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1              ### Node count required for the job
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Nod
module add gcc/7.3.0 java nextflow
nextflow run Project03.nf -profile kamiak
