#!/usr/bin/env python
# coding: utf-8

# ## 加载模块及数据导入

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#解决中文显示问题
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号


# In[4]:


mask = pd.read_csv('mask.csv',encoding="gbk")   #数据来源狗熊会
mask.head()


# In[5]:


print(mask['产地'].unique())
print(mask['店铺所在地'].unique())
print(mask['适合肤质'].unique())


# 店铺所在地的分类中，“英国”、“新加坡”与“海外”有重叠

# In[6]:


#店铺所在地为“英国”或“新加坡”的数据，更改为“海外”
mask.loc[mask.店铺所在地 == '英国','店铺所在地']= '海外'
mask.loc[mask.店铺所在地 == '新加坡','店铺所在地'] = '海外'
print(mask['店铺所在地'].unique())


# In[7]:


mask.loc[mask.产地 == '其他/other','产地'] = '其他'


# In[8]:


mask.loc[mask.适合肤质 != '任何肤质','适合肤质'] = '其他'


# ## 可视化

# ### 条形图

# #### sns.countplot计数条形图

# countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)

# In[148]:


#help(sns.countplot)


# In[147]:


plt.figure(figsize=(12,5))
sns.countplot('店铺所在地',data=mask,order = mask['店铺所在地'].value_counts().index,palette='Greens_r')


# #### sns.barplot

# barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean at 0x000001E8E4BE0268>, ci=95, n_boot=1000, units=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)
# 
# ci表示置信区间； 
# 
# estimator = mean表示取各类的均值；median表示取各类的中位数；
# 
# 指定color来改成单一颜色；palette指定调色板，saturation=0.5改变颜色饱和度；  
# 
# hue指定分类变量；  
# 
# order表示x的顺序；hue_order指定hue的顺序；  
# 
# orient = "h"表示绘制水平horizontal条形图；
# 
# errcolor = 'blue',指定误差棒的颜色； errwidth=2,指定误差棒的线宽；capsize = 0.05 指定误差棒两端线条的宽度；  

# In[12]:


#help(sns.barplot)


# In[19]:


from numpy import median

fig=plt.figure(figsize=(16,16))
ax=fig.add_subplot(2,2,1)
sns.barplot(x="产地", y="价格",data=mask, estimator=mean,ci=75,order=['美国', '韩国','英国','日本', '其他','中国'],capsize = 0.05) 



ax=fig.add_subplot(2,2,2)
sns.barplot(x="产地", y="月销量",hue="适合肤质", data=mask, estimator=median,ci=20)
plt.title('指定hue')
plt.legend(loc='upper right')




#plt.savefig('bar.png',dpi=500)
plt.show()


# In[31]:


fig= plt.figure(figsize=(20,6))

g = sns.barplot(x="月销量", y="产地",data=bardata, palette="Paired",orient = "h")
for index,row in bardata.iterrows():
    g.text(row.月销量,row.name,int(row.月销量),color="black",va="center") #va调整位置
plt.title('指定orient和标签')##注意改变x和y

#plt.savefig('bar.png',dpi=500)
plt.show()


# ### 箱线图

# #### boxplot

# boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)
# 
# width：float，箱的宽度  
# notch = True表示以凹槽显示中位数的置信区间；  
# fliersize：float，离群值点的大小；  
# whis：float，离群值范围（Q3+whis*IQR,+∞)和(-∞,Q1-whis*IQR)

# In[11]:


#help(sns.boxplot)


# In[38]:


'''加强版箱线图'''
#help(sns.boxenplot)

sns.boxenplot(x='产地',y=log(mask['月销量']),data=mask,palette="Set3")
plt.ylabel('log(月销量)')
#plt.savefig('box.png',dpi=500)


# #### swarmplot 

# In[45]:


'''美化版小提琴图'''
#help(sns.swarmplot)

plt.figure(figsize=(14,8))
sns.swarmplot(x=mask['适合肤质'],y=log(mask['月销量']),data=mask)
plt.ylabel('log(月销量)')


# ### 直方图 

# distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)  

# In[70]:


gongneng=['补水保湿','美白提亮','控油祛痘','清洁毛孔','提拉紧致']
y=array([1003791,663420,406096,505381,242276])
plt.bar(gongneng,y,color='turquoise')
plt.ylabel("月销量")

### 饼图
# pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)  
# 
# autopct设置数据标签；pctdistance数据标签的距离圆心位置：0~1；  
# labeldistance: label与圆心距离>1;  
# explode: 饼与圆心的距离(列表形式)  
# startangle起始角度；  
# shadow=True增加阴影，立体效果；  
# 

# In[78]:


#环形图
plt.figure(figsize=(7,7))
mask['店铺所在地'].value_counts().plot.pie(autopct = '%1.2f%%',startangle=90,pctdistance=0.8,colors=sns.color_palette("Set3", 10))   
plt.pie([1],radius=0.6,colors='w') #内部白色饼图
plt.ylabel('')
plt.show()


# ### 相关性图

# #### 相关性散点图

# In[131]:


sns.pairplot(mask[['月销量','评价数','价格','适合肤质']],hue='适合肤质')


# #### joint plot图

# jointplot(x, y, data=None, kind='scatter', stat_func=None, color=None, height=6, ratio=5, space=0.2, dropna=True, xlim=None, ylim=None, joint_kws=None, marginal_kws=None, annot_kws=None, **kwargs)  
# 
# kind : { "scatter" | "reg" | "resid" | "kde" | "hex" }

# In[51]:


x = mask['价格']
y = mask['月销量']

fig=plt.figure(figsize=(3,3))
sns.jointplot(x,y,kind = 'reg')
plt.show()


# #### 相关性热力图

# In[134]:


sns.heatmap(mask[['月销量','评价数','价格']].corr())

