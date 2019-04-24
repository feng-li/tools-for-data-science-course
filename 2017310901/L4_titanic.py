#!/usr/bin/env python
# coding: utf-8

# In[106]:


import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
data=sns.load_dataset("titanic")
print(data[0:5])

# 舱位直方图,数据不能有缺失
x1=data["pclass"]
nx1=x1.dropna()
sns.distplot(nx1, kde=False, rug=True)

#绘图
sns.lmplot(x="survived", y="age", data=data)
sns.lmplot(x="survived", y="age", data=data, x_estimator=np.mean)


# In[103]:


#年龄直方图
x3=data["age"]
nx3=x3.dropna()
sns.distplot(nx3, kde=False, rug=True)


# In[101]:


# 4纵向增加是否独身变量，线性回归
sns.lmplot(x="age", y="survived", hue="sex",col="pclass", row="alone", data=data)


# In[87]:


# 1绘制年龄与存活与否的逻辑回归图
sns.lmplot(x="age", y="survived", data=data,logistic=True)


# In[92]:


# 2绘制年龄与存活与否的逻辑回归图，按性别分
sns.lmplot(x="age", y="survived", hue="sex", col="pclass",row="", data=data)


# In[94]:


# 3横向增加舱位变量,线性回归
sns.lmplot(x="age", y="survived", hue="sex", col="pclass", data=data)


# In[98]:


#3 横向增加舱位变量，logit回归
sns.lmplot(x="age", y="survived", hue="sex", col="pclass", data=data,logistic=True)

