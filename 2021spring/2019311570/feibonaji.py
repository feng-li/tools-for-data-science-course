#!/usr/bin/env python
# coding: utf-8

# In[29]:


n=1
i=2
a=[]
a.append(1)
a.append(1)
while(n<=1000):
    a.append(a[i-1]+a[i-2])
    n=a[i]+a[i-1]
    i=i+1
print(a)


# In[35]:


def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x  
    return result  


# In[30]:


sum(a)


# In[34]:


n=1
i=2
a=[]
a.append(1)
a.append(1)
while(n<=100000):
    a.append(a[i-1]+a[i-2])
    n=a[i]+a[i-1]
    i=i+1
print(a)
sum(a)


# In[40]:


t=multiplyList(a)
t


# In[38]:


from sys import getsizeof
getsizeof(t)


# In[39]:


b=2
getsizeof(b)

