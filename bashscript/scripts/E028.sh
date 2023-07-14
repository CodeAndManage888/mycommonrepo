#!/bin/bash

input_file="input_data.txt"

while read -r line; do
    printf '%s\n' "$line"
done < "$input_file" | python /home/pi/Desktop/localrepo/mycommonrepo/pythonwb_intro/E028-test.py