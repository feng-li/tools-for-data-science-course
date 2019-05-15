#!/usr/bin/env python
# coding: utf-8
# In[10]:

import random
def find_root(a,b,c):
    """
    Judge whether an equation has root and figure out the root of a equation if it has.
    Usage
         root(a,b,c)
         a,b,c indicate ax**2+b*x+c=0
    be sure that a != 0
    """
    if a == 0:
        print("a couldn't be 0")
    else:
        deta=b**2-4*a*c
        if deta<0:
            print('None')
        elif deta==0:     
            x=-b/2*a
            print('One root is: '+str(x))
        else:
            x1=(-b+deta**0.5)/2*a
            x2=(-b-deta**0.5)/2*a
            print('One root is:',str(x1),'the other is:',str(x2))
a=[random.randint(1,100) for i in range(9)]
a.append(0)
b=[random.randint(1,100) for i in range(10)]
c=[random.randint(1,100) for i in range(10)]
print(a)
print(b)
print(c)
help(find_root)
for i in range(10):
    find_root(a[i],b[i],c[i])





