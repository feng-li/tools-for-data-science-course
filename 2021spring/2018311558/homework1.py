#!/usr/bin/env python
# coding: utf-8

# In[1]:


##计算斐波拉契乘积##


# In[7]:


a=1
b=2
product=a*b
for i in range(100):
    a=a+b
    b=a+b
    product=product*a*b
product


# In[ ]:




