#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#复习已知及练习未学习过的python语句


# In[5]:


def triangles(n):    
    L = [1]
    for x in range(n):
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


# In[6]:


for x in triangles(10):     
    print(x)


# In[7]:


def add(x, y, f):
    return f(x) + f(y)


# In[8]:


add(-5, 6, abs)


# In[9]:


list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# In[10]:


def normalize(name):  
    name = name.lower()
    name = name.capitalize()
    return name


# In[11]:


L = ['adam', 'LISA', 'barT']
list(map(normalize, L))


# In[12]:


from functools import reduce
def prod(L):  
    return reduce(lambda x, y: x * y, L )


# In[13]:


prod([3, 5, 7, 9])


# In[14]:


list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15]))


# In[15]:


sorted([36, 5, -12, 9, -21], key=abs)


# In[16]:


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=lambda x: x[0]))  
print(sorted(students, key=lambda x: x[1]))  
print(sorted(students, key=lambda x: x[1], reverse=True))  


# In[17]:


get_ipython().run_line_magic('pwd', '')

