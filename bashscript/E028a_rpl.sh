#!/bin/bash

input_file="/home/runner/mycommonrepo/bashscript/input_data_rpl.txt"
output_file="/home/runner/mycommonrepo/bashscript/output_data.txt"

total_lines=$(wc -l < "$input_file")
test_case=1

for ((i = 1; i <= total_lines; i +=3)); do
    echo "Executing Test Case ${test_case}:" | tee -a "$output_file"
    sed -n "${i},$((i+2))p" "$input_file" | python /home/runner/mycommonrepo/E028-test.py 2>/dev/null | tee -a "$output_file"
    echo "-----------------------------------" | tee -a "$output_file"
    test_case=$((test_case + 1))
done