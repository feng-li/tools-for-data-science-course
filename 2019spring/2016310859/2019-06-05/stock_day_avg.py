#! /usr/bin/env python3

import sys
data = []
for line in sys.stdin:
	fields = line.split(sep=',')
	stock_mean = (float(fields[2]) + float(fields[5]))/2
    data.append([fields[0], fields[1], stock_mean])
print(data)