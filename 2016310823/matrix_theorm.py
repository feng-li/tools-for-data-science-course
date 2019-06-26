# -*- coding: utf-8 -*-

import math
wwwwwrimport numpy as np
from scipy import linalg

a = np.array([[0,1,2],[1,1,4],[2,-1,0]])
b = np.array([[12,25,23],[31,13,11],[24,9,7]])
c = np.array([[11,21],[23,7],[9,22]])


#1.(a+b)c=ac+bc
(a+b).dot(c)==a.dot(c)+b.dot(c)

#2.(ab)c=a(bc)
(a.dot(b)).dot(c)==a.dot(b.dot(c))

#3.a与单位矩阵的乘积等于其本身
a.dot(np.eye(3))==a
np.eye(3).dot(a)==a

#4.(a')'=a
(a.T).T==a

#5.(ab)'=b'a'
a.dot(b).T==b.T.dot(a.T)

#6.(a+b)'=a'+b'
(a+b).T==a.T+b.T

#7.(ka)'=ka'
(2*a).T==2*a.T

#8.行列式转置，值不变
linalg.det(a)==linalg.det(a.T)

#9.一数乘行列式的一行等于此数乘行列式
n=a.copy()
n[0,:]=2*n[0,:]
n
linalg.det(n)==2*linalg.det(a)

#10.行列式两行相同，则行列式为零
e = np.array([[1,2,3],[1,2,3],[2,3,4]])
e
linalg.det(e)

#11.行列式两列成比例，那么行列式为零
f = np.array([[1,2,4],[2,4,5],[3,6,6]])
f
linalg.det(f)==0

#12.把一列的倍数加到另一列，行列式不变
g=a.copy()
g[:,1]=g[:,1]+2*g[:,2]
a
g
math.isclose(linalg.det(a),linalg.det(g),rel_tol=1e-9)

#13.对换行列式两列位置，行列式反号
h=a.copy()
m=h[:,1].copy()
h[:,1]=h[:,2].copy()
h[:,2]=m
a
h
linalg.det(a)
linalg.det(h)

#14.|ab|=|a|*|b|
linalg.det(a.dot(b))
linalg.det(a)*linalg.det(b)

#15.a的逆与a的乘积为单位矩阵
linalg.inv(a).dot(a)

#16.a的逆的转置等于a转置的逆
linalg.inv(a).T
linalg.inv(a.T)

#17.ab积的逆等于b的逆乘a的逆
linalg.inv(a.dot(b))
linalg.inv(b).dot(linalg.inv(a))

#18.矩阵a乘矩阵b等于矩阵d,则矩阵b等于a的逆乘d
d=a.dot(b)
b
linalg.inv(a).dot(d)

#19.矩阵特征值的乘积等于其行列式
ze,mat=linalg.eig(a)
np.prod(ze)
linalg.det(a)
math.isclose(np.prod(ze),linalg.det(a),rel_tol=1e-9)

#20.矩阵a与特征向量的乘积等于其对应特征值与其乘积
a.dot(mat[:,0])
ze[0]*mat[:,0]

