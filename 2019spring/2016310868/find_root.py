# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:49:14 2019

@author: HaoliangZheng
"""
def find_root(a,b,c):
    """
    Please input a,b,c as list.
    If they are int or float, the function will go wrong.
    """
    if len(a)-len(b) != 0 | len(a)-len(c) != 0:
        return("length is wrong!")
    
    import math as m
    
    n = len(a)
    for i in range(n):
        if a[i]==0 :
            x = -c[i]/b[i]
            print(repr(i) + ", " + "linear equation, the root is " + repr(x) )
        else:
            delta = b[i]**2 - 4*a[i]*c[i]
            if delta>0 :
                x1 = (-b[i] - m.sqrt(delta))/(2*a[i])
                x2 = (-b[i] + m.sqrt(delta))/(2*a[i])
                print(repr(i) + ", " + "2 real roots: " + repr(x1) + "," + repr(x2))
            if delta==0 :
                x = -b[i] /(2*a[i])
                print(repr(i) + ", " + "1 real root: " + repr(x))
            if delta<0 :
                print(repr(i) + ", " + "no real root ")

find_root([0,1,1,5],[1,2,4,34],[1,3,4,22])
find_root([1,1,5],[2,4,34],[3,4])
