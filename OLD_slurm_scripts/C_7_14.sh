#!/bin/bash
#SBATCH -N 1 # No. of computers you wanna use. Typically 1
#SBATCH -n 1 # No. of CPU cores you wanna use. Typically 1
#SBATCH -p gpu # This flag specifies that you wanna use GPU and not CPU 
#SBATCH -o ../results/C_7_14.out # output file name, in case your program has anything to output (like print, etc)
#SBATCH -t 8:00:00 # Amount of time
#SBATCH --gres=gpu:2 # No. of GPU cores you wanna use. Usually 2-3
#SBATCH --mem 20000 



source activate dlnn_gpu 
python ../applications/task1.py  -p ../configs/C_7_14.yaml >> ../results/C_7_14.log 
