# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:28:30 2019

@author: dell
"""

from numpy import *
from scipy import * # 有问题：numpy和scipy中都有linalg，但“结果”不同，这种方法不合适

M1 = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

## 计算
#转置
transpose(M1)
#求逆
linalg.inv(M1)
#行列式
linalg.det(M1)
#迹
trace(M1)
#特征值与特征向量
linalg.eig(M1)

#矩阵乘法
M2 = array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
M1
M2
M1*M2 # 对应位置相乘 
dot(M1,M2) # 矩阵乘积

m1 = mat(M1)
m2 = mat(M2)
m1*m2
dot(m1,m2)
multiply(m1,m2)

 #奇异值分解
linalg.svd(M1)
u,s,v = linalg.svd(M1)
s = diag(s)
dot(dot(u,s),v)


m1 = mat(M1)
m2 = mat(M2)
m1*m2
