import pandas
import jieba
import numpy as np
import re

fo = open('D:/ceshi1.txt')
print ("文件名为: ", fo.name)

filelist = fo.readlines()#将txt文件转换为所有的行组成的列表  
numberoflines =len(filelist)#得到行数            
print ("行数: %s" % (numberoflines))
returnMat = np.zeros((numberoflines,3))#生成一个numberoflines行，3列的矩阵
print(returnMat)
classLabelVector =[]
index=0

returnMat[0,:] =[1,2,3]
returnMat[1,:] =[4,5,6]
for line in filelist:#依次读取每行
    line = line.strip()#去掉每行头尾空白 
    listline=line.split('\t')#按换行符分割数据

    returnMat[index,:] =listline[0:3]#将文本数据前三列存入数据矩阵
    classLabelVector.append(int(listline[3]))#第四列以整型存入标签向量，append()函数用于向列表中添加元素
    #classLabelVector[index]=int(listline[3]) 错误，因为没有定义classLabelVector的长度
    index+=1
print(classLabelVector)
print(returnMat)
#关闭文件
fo.close()

