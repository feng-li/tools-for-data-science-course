#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

starts_with_hash = 0

with open('test.py', 'r') as files:
     while True:
        line = files.readline()
        if line:
            if re.match('^#', line):
                    starts_with_hash += 1
        else:
            break
    
print(starts_with_hash)