'''
#绘图专题练习——3D图
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import special
def drumhead_height(n, k, distance, angle, t):
   kth_zero = special.jn_zeros(n, k)[-1]
   return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)
theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
'''
#面膜数据可视化展示
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import median
import seaborn as sns
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

mask = pd.read_csv('mask.csv',encoding="gbk")
mask.loc[mask.店铺所在地 == '英国','店铺所在地']= '海外'
mask.loc[mask.店铺所在地 == '新加坡','店铺所在地'] = '海外'
mask.loc[mask.产地 == '其他/other','产地'] = '其他'
mask.loc[mask.适合肤质 != '任何肤质','适合肤质'] = '其他'
target_list = list(mask['名称'].value_counts()[9:].index)
mask.loc[mask['名称'].apply(lambda x: x in target_list),'名称'] = '其他'

mask1=mask.loc[mask.名称 != '其他']

'''

#条形图
plt.figure(figsize=(12,5))
sns.countplot('名称',data=mask1,order = mask1['名称'].value_counts().index,palette='Blues_r')
plt.xlabel('品牌')
plt.ylabel('数量')
plt.title('热销面膜品牌条形图')
plt.show()

#美化版小提琴图
plt.figure(figsize=(14,8))
sns.swarmplot(x = '名称', y=log(mask1['评价数']), data = mask1,order = mask1['名称'].value_counts().index)
plt.xlabel('品牌')
plt.ylabel('评价数量')
plt.title('热销面膜评价数小提琴图')
plt.show()

#环形图
target_list = list(mask['店铺所在地'].value_counts()[9:].index)
mask.loc[mask['店铺所在地'].apply(lambda x: x in target_list),'店铺所在地'] = '其他'
plt.figure(figsize=(7,7))
mask['店铺所在地'].value_counts().plot.pie(autopct = '%1.2f%%',startangle=90,pctdistance=0.8,colors=sns.color_palette("Set2", 10))   
plt.pie([1],radius=0.6,colors='w') #内部白色饼图
plt.title('热销店铺所在地环形图')
plt.ylabel('')
plt.show()
'''
#相关性图
sns.pairplot(mask[['月销量','评价数','价格','适合肤质']],hue='适合肤质')
plt.show()






