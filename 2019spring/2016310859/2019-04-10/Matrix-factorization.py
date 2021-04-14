#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import linalg

A = np.array([[1,2,3],
			 [4,5,6],
			 [7,8,9]])


# 1. 求方阵的特征值与特征向量
# Av = λv
a, b = linalg.eig(A)
print('特征值与特征向量'.center(40, '='))
print('特征值：', a, 
	  '特征向量：', b, 
	  'check:', np.dot(A, b[:,1]), np.dot(a[1], b[:,1]) , sep='\n\n')


# 2. SVD 分解
# 假设 M 是一个 m×n 的矩阵，其中的元素全部属于数域 K.
# 那么，存在 m×m 的酉矩阵 U 和 n×n 的酉矩阵 V 使得 M=UΣV^{h}.
# 其中 Σ 是 m×n 的非负实数对角矩阵；并且 Σ 对角线上的元素 Σ_{i,i} 是 M 的奇异值.
M,N = A.shape
U,s,Vh = linalg.svd(A)
Sig = linalg.diagsvd(s,M,N)
print('SVD 分解'.center(40, '='))
print('U:', U,
	  '奇异值:', s,
	  'V:', Vh,
	  'check:', U.dot(Sig.dot(Vh)), sep='\n\n')


# 3. QR 分解
# 如果实（复）非奇异矩阵 A 能够化成正交矩阵 Q 与上三角矩阵 R 的乘积，
# 即 A=QR，则称其为 A 的 QR 分解
# A 不必为方阵; 如果 A 大小为 m*n，则矩阵 Q 大小为 m*m，矩阵 R 大小为 m*n
q, r = linalg.qr(A)
print("QR 分解".center(40, '='))
print('Q:', q,
	  'R:', r, 
	  'check:', np.dot(q, r), sep='\n\n')


# 4. LU 分解
# LU分解是矩阵分解的一种，将一个矩阵分解为一个下三角矩阵 L 和一个上三角矩阵 U 的乘积，
# 有时需要再乘上一个置换矩阵 P, 即 A=PLU
P, L, U = linalg.lu(A)
print("LU 分解".center(40, '='))
print('P:', P,
	  'L:', L,
	  'U:', U, 
	  'check:', P.dot(L.dot(U)), sep='\n\n')


# 5. Cholesky 分解
# 将一个正定的埃尔米特矩阵分解成一个下三角矩阵与其共轭转置之乘积，即 A=L*L.H
A = np.array([[4,12,-16],
			  [12,37,-43],
			  [-16,-43,98]])
L = linalg.cholesky(A)
print("Cholesky 分解".center(40, '='))
print('L:', L, 
	  'L.H' , L.T.conj(),
	  'check:', np.dot(L.T.conj(), L), sep='\n\n')