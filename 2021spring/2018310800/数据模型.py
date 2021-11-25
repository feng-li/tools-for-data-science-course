#!/usr/bin/env python
# coding: utf-8

# 三阶段增长模型

# In[15]:


import pandas as pd


# In[21]:


a={
    'Year':[1,2,3,4,5,'after 5years'],
    'Growth rate':[6,6,5.25,4.5,3.75,3],
    'Dividend':[0.53,0.5618,0.5913,0.6179,0.6411,9.4333],
    'Discount rate':[0.1,0.1,0.1,0.1,0.1,0.1],
    'Discount factor':[0.9091,0.8264,0.7513,0.6830,0.6209,0.6209],
    'Present value':[0.4818,0.4643,0.4442,0.4220,0.3981,5.8571]
  }

table= pd.DataFrame(a)
table


# 如何居中；不要序列；合并表格；间距调整

# In[22]:


import matplotlib.pyplot as plt


# In[38]:


t_data=['t1','t2','t3','t4','t5','t6','t7','t8']
g_data=[6,6,5.25,4.5,3.75,3,3,3]
plt.plot(t_data,g_data,color='blue',linewidth=3.0,linestyle='-')
plt.show()


# In[ ]:


太严格了！！！！
间距；起点；垂直水平；提示


# In[58]:


import pandas as pd


# In[59]:


import numpy as np


# In[56]:


#===


# In[57]:


file_name=''


# In[ ]:


time=4


# In[63]:


zero_change= False


# In[64]:


one_change= False


# In[65]:


two_change= False


# In[68]:


three_change= True


# In[71]:


g1,g2,g3,g4,g5=0.6,0.525,0.45,0.375,0.3


# In[72]:


t1,t2=np.arange(1,4),np.arange(1,3)


# In[ ]:


def read_file(file_name):
