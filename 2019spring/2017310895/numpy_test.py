import numpy as np
import numpy.matlib 

#计算矩阵的乘法
a=np.array([[1,2],[3,4]])
b=np.array([[11,12],[13,14]])
print(np.dot(a,b))

#计算两个向量的点积
print(np.vdot(a,b))

#计算向量的内积
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))

#计算矩阵的行列式
print(np.linalg.det(a))

#求逆
print("矩阵a：")
print(a)
print("矩阵的逆")
print(np.linalg.inv(a))

#解方程
print("矩阵c：")
c=np.array([[3],[6]])
print(b)
print("计算：a^(-1)c")
print(np.linalg.solve(a,c))

#创建0矩阵
print(np.matlib.zeros((2,2)))

#创建单位矩阵
print(np.matlib.eye(n=3,M=3,k=0,dtype=float))

#求特征根，特征向量
print("a的特征根和特征向量是：")
print(np.linalg.eig(a))

#求广义逆矩阵
print("求解广义逆矩阵：")
d=np.array([[1,2],[4,8]])
print("d",d)
print(np.linalg.pinv(d))

#做矩阵除法
print("divide的结果")
print(np.divide(a,b))
