#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  
mask = pd.read_csv('D:/Learning materials/tools-for-data-science-course/课件/面膜数据可视化案例/mask.csv',encoding="gbk")   
mask.head()


# In[5]:


mask.info()


# In[6]:


sns.palplot(sns.color_palette())
plt.xlabel('当前')
sns.palplot(sns.color_palette("Paired", 10))
plt.xlabel('Paired')
# sns.palplot(sns.color_palette("BrBG", 10))
# plt.xlabel('BrBG')
# sns.palplot(sns.color_palette("Set1", 10))
# plt.xlabel('Set1')
# sns.palplot(sns.color_palette("Set2", 10))
# plt.xlabel('Set2')
# sns.palplot(sns.color_palette("Set3", 10))
# plt.xlabel('Set3')
# sns.palplot(sns.color_palette("hls", 10))
# plt.xlabel('hls')
# sns.palplot(sns.color_palette("husl", 10))
# plt.xlabel('husl')

#渐变色
sns.palplot(sns.color_palette("Blues", 10))
plt.xlabel('Blues')
sns.palplot(sns.color_palette("Blues_r", 10))
plt.xlabel('Blues_r')
# sns.palplot(sns.color_palette("Greens_r", 10))
# plt.xlabel('Greens_r')
# sns.palplot(sns.color_palette("Reds_r", 10))
# plt.xlabel('Reds_r')


# In[7]:


plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
 
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])
 
plt.subplot(235)
plt.plot([0,1],[0,3])
 
plt.subplot(236)
plt.plot([0,1],[0,4])
 
plt.show()  # 展示


# In[8]:


import numpy as np
x = np.linspace(0,20)
y1 = np.linspace(0,20)
y2 = np.sin(x/3)

fig,ax1=plt.subplots(figsize = (10,5))
ax1.plot(x,y1,c='g',alpha=0.6)
ax2 = ax1.twinx() ##双轴
ax2.plot(x,y2,c='b',alpha=0.6)


# In[9]:


plt.figure(figsize=(6,6))
x = np.arange(0, 5, 0.2)
plt.xlim((0,6)) #设置x轴范围，y轴同理
#'r--'首字母代表颜色，后面符号代表形状
plt.plot(x, x, 'r--', x, x**1.2, 'ys', x, x**1.3, 'g^',x,x**1.4,'co',x,x**1.5,'mv',x,x**1.6,'k:') 
plt.show()


# In[10]:


plt.figure(figsize=(12,5))
sns.countplot('店铺所在地',data=mask,order = mask['店铺所在地'].value_counts().index,palette='Greens_r')


# In[11]:


from numpy import median

fig=plt.figure(figsize=(16,16))
ax=fig.add_subplot(3,2,1)
sns.barplot(x="产地", y="价格",data=mask, estimator=mean,ci=75,order=['美国', '韩国','英国','日本', '其他','中国'],capsize = 0.05) 
plt.title('指定order和capsize = 0.05')

ax=fig.add_subplot(3,2,2)
sns.barplot(x="产地", y="月销量", data=mask, estimator=median,ci=20,color="salmon")
plt.xticks(rotation=-30) #旋转标签
plt.title('指定color')

ax=fig.add_subplot(3,2,3)
sns.barplot(x="产地", y="月销量",hue="适合肤质", data=mask, estimator=median,ci=20)
plt.title('指定hue')
plt.legend(loc='upper right')

ax=fig.add_subplot(3,2,4)
sns.barplot(x="产地", y="月销量", data=mask, estimator=median,ci=20,color="salmon",saturation=1.2)
plt.title('指定saturation')

ax=fig.add_subplot(3,2,5)
bardata = mask[['产地','月销量']].groupby(['产地']).median().sort_values(by='月销量',ascending = False).reset_index()
g = sns.barplot(x="产地", y="月销量",data=bardata, palette="Paired")
for index,row in bardata.iterrows():
    g.text(row.name,row.月销量,int(row.月销量),color="black",ha="center") #ha调整位置
plt.title('指定palette和标签')

ax=fig.add_subplot(3,2,6)
g = sns.barplot(x="月销量", y="产地",data=bardata, palette="Paired",orient = "h")
for index,row in bardata.iterrows():
    g.text(row.月销量,row.name,int(row.月销量),color="black",va="center") #va调整位置
plt.title('指定orient和标签')##注意改变x和y

#plt.savefig('bar.png',dpi=500)
plt.show()

