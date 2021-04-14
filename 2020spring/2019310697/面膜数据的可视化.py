#!/usr/bin/env python
# coding: utf-8

# # 面膜数据的可视化 
# *Homework of week6*      2020.3.27

# ## Preparation

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#解决中文显示问题
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号


# In[2]:


mask = pd.read_csv('C:\\Users\\wendy.wu\\Desktop\\数据科学工具\\可视化\\mask.csv',encoding="gbk")   #数据来源狗熊会
mask.head()


# In[3]:


mask.info()


# In[4]:


print(mask['产地'].unique())
print(mask['店铺所在地'].unique())
print(mask['适合肤质'].unique())


# In[5]:


#店铺所在地为“英国”或“新加坡”的数据，更改为“海外”
mask.loc[mask.店铺所在地 == '英国','店铺所在地']= '海外'
mask.loc[mask.店铺所在地 == '新加坡','店铺所在地'] = '海外'
print(mask['店铺所在地'].unique())


# In[6]:


mask.loc[mask.产地 == '其他/other','产地'] = '其他'


# In[7]:


mask.loc[mask.适合肤质 != '任何肤质','适合肤质'] = '其他'


# ## Exploration 1 条形图

# In[8]:


plt.figure(figsize=(12,5))
sns.countplot('店铺所在地',data=mask,order = mask['店铺所在地'].value_counts().index,palette='Blues_r')
plt.title('店铺所在地分布情况')


# 此条形图统计了所有品牌的面膜店铺所在地的分布情况，但只简单罗列了表格中“店铺所在地”这一列的数据，不能够全方面透视数据。

# In[9]:


fig=plt.figure(figsize=(16,16))
ax=fig.add_subplot(3,2,1)
sns.barplot(x="产地", y="价格",data=mask, estimator=mean,ci=75,order=['美国', '韩国','英国','日本', '其他','中国'],capsize = 0.1,palette='Greens_r') 
plt.title('各产地面膜的平均价格')


# 展示了在各国生产出来的面膜的平均售价，间接反映了各国的生产成本，但仅简单地用“取中位数”的方式联系了表格中产地和价格两列的数据，也没有能透视数据。

# In[11]:


fig=plt.figure(figsize=(12,5))
bardata = mask[['产地','月销量']].groupby(['产地']).median().sort_values(by='月销量',ascending = False).reset_index()
ax=fig.add_subplot(1,2,2)
ax.barh(y = range(bardata.shape[0]),width = bardata.月销量,tick_label = bardata.产地,color = 'Steelblue')
for index,row in bardata.iterrows():
    ax.text(row.月销量,row.name,int(row.月销量),color="black",va="center") #va调整位置
ax.set_title('各产地面膜平均月销量')
ax.set_ylabel('产地')
ax.set_xlabel('平均月销量')
plt.show()


# 展示了各国生产出来的面膜的平均月销量，间接反映了各国的面膜质量与受喜爱程度，但仅简单地用“取平均数”的方式联系了表格中产地和月销量两列的数据，也没有能透视数据。

# ***总结来说，条形图一般只能展现出两个变量间的简单关系（加上hue也可联系三个变量的关系），很难展现出数据更深层的联系。***

# ## Exploration 2 箱线图

# In[12]:


fig=plt.figure(figsize=(16,5))
ax=fig.add_subplot(1,2,2)
sns.boxplot(data=mask,x=log(mask['月销量']),y='产地',orient = "h",whis=1,fliersize=3)
plt.xlabel('log(月销量)')
ax.set_title('各产地面膜平均月销量')


# In[13]:


sns.boxenplot(x='产地',y=log(mask['月销量']),data=mask,palette="Set2")
plt.ylabel('log(月销量)')
plt.title('各产地面膜平均月销量(加强版)')


# 此箱线图虽然只反映月销量和产地表格中两列数据的关系，但将数据的联系展示得更透彻：对于没各产地的月销量，箱线图用上下边缘和上下四分位数线划定了此产地中各种面膜月销量较为精确的分布（加强版更是将数据分布表现得更为清晰），相对条形图的简单取中位数/平均值的操作能更为准确的反映数据。
# **与条形图相比，箱线图突出反映了数据的集中程度，各产地间的月销量重叠区域等信息。**

# ## Exploration 3 直方图 

# In[14]:


fig,axes=plt.subplots(1,2)      #加入参数sharey=True表示公用y坐标
plt.subplots_adjust(wspace=0.4) #子图间距
sns.distplot(mask['月销量'],rug=True,ax=axes[0],hist=False) #去除直方
sns.distplot(mask['价格'],rug=True,ax=axes[1],kde=False)    #去除核密度曲线


# 两个直方图虽然只展示了一一列数据，但却同时展现了其分布及分布密度，是透视单一变量比较有效的方法；但无法展现变量间的关系。

# ## Exploration 4 环形图

# In[16]:


plt.figure(figsize=(7,7))
mask['店铺所在地'].value_counts().plot.pie(autopct = '%1.2f%%',startangle=90,pctdistance=0.8,colors=sns.color_palette("Set3", 10))   
plt.pie([1],radius=0.6,colors='w') #内部白色饼图
plt.ylabel('')
plt.show()


# 环形图也是仅展示了店铺所在地这一个变量的分布情况，却将各自所占总体比例表现得很清晰，这是较条形图的一大优势。

# ## Exploration 5 相关性图

# In[17]:


sns.pairplot(mask[['月销量','评价数','价格','适合肤质']],hue='适合肤质')


# 相关性图展现了个变量间的关联，是两个变量间将关系展示得最清楚的一种图形。

# ## 汇总

# 目标：
# - 将表格中大部分数据都囊括在内
# - 将数据间关联建构得较为清晰，使得能将整个数据透视

# 展示店铺分布：第一时间让顾客清楚店铺分布情况，方便购买。

# In[20]:


plt.figure(figsize=(7,7))
mask['店铺所在地'].value_counts().plot.pie(autopct = '%1.2f%%',startangle=90,pctdistance=0.8,colors=sns.color_palette("Set3", 10))   
plt.pie([1],radius=0.6,colors='w') #内部白色饼图
plt.ylabel('')
plt.show()


# 展示月销量，评价数，价格，适合肤质之间的相关性：让顾客了解各产品情况，方便进一步购买。如对比各产品的月销量与评价数，获得产品受欢迎程度；对比各产品的价格和适合肤质，挑选最适合自己的面膜。

# In[21]:


sns.pairplot(mask[['月销量','评价数','价格','适合肤质']],hue='适合肤质')


# 展示月销量和产地的关系：精确展示各产地产品的月销量情况，方便顾客挑选时同时将产地因素考虑在内。

# In[19]:


sns.boxenplot(x='产地',y=log(mask['月销量']),data=mask,palette="Set2")
plt.ylabel('log(月销量)')
plt.title('各产地面膜平均月销量(加强版)')


# ***End of the homework of this week***
