#!/bin/bash

input_file="/home/runner/mycommonrepo/bashscript/inE031.txt"
output_file="/home/runner/mycommonrepo/bashscript/outE031.txt"

total_lines=$(wc -l < "$input_file")
test_case=1

for ((i = 1; i <= total_lines; i += 2)); do
    description=$(sed -n "${i}p" "$input_file")
    echo "Executing Test Case ${test_case} ${description}:" | tee -a "$output_file"
    echo "-----------------------------------" | tee -a "$output_file"
    
    sed -n "$((i+1)),$((i+1))p" "$input_file" | python3 /home/runner/mycommonrepo/pythonwb_intro/E031-test.py 2>/dev/null | tee -a "$output_file"
    
    echo "-----------------------------------" | tee -a "$output_file"
    echo | tee -a "$output_file"
    test_case=$((test_case + 1))
done