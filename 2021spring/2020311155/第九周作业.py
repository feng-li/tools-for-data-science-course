# -*- coding = utf-8 -*-
# @Time :2021/4/21 8:48 pm
# @Author : Lily
# @File :第九周作业.py
# @Mac :PyCharm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
titanic=sns.load_dataset("titanic")
print(titanic.head())
sns.set(style='darkgrid')
# 存活率与性别
sns.catplot(x='survived',y='sex',kind="bar",data=titanic)
plt.show()
# 存活率与年龄
sns.displot(titanic,x='age',y='survived')
plt.show()

