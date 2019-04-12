#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:36:49 2019

@author: lvanzhu
"""

import numpy
import scipy
import pandas
import matplotlib
import re

import os
os.chdir('/Users/lvanzhu/Documents')

open("reading 0403.py",'r')

start_hash = 0

with open('0403..py','r') as file:
    for line in file:
        if re.match("#",line):
           start_hash += 1
print(start_hash)
                    