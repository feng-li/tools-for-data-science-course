# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:49:04 2019

@author: dell
"""

from scipy import stats
import numpy as np
import time

### mean_time

time1 = np.array([])
time2 = np.array([])
for i in range(100):
    rnorm = np.random.normal(0,1,10000000)
    rnorm_mat = rnorm.reshape(10,1000000)
    
    start = time.time()
    np.mean(rnorm)
    end = time.time()
    
    time1a = end-start
    time1 = np.append(time1,time1a)
    
    start = time.time()
    np.mean(np.mean(rnorm_mat,axis=1))
    end = time.time()
    
    time2a = end-start
    time2 = np.append(time2,time2a)

np.mean(time1)
np.mean(time2)

stats.ttest_ind(time1,time2)


time3 = np.array([])
time4 = np.array([])
for i in range(100):
    rnorm = np.random.normal(0,1,10000000)
    rnorm_mat = rnorm.reshape(10,1000000)

    start = time.time()
    np.mean(np.mean(rnorm_mat,axis=1))
    end = time.time()
    
    time4a = end-start
    time4 = np.append(time4,time4a)
    
    start = time.time()
    np.mean(rnorm)
    end = time.time()
    
    time3a = end-start
    time3 = np.append(time3,time3a)
    

np.mean(time3)
np.mean(time4)

stats.ttest_ind(time3,time4)


### map_var

n = 10
rnorm = np.random.normal(0,1,100000)
rnorm_mat = rnorm.reshape(n,10000)
np.var(rnorm)

# map
varn = np.var(rnorm_mat,axis=1)
meann = np.mean(rnorm_mat,axis=1)
# reduce
mean1 = np.mean(np.mean(rnorm_mat,axis=1))
var = varn + (mean1-meann)**2
np.sum(var)/n

