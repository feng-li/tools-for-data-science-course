# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:47:28 2021

@author: Always
"""


# 导入相关库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.dtypes
train.describe()

# 中文字体设置
plt.rcParams['font.sans-serif'] = ['SimHei']    
plt.rcParams['axes.unicode_minus'] = False 
 
# 各属性对应的人数分布
plt.subplot(2,2,1)
sns.countplot(x='Survived', data=train)
plt.title('存活情况')
plt.subplot(2,2,2)
sns.countplot(x='Pclass', data=train)
plt.title('各等级舱人数')
plt.subplot(2,2,3)
sns.countplot(x='Sex', data=train)
plt.title('男女人数')
plt.subplot(2,2,4)
sns.countplot(x='Embarked', data=train)
plt.title('登船港口')
plt.tight_layout()

# 舱等级与存活情况之间的关系
Survived_0 = train.Pclass[train.Survived == 0].value_counts()
Survived_1 = train.Pclass[train.Survived == 1].value_counts()
Pclass_df = pd.DataFrame({'未获救': Survived_0, '获救': Survived_1})
Pclass_df.plot(kind='bar', stacked=True)
plt.title('各乘客舱等级的获救情况')
plt.xlabel('乘客舱等级') 
plt.ylabel('人数') 
plt.show()

# 上船港口与存活情况之间的关系
Survived_0 = train.Embarked[train.Survived == 0].value_counts()
Survived_1 = train.Embarked[train.Survived == 1].value_counts()
Pclass_df = pd.DataFrame({'未获救': Survived_0, '获救': Survived_1})
Pclass_df.plot(kind='bar', stacked=True)
plt.title('不同上传港口乘客的获救情况')
plt.xlabel('乘客上传港口') 
plt.ylabel('人数') 
plt.show()

# 性别与存活情况之间的关系
Survived_0 = train.Sex[train.Survived == 0].value_counts()
Survived_1 = train.Sex[train.Survived == 1].value_counts()
Pclass_df = pd.DataFrame({'未获救': Survived_0, '获救': Survived_1})
Pclass_df.plot(kind='bar', stacked=True)
plt.title('各乘客性别的获救情况')
plt.xlabel('乘客性别') 
plt.ylabel('人数') 
plt.show()
