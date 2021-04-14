# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:30:02 2019

@author: Lee Oscar
"""
import re
count = 0
with open('line_count.py','r') as file:
    for line in file:
        if re.match("^#",line):
            count += 1
print(count)
 

