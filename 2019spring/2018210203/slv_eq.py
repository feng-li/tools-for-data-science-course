## -*- coding: utf-8 -*-

#
import random
import numpy as np
import pandas as pd

a = np.array([random.randint(1,30) for i in range(10)])
b = np.array([random.randint(1,30) for i in range(10)])
c = np.array([random.randint(1,30) for i in range(10)])
a1 = -b/(2*a)
delta = (b**2 -4*a*c)/(2*a)
j = 0
x1 = np.array([])
slv = pd.DataFrame(columns=['a','b','c','是否有解','x1','x2'])
slv['a'] = a
slv['b'] = b
slv['c'] = c
slv['是否有解'] = delta >= 0
i = 0
while i <= len(slv['是否有解']) - 1:
    if slv['是否有解'].iloc[i]:
        x1 = a1[i] + delta[i]
        x2 = a1[i] - delta[i]
        slv['x1'].iloc[i] = x1
        slv['x2'].iloc[i] = x2
    i = i + 1
print(slv)

    
        
    
