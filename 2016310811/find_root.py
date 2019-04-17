#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:24:52 2019

@author: lvanzhu
"""

#set function as module
import math
import random
a = random.randint(1,7)

    
def find_root(a,b,c):
    for i in a:
        for j in b:
            for k in c:
                if j**2-4*i*k>=0:
                    print("x1=",(-j+math.sqrt(j**2-4*i*k))/2,",x2=",(-j-math.sqrt(j**2-4*i*k))/2)
                else:
                    print("x1=",(-j+math.sqrt(-j**2+4*i*k))/2,"i ,x2=",(-j-math.sqrt(-j**2+4*i*k))/2,"i")

a = [1,2,3,4]
b = [1,5]
c = [3,5,6]
find_root(a,b,c)
