#!/usr/bin/env python
# coding: utf-8

# In[54]:


from random import *
a=list()
for i in range(100000):
    a.append(randint(1,100))


# In[70]:


a1=a[0:10000]
a2=a[10000:20000]
a3=a[20000:30000]
a4=a[30000:40000]
a5=a[40000:50000]
a6=a[50000:60000]
a7=a[60000:70000]
a8=a[70000:80000]
a9=a[80000:90000]
a10=a[90000:100000]
aa=list()
aa.append(a1)
aa.append(a2)
aa.append(a3)
aa.append(a4)
aa.append(a5)
aa.append(a6)
aa.append(a7)
aa.append(a8)
aa.append(a9)
aa.append(a10)


# In[83]:


def mean(a):
    s=0
    for i in range(len(a)):
        s+=a[i]
    m=s/len(a)
    return m
mean(a)


# In[72]:


m=mean(a)
mls=list()
for i in range(len(aa)):
    mls.append(mean(aa[i]))
m2=mean(mls)
print(m)
print(m2)


# In[58]:


import time
time_start=time.time()
for i in range(1000):
    mean(a)
time_end=time.time()
print('time cost',time_end-time_start,'s')


# In[73]:


time_start=time.time()
for i in range(1000):
    mls=list()
    for i in range(len(aa)):
        mls.append(mean(aa[i]))
    m2=mean(mls)
time_end=time.time()
print('time cost',time_end-time_start,'s')


# In[63]:


def var(a):
    s=0
    m=mean(a)
    for i in range(len(a)):
        s+=(a[i]-m)*(a[i]-m)
    v=s/(len(a)-1)
    return v
print(var(a))
print(var(a1))


# In[75]:


s=0
m=mean(a)
for j in range(10):
    s+=(len(a1)-1)*var(aa[j])+len(a1)*(mean(aa[j])-m)*(mean(aa[j])-m)
v2=s/(len(a)-1)
print(v)
print(v2)


# In[81]:


time_start=time.time()
for i in range(100):
    var(a)
time_end=time.time()
print('time cost',time_end-time_start,'s')


# In[85]:


time_start=time.time()
for i in range(100):
    s=0
    m=mean(a)
    for j in range(10):
        s+=(len(a1)-1)*var(aa[j])+len(a1)*(mean(aa[j])-m)*(mean(aa[j])-m)
    v2=s/(len(a)-1)
time_end=time.time()
print('time cost',time_end-time_start,'s')

