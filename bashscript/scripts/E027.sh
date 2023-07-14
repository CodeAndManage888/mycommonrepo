#!/bin/bash

input_file="/home/pi/Desktop/localrepo/mycommonrepo/bashscript/inE027.txt"
output_file="/home/pi/Desktop/localrepo/mycommonrepo/bashscript/outE027.txt"

total_lines=$(wc -l < "$input_file")
test_case=1

for ((i = 1; i <= total_lines; i += 5)); do
    description=$(sed -n "${i}p" "$input_file")
    echo "Executing Test Case ${test_case} ${description}:" | tee -a "$output_file"
    
    sed -n "$((i+1)),$((i+4))p" "$input_file" | python /home/pi/Desktop/localrepo/mycommonrepo/pythonwb_intro/E027-test.py 2>/dev/null | tee -a "$output_file"
    
    echo "-----------------------------------" | tee -a "$output_file"
    echo | tee -a "$output_file"
    test_case=$((test_case + 1))
done