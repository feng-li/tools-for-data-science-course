#! /usr/bin/env python3

import sys
import io
import csv

input_stream = io.TextIOWrapper(sys.stdin.buffer , encoding ='gbk')

csv_file = csv.reader(input_stream)

print(csv_file)
for lines in csv_file:
    numbers = [lines[5],lines[6]]
    numbers = list(map(float, numbers))
    dif = numbers[0] - numbers[1]
    print("%s %f"%(lines[1],dif))
