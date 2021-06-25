# -*- coding = utf-8 -*-
# 作者：汪成智
# 学号：2020311476
# 创建时间：2021/4/7 20:56
# 开发环境：PyCharm


#导入需要模块
import numpy as np
import  math as m
import matplotlib.pyplot as plt

#导入数据

set=np.array([[825,3.5],[215,1.0],[1070,4.0],[550,2.0],[480,1.0],[920,3.0],[1350,4.5],[325,1.5],[670,3.0],[1215,5.0]])

#计算 y=ax+b

n = set.shape[0]#得到数据组数
#分别获取点的横纵坐标
set_x=[]
set_y=[]
for i in range(n):
    set_x.append(float(set[i][0]))
    set_y.append(float(set[i][1]))

#计算横坐标平均值
def avg_x(set):
    sum = 0
    for i in range(n):
        sum = sum + set[i][0]
    avgx = sum/n
    return avgx
#计算纵坐标平均值
def avg_y(set):
    sum = 0
    for i in range(n):
        sum = sum + set[i][1]
    avgy = sum/n
    return avgy

def sigmaxx(set, avgx):
    sigma = 0
    for i in range(n):
        sigma = sigma + (set[i][0] - avgx)**2
    return sigma

def sigmayy(set, avgy):
    sigma = 0
    for i in range(n):
        sigma = sigma + (set[i][1] - avgy)**2
    return sigma

def sigmaxy(set,avgx,avgy):
    sigma = 0
    for i in range(n):
        sigma = sigma + (set[i][1] - avgy)*(set[i][0] - avgx)
    return sigma

#计算回归方程b，a
b = round(sigmaxy(set,avg_x(set),avg_y(set))/sigmaxx(set,avg_x(set)),4)
a = round(avg_y(set) - b*avg_x(set),4)

print("回归方程为","y=",b,"x+",a)


fig, ax = plt.subplots()
x = np.linspace(min(set_x),max(set_x),num=5)
y = b*x+a
plt.plot(x,y,color= 'orange',label = 'Fitting Line',linewidth = 2)
plt.legend()#不带参数调用 legend 会自动获取图例句柄及相关标签
ax.scatter(set_x,set_y)
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
fig.suptitle('Categorical Plotting')
plt.show()
