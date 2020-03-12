import numpy as np
#1、计算逆矩阵

A = np.mat("0 1 2;1 0 3;4 -3 8")
inv = np.linalg.inv(A)
print (inv)
# 检查 相乘结果为单位矩阵
print (A * inv)


#2、线性方程组
B = np.mat("1 -2 1;0 2 -8;-4 5 9")
b = np.array([0,8,-9])
x = np.linalg.solve(B,b)
print (x)
#[ 29. 16. 3.]
# 使用dot函数检查求得的解是否正确
print (np.dot(B , x))
print(np.allclose(np.dot(B,x),b))
# [[ 0. 8. -9.]]


# 3. 特征值和特征向量
# 特征值（eigenvalue）即方程 Ax = ax 的根，是一个标量。其中，A 是一个二维矩阵，x 是一个一维向量。特征向量（eigenvector）是关于特征值的向量
# numpy.linalg模块中，eigvals函数可以计算矩阵的特征值，而eig函数可以返回一个包含特征值和对应的特征向量的元组 
C = np.mat("3 -2;1 0")
# 求解特征值
c0 = np.linalg.eigvals(C)
print (c0)
# [ 2. 1.]
# 求解特征值和特征向量 (该函数返回一个元组，按列排放着特征值和对应的特征向量，其中第一列为特征值，第二列为特征向量)
c1,c2 = np.linalg.eig(C)
print (c1)
# [ 2. 1.] 
print (c2)
#[[ 0.89442719 0.70710678]
# [ 0.4472136 0.70710678]] 
# 使用dot函数验证求得的解是否正确
for i in range(len(c1)):
    print("left:",np.dot(C,c2[:,i]))
    print("right:",c1[i] * c2[:,i])


#4、行列式
D = np.mat("3 4;5 6")
print (np.linalg.det(D))
E = np.mat("5 6;3 4")
print (np.linalg.det(E))            

#5、python实现LU分解
import numpy as np
def my_LU(B):
    A = np.array(B)
    n = len(A)
    #print(A)
    L = np.zeros(shape=(n,n))
    U = np.zeros(shape=(n,n))
    for k in range(n-1):
        gauss_vector = A[:,k]
        gauss_vector[k+1:] = gauss_vector[k+1:] / gauss_vector[k]
        gauss_vector[0:k+1] = np.zeros(k+1)
        #print(gauss_vector)
        L[:,k] = gauss_vector
        L[k][k] = 1.0
        #print(L)
        #print(A)
        for l in range(k+1,n):
            B[l,:] = B[l,:] - gauss_vector[l] * B[k,:]
        A = np.array(B)
    L[k+1][k+1] = 1.0
    U = A
    print(U)
    print(L)
def main():
    A = np.array([[2., 2., 3.],
                  [4., 7., 7.],
                  [-2.,4., 5.]])
    my_LU(A)
main()



#参考网址http://www.cnblogs.com/xieshengsen/p/6836430.html
