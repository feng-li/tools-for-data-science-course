import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy import interpolate

#一个小函数
def demand_curve(x, a, c):
    return 5*(x-a)**(2)+c

#设置编码，让中文可以在图上显示
mpl.rcParams['font.sans-serif'] = ['SimHei']

#开启一个窗口，num设置子图数量，figsize设置窗口大小，dpi设置分辨率
fig = plt.figure(num=1, figsize=(15, 8),dpi=80)
plt.title("送给小老婆", {"size":24})

#这是和L1相切的无差异曲线
x = np.arange(0, 0.2, 0.01)
y = demand_curve(x, 0.3, 0.6)
plt.plot(x, y, linestyle="--")
#这是和L2相切的无差异曲线
x = np.arange(0.5,0.7,0.01)
y = demand_curve(x, 0.7, 0.35)
plt.plot(x, y, linestyle="--")
#这是和L3相切的无差异曲线
x = np.arange(1.1,1.3,0.01)
y = demand_curve(x, 1.25, 0.3875)
plt.plot(x, y, linestyle="--")

#这是三条切线
plt.plot([0,0.5],[1,0], label="L1", linestyle="-")
plt.plot([0,1],[1,0], label="L2", linestyle="-")
plt.plot([0,2],[1,0], label="L3", linestyle="-")

#这是三条无差异曲线和切线的切点以及一个额外点表示价格-消费曲线，这里我用线性插值的方式把价格-消费曲线补全
x = np.array([0.1, 0.6, 1.2, 1.5])
y = np.array([0.8, 0.4, 0.4, 0.5])
xnew = np.arange(0.1,1.5,0.01)
func = interpolate.interp1d(x, y, kind='quadratic')
ynew = func(xnew)
plt.plot(xnew,ynew,label="价格-消费曲线",linestyle="-.")

#这是三个切点
plt.plot(0.1, 0.8, 'rs', 0.6, 0.4, 'bs', 1.2, 0.4, 'ys')

#这些是图例以及坐标轴显示范围 
plt.legend(["U1", "U2", "U3", "L1", "L2", "L3","价格-消费曲线", "A", "B", "C"], loc=0, ncol=2, prop={"size":20})
plt.xlim(0,2.2)
plt.ylim(0,1.2)
plt.xlabel("食物（单位/月）",{"size":20})
plt.ylabel("衣服（单位/月）",{"size":20})
#让坐标轴刻度隐身
plt.xticks([])
plt.yticks([])

#显示绘图结果
plt.show()
