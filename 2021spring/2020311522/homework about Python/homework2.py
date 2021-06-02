import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 一元线性回归模型
#公式：a = y - bx(a,b为参数的拟合值)

#自变量与因变量(引例，x为可支配收入，y为消费支出)
dict_data = {"x" :[2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5],
            "y":[1.6,2.0,2.3,2.4,3.0,3.2,3.1,3.5,3.6,4.4]
}
data = pd.DataFrame(dict_data)
print(data)

#数据准备
list_data1 = np.array([2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5])
list_data2 = np.array([1.6,2.0,2.3,2.4,3.0,3.2,3.1,3.5,3.6,4.4])
AVG_x = np.mean(list_data1)
AVG_y = np.mean(list_data2)

#公式套用
num1 = list_data1 - AVG_x
num2 = list_data2 - AVG_y
sum1 = np.sum([num1 * num2])
sum2 = np.sum(np.square(num1))

final_b = sum1 / sum2
b = final_b.round(3)
print(b)
a = AVG_y - b*AVG_x
print(a)

print("得到的函数是y="+str(a)+"x+"+str(b))

