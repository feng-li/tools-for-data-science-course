# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:21:55 2019

@author: Lee Oscar
"""

import numpy
m1 = numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])

#转置
numpy.transpose(m1)

#求逆
numpy.linalg.inv(m1)

#行列式值
numpy.linalg.det(m1)

#迹
numpy.trace(m1)

#特征值与特征向量
numpy.linalg.eig(m1)

#矩阵相乘
m2 = numpy.matrix([[1,4,7],[8,5,2],[3,6,9]])
m1*m2
numpy.dot(m1,m2)

#奇异值分解
numpy.linalg.svd(m1)

#LU分解
import scipy.linalg
scipy.linalg.lu(m1)

#cholesky分解
scipy.linalg.lu(m1)