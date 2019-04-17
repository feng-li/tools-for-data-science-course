#!/usr/bin/env python
# coding: utf-8

# In[53]:


# 邓煊洁 2017310901 验证5条矩阵性质
import numpy as np
from scipy import linalg
import random as r
from scipy.sparse import identity

X=np.array([2,5,8])   # 用行向量
A=np.array([[1,2,3],[3,4,5],[4,5,6]])  #A的秩是2，不可逆
B=np.array([[r.randint(0,9) for i in range(3)],[r.randint(0,9) for i in range(3)],[r.randint(0,9) for i in range(3)]]) #随机生成
C=np.array([[-5,6,7],[10,2,-6],[-2,17,10]])  #C可逆
D=np.array([[1,2,3],[2,7,4],[3,4,8]])  #D可逆
E=identity(3).toarray()  #E是三阶单位阵

# 1验证对1<=p<q，有向量x的q范数小于x的p范数
print(linalg.norm(X,5)>linalg.norm(X,6)>linalg.norm(X,50))

# 2验证矩阵范数的相容性
print(linalg.norm(A.dot(B),2)<=linalg.norm(A,2)*linalg.norm(B,2))

# 3证明列选主元LU分解的L矩阵元素<=1,U对角线非零元的个数等于A的秩
P,L,U=linalg.lu(A)
print(P)
print(L)
print(U)
print(np.linalg.matrix_rank(A))

# 4验证矩阵的逆的定义
print((C.dot(linalg.inv(C))==E).all())
print(C.dot(linalg.inv(C)))

# 5验证(CD)^-1=C^-1*D^-1
print(linalg.inv(C.dot(D)))
print(linalg.inv(D).dot(linalg.inv(C)))


# In[20]:


import random as r
B=np.array([[r.randint(0,9) for i in range(3)],[r.randint(0,9) for i in range(3)],[r.randint(0,9) for i in range(3)]])
B

