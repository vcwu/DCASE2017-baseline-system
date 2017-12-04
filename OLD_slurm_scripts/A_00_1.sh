#!/bin/bash
#SBATCH -N 1 # No. of computers you wanna use. Typically 1
#SBATCH -n 2 # No. of CPU cores you wanna use. Typically 1
#SBATCH -p gpu # This flag specifies that you wanna use GPU and not CPU 
#SBATCH -o results/A_00_1.out # output file name, in case your program has anything to output (like print, etc)
#SBATCH -t 3:00:00 # Amount of time
#SBATCH --gres=gpu:2 # No. of GPU cores you wanna use. Usually 2-3

source activate tensorflow 
python applications/task1.py -p configs/A_00_1.yaml >> baseline.log
