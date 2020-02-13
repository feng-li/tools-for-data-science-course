#统计模型 包的介绍

#NumPy #n维数据操作方法
#Scipy
#integrate #数值积分
#linalg #求逆 行列式 等
#主成分分析法
#pandas #数据框
#matplotlib #画图

#打开文件
#open('ii.txt','a')
#fire_for_writing.close()

#with open(firename,'r') as f:
#   data = function_that_get_data_from(f)


#方法一
#! /Usr/bin/ecv python3
# hash_check.py
import re
starts_with_hash = 0
with open('方程有无解.py','r',encoding='gb18030',errors='ignore') as file:  
    for line in file:
        if re.match('#',line):
            starts_with_hash += 1
print(starts_with_hash)


#方法二
starts_with_hash2 = 0
file2 = open("方程有无解.py",encoding='gb18030',errors='ignore')
cf = file2.read()
for line in cf:
    if re.match('#',line):
        starts_with_hash2 += 1
print(starts_with_hash2)
file2.close()

import pandas
data2 = pandas.read_csv('beijing1.csv', delimiter = 't', header = None)
print(len(data2))
#搞成数据框
#read_hdf read_sql等等

#打开压缩包，不需要解压即可打开
import zipfile
myzip = zipfile.ZipFile('beijing1.zip')
myzip.filename
myzip.namelist()
pandas.read_csv(myzip.open('beijing1.csv'))

#切换路径
import os
os,ch
os.chdir('/data1')

#矩阵
b.T  转置
A*b  点乘
A.dot(b.T)  A乘b
linalg.inv(A).dot(b)  求解线性方程组
np.linalg
linalg.det 行列式
lstsq 广义逆
plt.plot(x,y,)


特征向量特征值 norm模
SVD奇异值分解
QR分解
LU分解

统计分布函数
norm.rvs(loc = 0,scale = 1, size = 1000)

画密度
直方图
fg,ax = plt.subplots(1,1)
线性回归


作业：linalg
5-10个线性代数工具
