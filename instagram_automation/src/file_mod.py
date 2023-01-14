#!/usr/bin/env python3

filename = "file.txt"
output_file = "modified_file.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

with open(output_file, 'w') as f:
    for i in range(2, len(lines), 3):
        f.write(lines[i])
