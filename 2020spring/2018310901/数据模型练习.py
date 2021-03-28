#!/usr/bin/env python
# coding: utf-8

# In[29]:


with open("D:/Learning materials/tools-for-data-science-course/课件/data/BABAnews.txt", mode = 'r',encoding='UTF-8') as myfile: 
        print(myfile.read())


# In[5]:


myfile.closed


# In[30]:


myfile = open("D:/Learning materials/tools-for-data-science-course/课件/data/BABAnews.txt", mode = 'r',encoding='UTF-8')
text = myfile.read()
myfile.close()
print(text)


# In[31]:


myfile.read()


# In[32]:


myfile = open("D:/Learning materials/tools-for-data-science-course/课件/data/BABAnews.txt", mode = 'r',encoding='UTF-8')
myfile.read()


# In[33]:


myfile.read()
myfile.close()


# In[34]:


myfile = open("D:/Learning materials/tools-for-data-science-course/课件/data/BABAnews.txt", mode = 'r',encoding='UTF-8')
myfile.readline()


# In[35]:


myfile.readlines()


# In[13]:


with open('D:/Learning materials/tools-for-data-science-course/课件/data/Titanic.csv', 'r') as myfile:
    for line in myfile:
        print(line, end ='')


# In[14]:


import pandas as pd
titanicData = pd.read_csv('D:/Learning materials/tools-for-data-science-course/课件/data/Titanic.csv') 
titanicData.head()

