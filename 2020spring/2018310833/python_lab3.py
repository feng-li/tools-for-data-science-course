#这个实在不会
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import *
import time
 
 

def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))  
def trainLogRegres(train_x, train_y, opts):
    
    startTime = time.time()
 
    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha']
    maxIter = opts['maxIter']
    weights = ones((numFeatures, 1))
 
    
    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':  # gradient descent algorilthm
            output = sigmoid(train_x * weights)
            error = train_y - output  
            weights = weights + alpha * train_x.transpose() * error
        elif opts['optimizeType'] == 'stocGradDescent':  # stochastic gradient descent
            for i in range(numSamples):
                output = sigmoid(train_x[i, :] * weights)
                error = train_y[i, 0] - output
                weights = weights + alpha * train_x[i, :].transpose() * error 
        elif opts['optimizeType'] == 'smoothStocGradDescent':  # smooth stochastic gradient descent
            # randomly select samples to optimize for reducing cycle fluctuations
            dataIndex = range(numSamples)
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights = weights + alpha * train_x[randIndex, :].transpose() * error
                del (dataIndex[randIndex])  # during one interation, delete the optimized sample
        else:
            raise NameError('Not support optimize method type!')
    return weights
 
 

def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    for i in range(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5  
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy
 
 
def showLogRegres(weights, train_x, train_y):
    # notice: train_x and train_y is mat datatype
    numSamples, numFeatures = shape(train_x)
    if numFeatures != 3:
        print
        "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1
 
    # draw all samples
    for i in range(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')
 
    # draw the classify line
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    weights = weights.getA()  # convert mat to array
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1');
    plt.ylabel('X2')
    plt.show()
 
 
 
def loadData():
    train_x = []
    train_y = []
    fileIn = open('C:/Users/Jellysillyfish/Desktop/工作簿1.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()
 
 
## step 1: load data

train_x, train_y = loadData()
test_x = train_x
test_y = train_y
 
## step 2: training...

opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)
 
## step 3: testing

accuracy = testLogRegres(optimalWeights, test_x, test_y)
 
## step 4: show the result
print('The classify accuracy is: %.3f%%' % (accuracy * 100))
showLogRegres(optimalWeights, train_x, train_y)


#mask

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
mask = pd.read_csv('C:/Users/Jellysillyfish/Desktop/ISTIC/数据科学工具/课件/面膜数据可视化案例/mask.csv',encoding = "gbk")  
mask.info()
mask.loc[mask.店铺所在地 == '英国','店铺所在地']= '海外'
mask.loc[mask.店铺所在地 == '新加坡','店铺所在地'] = '海外'
print(mask['店铺所在地'].unique())
mask.loc[mask.产地 == '其他/other','产地'] = '其他'
print(mask['产地'].unique())
mask.loc[mask.适合肤质 != '任何肤质','适合肤质'] = '其他'
print(mask['适合肤质'].unique())

#各地区店铺数量直方图
plt.figure(figsize=(12,5))
sns.countplot('店铺所在地',data=mask,order = mask['店铺所在地'].value_counts().index,palette='Greens_r')
plt.show()

#箱线图
fig=plt.figure(figsize=(16,5))
ax=fig.add_subplot(1,2,1)
sns.boxplot(data=mask,x='产地',y=log(mask['价格']),hue='适合肤质',notch = True) #中位数置信区间
plt.ylabel('log(价格)')
ax=fig.add_subplot(1,2,2)
sns.boxplot(data=mask,x=log(mask['月销量']),y='产地',orient = "h",whis=1,fliersize=3)
plt.xlabel('log(月销量)')
plt.show()

#相关性散点图
sns.pairplot(mask[['月销量','评价数','价格','适合肤质']],hue='适合肤质')
plt.show()

#joint plot
x = mask.月销量
y = mask.价格
sns.jointplot(x,y,kind = 'hex')
sns.jointplot(x,y,kind = 'kde')
sns.jointplot(x,y,kind = 'reg')
sns.jointplot(x,y,kind = 'resid')
plt.show()

#相关性热力图
sns.heatmap(mask[['月销量','评价数','价格']].corr())
plt.show()
