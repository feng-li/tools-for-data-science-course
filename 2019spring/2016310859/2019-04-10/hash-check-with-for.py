#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hash_check_1.py

import re

starts_with_hash = 0

with open('test.py', 'r') as files:
    for line in files:
        if re.match('^#', line):

print(starts_with_hash)

