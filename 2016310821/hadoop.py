# /usr/bin/python3
import numpy as np
import pandas as pd
x = pd.DataFrame(np.random.randn(1000, 100)) #创建100000随机数的数据框
x.shape

import time
start_time = time.clock()
mean = x.apply(sum, 0)                       #计算均值
mean = mean.sum()/100000
end_time = time.clock()
print('cost time: ', end_time-start_time, 's')
mean

y = pd.DataFrame(np.array([x[i]-mean for i in range(100)]).reshape((1000, 100)))
SS = y.apply(lambda m: m**2, 1)
SSE = SS.apply(sum, 0)
SSE.sum()/100000                             #计算方差
