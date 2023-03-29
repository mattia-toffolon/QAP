#!/bin/bash
#SBATCH --job-name QAP
#SBATCH --partition arrow 
#SBATCH --ntasks 1
#SBATCH --mem 14GB
#SBATCH --time 01:00:00

# warm up processors
sudo cpupower frequency-set -g performance

sleep 0.1

stress-ng -c 4 --cpu-ops=100

# set limits
ulimit -v 16777216

#####################
# commands to execute
python Main.py
#####################

# back to power saving mode
sudo cpupower frequency-set -g powersave
