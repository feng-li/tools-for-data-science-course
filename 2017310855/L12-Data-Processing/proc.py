#! /usr/bin/env python3

import sys
import io

input = io.TextIOWrapper(sys.stdin.buffer, encoding = 'gbk')

for line in input:
	
    # Split
    field = line.split(',')
    
    # Process
    date = field[2]
    max = float(field[5])
    min = float(field[6])
    range = max - min
    mean = (max + min)/2

    data = (date, str(max), str(min), str(range), str(mean))
	
    # Split by space
    ' '.join(data)
    
