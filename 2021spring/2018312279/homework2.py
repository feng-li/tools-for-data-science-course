# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:50:21 2021

@author: Xiang Luwei
"""
import numpy as np
from sklearn.linear_model import LinearRegression
X = 2 * np.random.rand(100,1)
y = 4 + 3*X + np.random.randn(100,1)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print("截距：",lin_reg.intercept_)
print("系数: ",lin_reg.coef_)
print("拟合方程为:",lin_reg.coef_,"x+",lin_reg.intercept_)