#!/usr/bin/env python
# coding: utf-8

# In[7]:


# A+B
import numpy as np
A = np.array([[2,2,3],[1,3,5],[4,6,1]])
B = np.array([[9,4,1],[2,6,3],[7,5,8]])
print("A=",A)
print("B=",B)
print("A+B=",A + B)


# In[8]:


# A·B
import numpy as np
from scipy import linalg
A = np.array([[2,2,3],[1,3,5],[4,6,1]])
B = np.array([[9,4,1],[2,6,3],[7,5,8]])
print("A·B=",A.dot(B))


# In[11]:


import re
have_H = 0
with open('goodbye.txt','r')as file:
    for line in file:
        if re.match("H",line):
            have_H +=1
print(have_H)


# In[12]:


import pandas
data = pandas.read_csv('data.csv',delimiter='\t',header=None)
print(len(data))
print(type(data))


# In[ ]:


import zipfile
myzip = zipfile.ZipFile('data.zip')
myzip.filename()

