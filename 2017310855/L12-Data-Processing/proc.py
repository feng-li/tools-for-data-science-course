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
    min = float(field[4])
    range = max - min
	mean = (max + min)/2

    data = (date, max, min, range, mean)
    print(data) 
    