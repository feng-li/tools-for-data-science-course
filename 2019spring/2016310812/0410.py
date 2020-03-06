# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:54:23 2019

@author: tutuxy
"""

import zipfile

myzip = zipfile.ZipFile('C:/liwi/tds19/2016310812/0410.zip')
myzip.filename
myzip.namelist()

import pandas
pandas.read_csv(myzip.open('0410.csv'))


#! /usr/bin/env python3
# hash_check.py

import re
starts_with_hash = 0
starts_with_hash
# look at each line in the file use a regex to see if it starts with '#' if it does, add 1
# to the count.

with open('C:/liwi/tds19/2016310812/from scratch.py','r',encoding='UTF-8') as file:
    for line in file:
        if re.match("^#",line):
            starts_with_hash += 1
print(starts_with_hash)


#! /usr/bin/env python3

import pandas

data2 = pandas.read_csv('C:/liwi/tds19/2016310812/0410.csv', delimiter='\t',header=None)
print(len(data2))
print(type(data2))

data2
