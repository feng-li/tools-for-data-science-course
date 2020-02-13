# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:03:59 2019

@author: 兔毛
"""

import re
starts_with_hash = 0

with open('C:/Users/oguri/Documents/ME/Future/统计计算/MC&MH.R','r') as file:
    for line in file:
        if re.match("^#",line):
            starts_with_hash += 1
print(starts_with_hash)