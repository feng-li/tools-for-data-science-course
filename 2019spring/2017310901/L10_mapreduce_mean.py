#! /usr/bin/env python3
import sys
import io
s=0
l=0
input_stream=io.TextIOWrapper(sys.stdin.buffer, encoding='gbk')
for line in input_stream:
    linp=line.split(",")
    s+=eval(inp[5])
    l+=1
mean=s/l
print(mean)
