import numpy as np
import pandas as pd
#1.标量创建Series对象
print(pd.Series(3.14))
#2.自定义索引
print(pd.Series(3.14,index=['a','b','c']))

#3.字典创建Series对象
dict={'张三':'北京','李四':'上海','王五':'广东'}
print(pd.Series(dict))

#4.生成数组创建Series对象0...N-1
arr=np.random.randn(5)
print(pd.Series(arr))

#5.改变索引
arr=np.random.randn(5)
print(pd.Series(arr,index=['a','b','c','d','e']))


#6.操作一维数组Series
arr=np.random.randn(5)
series=pd.Series(arr)
print(series)
print(series[1])
print(series[2:])
print(series[[3,2,1]])
print(series**2)

data_excel=pd.read_excel("D:\\Test.xlsx")
#1.读取指定具体表格
print(data_excel)

 
