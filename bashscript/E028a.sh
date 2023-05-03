#!/bin/bash

input_file="input_data.txt"
output_file="output_data.txt"

total_lines=$(wc -l < "$input_file")
test_case=1

for ((i = 1; i <= total_lines; i +=3)); do
    echo "Executing Test Case ${test_case}:" | tee -a "$output_file"
    sed -n "${i},$((i+2))p" "$input_file" | python /home/pi/Desktop/localrepo/mycommonrepo/E028-test.py 2>/dev/null | tee -a "$output_file"
    echo "-----------------------------------" | tee -a "$output_file"
    test_case=$((test_case + 1))
done