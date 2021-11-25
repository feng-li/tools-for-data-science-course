# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:29:28 2021

@author: Always
"""

def fib_loop(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
    return a


for i in range(20):
    print(fib_loop(i),end=' ')
    
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 
