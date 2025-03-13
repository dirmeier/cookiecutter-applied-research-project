#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks-per-core=1
#SBATCH --partition=debug
#SBATCH --constraint=gpu

srun nvidia-smi
srun python check_jax.py

