# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:54:23 2019

@author: tutuxy
"""

#! /usr/bin/env python3
# hash_check.py

import re
starts_with_hash = 0
starts_with_hash
# look at each line in the file use a regex to see if it starts with '#' if it does, add 1
# to the count.

with open('from scratch.py','r',encoding='UTF-8') as file:
    for line in file:
        if re.match("^#",line):
            starts_with_hash += 1
print(starts_with_hash)
