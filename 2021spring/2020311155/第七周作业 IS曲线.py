# -*- coding = utf-8 -*-
# @Time :2021/4/8 8:27 pm
# @Author : Lily
# @File :第七周作业 IS曲线第七周作业 IS曲线.py
# @Mac :PyCharm

'''IS曲线 美国利率r与产出Y的关系'''
from scipy import stats
import numpy as np
x = 1.67,1.13,1.35,3.22,4.97,5.02,1.92,0.16,0.18,0.1,0.14,0.11,0.09,0.14,
y = 10581.82,11458.24,12213.73,13036.64,13814.61,14451.86,14712.84,14448.93,14492.05,15542.58,16197.01,16784.85,17527.2,18224.7
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print({'slope':slope,'intercept':intercept})
print({'p_value':p_value,'r-squared':round(r_value**2,2)})
# r-square=0.16 emmm看起来r不太能解释Y
