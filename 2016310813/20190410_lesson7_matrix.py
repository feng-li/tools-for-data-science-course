
# coding: utf-8

# In[27]:

import csv
import os
import numpy as np
import random
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from random import randint


# In[28]:

# 性质1：行列互换：行列式不变

# 思路：
# (1)随机生成一个矩阵mat1，得到mat1的行列式为det1
# (2)将矩阵转置，得到mat2,得到mat2的行列式为det2
# (3)判断det1和det2是否相等，输出结果为True
n = 5                                      # (1)n决定矩阵是n行n列的
t = [random.randint(0,10) for _ in range(n**2)];mat1 = np.matrix(t).reshape(n,n)   # 随机生成一个n行n列的矩阵
mat2 = np.transpose(mat1)                  # (2)mat2为mat1转置后的矩阵
np.linalg.det(mat1) - np.linalg.det(mat2)  # (3)求mat1和mat2相差的值,变量记为a,看结果是否为0

# 验算多次结果为0，验证得到性质1正确

# ————————————————————————————————————————


# In[30]:

# 性质2：如果行列式中的一行为0，那么行列式为0

# 思路：
# (1)随机生成一个n*n的矩阵mat
# (2)随机生成一个数a(a的取值范围为(1,n)),让矩阵mat第a列的元素都为0
# (3)判断mat的行列式det的值是否为0，结果为True

a = randint(1, n)                   # (2)随机生成一个数a
mat1[a,:]=0                           # 让第a行的元素都为0
np.linalg.det(mat1)==0                         # (3)判断矩阵mat的行列式是否为0

# 验算多次结果为True，验证得到性质2正确

# ————————————————————————————————————————


# In[32]:

# 性质3：如果某一行是两组数的和，那么这个行列式就等于两个行列式的和，而这
#        两个行列式除这一行以外全与原来行列式的对应的行一样

# 思路：
# (1)随机生成一个n*n的矩阵mat
# (2)随机生成两组随机数，将这两组数代入矩阵mat中第a行，得到两个新矩阵mat1,mat2
# (3)将两组随机数相加，代入矩阵mat第a行，得到mat3
# (4)判断矩阵mat3的行列式是否等于mat1,mat2的行列式的和
n = 5                                      # (1)n决定矩阵是n行n列的
t = [random.randint(0,10) for _ in range(n**2)];mat = np.matrix(t).reshape(n,n)   # 随机生成一个n行n列的矩阵
c1=random.uniform(0,1)                     # (2)随机生成两组[0,1]的均匀分布的随机数随机数
c2=random.uniform(0,1)
c3=c1+c2 
a=random.randrange(1, n)                    # 随机生成一个数a
mat[a,:]=c1                          # 让第a行的元素都为0
mat1=mat                            # 得到新矩阵mat1
mat[a,:]=c2   
mat2=mat                            # 得到新矩阵mat2
mat[a,]=c3   
mat3=mat                            # (3)得到新矩阵mat2
np.linalg.det(mat1)+np.linalg.det(mat2)-np.linalg.det(mat3)       # (4)矩阵mat1,mat2的行列式相加后减去矩阵mat3行列式

# 验算多次结果为0，验证得到性质3正确


# In[35]:

# 性质4：如果行列式中有两行相同，那么行列式为0

# 思路：
# (1)随机生成一个n*n的矩阵mat
# (2)随机生成一组随机数，将这两组数代入矩阵mat中某两行，得到新矩阵mat1
# (3)判断新矩阵mat1的行列式是否等于0

n = 5                                      # (1)n决定矩阵是n行n列的
t = [random.randint(0,10) for _ in range(n**2)];mat = np.matrix(t).reshape(n,n)   # 随机生成一个n行n列的矩阵
c1=[random.uniform(0,1) for _ in range(n)]           # (2)随机生成一组[0,1]的均匀分布的随机数随机数                  
r=[random.randrange(1, n) for _ in range(2)]             # 随机生成两个数a,b
a=r[0]
b=r[1]                
mat[a,:]=c1                          # 让第a,b行的元素相同
mat[b,:]=c1 
mat1=mat                            # 得到新矩阵mat1
np.linalg.det(mat1)                           # (3)求出矩阵mat1的行列式

# 验算多次结果为0，验证得到性质4正确

# ————————————————————————————————————————


# In[47]:

# 性质5：如果行列式中有两行成比例，那么行列式为0

# 思路：
# (1)随机生成一个n*n的矩阵mat
# (2)随机生成一组随机数c1，并得到c1的倍数c2，令c2为c1的m倍
# (3)将这两组数分别代入矩阵mat中某两行，得到新矩阵mat1
# (4)判断新矩阵mat1的行列式是否等于0

n = 5                                      # (1)n决定矩阵是n行n列的
t = [random.randint(0,10) for _ in range(n**2)];mat = np.matrix(t).reshape(n,n)   # 随机生成一个n行n列的矩阵
c1=[random.uniform(0,1) for _ in range(n)]           # (2)随机生成一组[0,1]的均匀分布的随机数随机数                  
m=random.randrange(1, 20)                     # 随机抽取倍数m
c2=[i*m for i in c1]                          # 得到第二组数c2
r=[random.randrange(1, n) for _ in range(2)]             # 随机生成两个数a,b
a=r[0]
b=r[1]
mat[a,:]=c1                          # 让第a行的元素为c1
mat[b,:]=c2                          # 让第b行的元素为c2
mat1=mat                            # 得到新矩阵mat1
np.linalg.det(mat1)                           # (3)求出矩阵mat1的行列式，判断是否为0
# 验算多次结果为0，验证得到性质5正确


# In[65]:

# 性质6：把一行的倍数加到另一行，行列式不变

# 思路：
# (1)随机生成一个n*n的矩阵mat1
# (2)随机取第a行，让第b行加上a行的m倍，得到新的矩阵mat2
# (3)判断两个矩阵的行列式之差是否为0

n = 5                                      # (1)n决定矩阵是n行n列的
t = [random.randint(0,10) for _ in range(n**2)];mat = np.matrix(t).reshape(n,n)   # 随机生成一个n行n列的矩阵
mat1=mat                            # 生成的矩阵记为mat1
m=random.randrange(1, 20)                     # 随机抽取倍数m
r=[random.randrange(1, n) for _ in range(2)]             # 随机生成两个数a,b
a=r[0]
b=r[1]
c1=mat[a,:]                          # 取出矩阵第a行的元素
k = [];                              # 让第b行的元素加上第a行元素的m倍
for i,j in zip([i*m for i in c1],mat[b,:]):
    k.append(i+j)
mat[b,:] = k
mat2=mat                            # 得到新矩阵mat2
np.linalg.det(mat1)-np.linalg.det(mat2)                 # (3)求出矩阵mat1和mat2的行列式之差，判断是否为0

