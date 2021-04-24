#TitanicAnalysis.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family'] = 'Simhei'
matplotlib.rcParams['font.sans-serif'] = ['Simhei']  #正确显示中文字体


data =  np.array([4, 6, 8]) #导入数据（待制）


labels = np.array(['舱位(1st)', '年龄(<45)', '性别(male)'])
nAttr = 3                                            #设置雷达图


angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor = 'white')
plt.subplot(111, polar=True)
plt.plot(angles,data,'bo-',color ='g',linewidth=2)
plt.fill(angles,data,facecolor='g',alpha=0.25)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.25, 0.95, '生存能力值', ha='center')
plt.grid(True)
plt.savefig('TitanicAnalysis.JPG')
plt.show()
