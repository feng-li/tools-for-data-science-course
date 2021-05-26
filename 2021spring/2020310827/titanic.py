# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:43:20 2021

@author: Vicky Lamperouge
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#中文体设置
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcparams['axes.unicode_minus'] = False

#船舱等级和存活情况对应的人数分布
plt.subplot(2,2,1)
sns.countplot(x='Survived',data=train)
plt.title('存活情况')
plt.subplot(2,2,2)
sns.countplot(x='Pclass',data=train)
plt.title('各等级船舱人数')

#船舱等级与存活情况之间的关系
survived_0 = train.Pclass[train.survived == 0].value_counts()
survived_1 = train.Pclass[train.survived == 1].value_counts()
Pclass_df = pd.DataFrame({'未获救':survived_0,'获救':survived_1})
Pclass_df.plot(kind='bar',stacked=True)
plt.title('船舱等级与存活情况之间的关系')
plt.xlabel('船舱等级')
plt.ylabel('人数')
plt.show