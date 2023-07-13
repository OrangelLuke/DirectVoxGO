#! /bin/bash

# Define the number of times to run the command
num_times=10

# Define the command to be executed
command="python3 run.py --config configs/nerf/lego.py --render_test --eval_ssim --eval_lpips_vgg"

# Loop to run the command multiple times
for ((i=1; i<=$num_times; i++))
do
    echo "Running command: $command (Iteration: $i)"
    $command
done