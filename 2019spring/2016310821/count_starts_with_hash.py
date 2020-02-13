#! /usr/bin/env python3
# hash_check.py
import re
starts_with_hash = 0

# look at eachline in the file use a regex to see if it starts with "#"
# and if it is, add 1 to the count

with open('google.py', 'r') as f:
    for line in f:
        if re.match("^#", line):
            starts_with_hash += 1
print(starts_with_hash)
