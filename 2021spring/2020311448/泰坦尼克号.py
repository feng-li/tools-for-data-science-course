import pandas as pd
import numpy as np
from pandas import Series,DataFrame
f = open(r'E:\Python\数据分析\data\train.csv')
data_train = pd.read_csv(f)
data_train.describe()
#运行结果
data_train.info()
#运行结果