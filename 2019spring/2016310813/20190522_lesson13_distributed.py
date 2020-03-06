
# coding: utf-8

# In[15]:

import csv
import os
import numpy as np
import random
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from random import randint
import seaborn
import math 


# # 分成k部分储存数据

# In[9]:

import time   # 看运行时间
start = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
start


# In[35]:

n = 110
number = np.random.rand(n) # 生成随机数
number


# In[50]:

i = 10 # 每个文件里面最多可以包含的数据个数
k = math.ceil(n/i) # 上取整,需要分成的块数
data = number.reshape((-1,i)) # 分成k份
data


# # 分布计算均值 

# In[54]:

data_mean = [];
for i in range(k):
    t = data[i].mean();data_mean.append(t);
data_mean  # 计算每部分的均值


# In[58]:

print(np.mean(data_mean))  # 通过每部分均值计算出来
print(np.mean(number) )    # 通过总体计算出来的均值


# # 分布求均值

# In[70]:

data_var = [];
for i in range(k):
    t = data[i].var();data_var.append(t);
data_var  # 计算每部分的方差
data_mean


# In[73]:

t = np.var(data_mean)*k
r_var = ((i-1)*t + i*(k-1)*(np.mean(data_var)))/(i*k - 1)


# In[74]:

print(r_var)          # 分布计算出的误差
print(np.var(number)) # 总体误差


# In[67]:




# In[62]:



print(S2_distributed, time_var/m + time.clock()-start_var2)
start_var3 = time.clock()
S2 = data.var(ddof=1)
print(S2, time.clock()-start_var3)


# In[ ]:




# In[ ]:




# In[ ]:



