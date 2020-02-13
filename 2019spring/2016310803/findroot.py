# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:50:57 2019

@author: think
"""

import math
def findroot(a, b, c):
    delta = b*b-4*a*c
    if delta < 0:
        print('无实数解')
    elif a == 0:
        if b == 0:
            if c!=0:
                print('无解')
            else:
                print('在实数范围恒成立')
        else:
            x = -c/b
            print("解为"+repr(x))
    else:
        if delta == 0:
            x =  (-b+math.sqrt(delta))/(2*a)
            print("解为"+repr(x))
        else:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            print("一个解为"+repr(x1)+',另一个为'+repr(x2))