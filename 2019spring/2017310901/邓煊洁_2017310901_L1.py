#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_root(a,b,c):
    """
    Judge whether an equation has root and figure out the root of a equation if it has.
    Usage
         root(a,b,c)
         a,b,c indicate ax**2+b*x+c=0
    """
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
a=[1,2,3,4,5,6,7,8,9,1]
b=[13,3,125,2,136,8,32,6,9,2]
c=[2,54,87,623,7,578,6,54,3,1]
help(find_root)
for i in range(10):
    find_root(a[i],b[i],c[i])

