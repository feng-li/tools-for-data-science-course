# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:34:52 2019

@author: tutuxy
"""

import numpy as np
#这个方式使用numpy的函数时，需要以np.开头。

#1.1矩阵的加法交换律A+B=B+A
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
A+B == B+A

#1.2加法结合律(A+B)+C=A+(B+C)
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
C = np.mat([[1,1],[1,1]])
(A+B)+C == A+(B+C)

#2.1数λ乘矩阵A结合律(λμ)A=λ(μA);(λ+μ)A=λA+μA
λ = 2
μ = 3
A = np.mat([[3,-1],[2,0]])
(λ*μ)*A == λ*(μ*A)
(λ+μ)*A == λ*A+μ*A

#2.2分配律λ(A+B)=λA+λB
λ = 2
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
λ*(A+B) == λ*A+λ*B

#3.1矩阵的乘法结合律（AB)C=A(BC)
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
C = np.mat([[1,1],[1,1]])
(A*B)*C == A*(B*C)

#3.2乘法分配律 右分配律(A+-B)C=AC+-BC,左分配律A(B+-C)=AB+-AC
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
C = np.mat([[1,1],[1,1]])
(A+B)*C == A*C+B*C
(A-B)*C == A*C-B*C
A*(B+C) == A*B+A*C
A*(B-C) == A*B-A*C

#3.3(λA)B=λ(AB)=A(λB)
λ = 2
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
(λ*A)*B == λ*(A*B)
λ*(A*B) == A*(λ*B)

#4.1矩阵的转置(A')'=A
A = np.mat([[3,-1],[2,0]])
A.T.T == A

#4.2(A+B)'=A'+B'
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
(A+B).T == A.T+B.T

#4.3(AB)'=B'A'
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
(A*B).T == B.T*A.T

#4.4(λA)'=λA'
λ = 2
A = np.mat([[3,-1],[2,0]])
(λ*A).T == λ*A.T

#5.1矩阵的行列式|A'|=|A|
A = np.mat([[3,-1],[2,0]])
np.linalg.det(A.T) == np.linalg.det(A)

#5.2|AB|=|A||B|
A = np.mat([[3,-1],[2,0]])
B = np.mat([[-7,2],[3,5]])
np.linalg.det(A*B) == np.linalg.det(A)*np.linalg.det(B)

#5.3|λA|=λ^n|A|(A的阶数为n)
λ = 2
A = np.mat([[3,-1],[2,0]])
m,n = A.shape
if m==n:
    if abs(np.linalg.det(λ*A)-λ**m*np.linalg.det(A)) < 1e-3:
        print(True)

#practice
a1=np.array([1,2,3])
a1

a1=np.mat(a1)
a1
np.shape(a1)

b=np.matrix([1,2,3])
np.shape(b)

data1=np.mat(np.zeros((3,3))) 
#创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
data1

data2=np.mat(np.ones((2,4))) 
#创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
data2

data3=np.mat(np.random.rand(2,2)) 
#这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，
#需要将其转换成#matrix
data3

data4=np.mat(np.random.randint(10,size=(3,3))) 
#生成一个3*3的0-10之间的随机整数矩阵，如果需要指定下界则可以多加一个参数
data4

data5=np.mat(np.random.randint(2,8,size=(2,5))) #产生一个2-8之间的随机整数矩阵
data5

data6=np.mat(np.eye(2,2,dtype=int)) #产生一个2*2的对角矩阵
data6

a1=[1,2,3]
a2=np.mat(np.diag(a1)) #生成一个对角线为1、2、3的对角矩阵
a2

a1 = np.mat([1,2])
a2 = np.mat([[1],[2]])
a3 = a1*a2
a3
a = np.mat([[1,2]])
a
a1 = np.mat([1,1])
a2 = np.mat([2,2])
a3 = np.multiply(a1,a2)
a3
a1 = np.mat([2,2])
a2 = a1*2
a2
a1 = np.mat(np.eye(2,2)*0.5)
a1
a2 = a1.I
a2
a1 = np.mat([[1,1],[0,0]])
a1
a2 = a1.T
a2
a1 = np.mat([[1,1],[2,3],[4,2]])
a1
a2 = a1.sum(axis = 0)#列
a2
a3 = a1.sum(axis = 1)
a3
a4 = sum(a1[0,:])
a4
a1.max()
a2 = np.max(a1[:,1])
a2
a1[1,:].max()
np.max(a1,0)
np.max(a1,1)
np.argmax(a1,0)
np.argmax(a1[1,:])
a1
a = np.mat(np.ones((3,3)))
a
b = a[1:,1:]
b
a = np.mat(np.ones((2,2)))
a
b = np.mat(np.eye(2))
b
c = np.vstack((a,b))
c
d = np.hstack((a,b))
d

l1 = [[1],'hello',3]
a = np.array([[2],[1]])
a
dimension = a.ndim
dimension
m,n = a.shape
m
n
number = a.size
number
str = a.dtype
str
a1 = [[1,2],[3,2],[5,2]]
a1
a2 = np.array(a1)
a2
a3 = np.mat(a1)
a3
a4 = np.array(a3)
a4
a41 = a3.getA()
a41
a5 = a3.tolist()
a5
a6 = a2.tolist()
a6

a1=[1,2,3]
a2=np.array(a1)
a2
a3=np.mat(a1)
a3
a4=a2.tolist()
a4
a5=a3.tolist()
a5
a6=(a4==a5)
a6
a7=(a4 == a5[0])
a7