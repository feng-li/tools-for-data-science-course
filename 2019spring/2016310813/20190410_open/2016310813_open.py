
# coding: utf-8

# In[1]:

#! /usr/bin/env python3
# hash_check.py
import re
starts_with_hash = 0

# look at each line in the file use a regex to see if it starts with '#' if it does, add 1
# to the count.

with open(r'C:\Users\u\2016310813_find_root.py','r',encoding='UTF-8') as file:
    for line in file:
        if re.match("^#",line):
            starts_with_hash += 1
print(starts_with_hash)


# In[ ]:



