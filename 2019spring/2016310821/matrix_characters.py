#! /usr/bin/env python3

import numpy as np


#1 cholesky decomposition
x = np.floor(10*np.random.random((4, 3)))
a = x.T @ x
L = np.linalg.cholesky(a)
np.allclose(L @ L.T, a)

#2 qr decomposition
b, c = np.linalg.qr(a)
np.allclose(b @ c, a)

#3 svd composition
u, s, v = np.linalg.svd(x)
np.allclose(u @ np.vstack((np.diag(s), np.array([[0, 0, 0]]))) @ v, x)

#4 egienvalues and right eigenvectors
b, c = np.linalg.eig(a)
np.allclose(c @ np.diag(b) @ np.linalg.inv(c), a)

#5 max(rank(A), rank(B)) <= rank( (A, B) ) <= rank(A + B)
y = np.arange(8).reshape((4, 2))
rx = np.linalg.matrix_rank(x)
ry = np.linalg.matrix_rank(y)
xy = np.hstack((x, y))
rxy = np.linalg.matrix_rank(xy)
max(rx, ry) <= rxy & rxy <= rx+ry
