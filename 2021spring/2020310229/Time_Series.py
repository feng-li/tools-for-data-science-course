#!/usr/bin/env python
# coding: utf-8

# In[107]:
"""
This homework is done with the reference to an online resources:
https://mp.weixin.qq.com/s?src=11&timestamp=1617880347&ver=2996&signature=gdKGAXFm0djdZ6WT0YxWV4Xvkx73r7IVMrhKAoCk49s8bRgq3Z*sWQeehh0gUktEorza3H2C0FWzhUCDsbFpynhiE5Hspu35xJlFL78EL09mzQ1unSCLaQuja6ekzkBZ&new=1


"""

import pandas as pd
import matplotlib.pyplot as plt

#这里的路径不太会设置，具体就是仓库中实际利率的那个文件
TSdata = pd.read_excel("..\\实际利率.xlsx")

TSdata.head()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(TSdata["Column1"], TSdata["Column2"])




# In[108]:


#运用ARMA模型

Ct = TSdata[0:53]
"""
plt.plot(Ct["Column1"], Ct["Column2"])
plt.show()
"""



# In[109]:


#模型预处理
from statsmodels.tsa.stattools import adfuller
def ADF(ts):
    dftest=adfuller(ts)
    dfoutput=pd.Series(dftest[0:4],index=["Test Stastics", "p-value","#Lags Used",'Number of observations used'])
    for key,values in dftest[4].items():
        dfoutput["Critical Values(%s)"%key]=values
    return round(dfoutput,4)

print(ADF(Ct["Column2"]))


# In[110]:


#模型拟合

from statsmodels.tsa.arima_model import ARMA

Ct_ARMA = ARMA(Ct["Column2"], order=(4,2)).fit()
print(Ct_ARMA.summary())


# In[116]:


plt.plot(TSdata['Column1'], TSdata["Column2"], "o-")
plt.plot(Ct["Column1"][0:53], Ct_ARMA.fittedvalues, 'o-')

foresee = Ct_ARMA.forecast(6)[0].tolist()
plt.plot(TSdata["Column1"][53:66],foresee,'*-')
plt.show()


# In[118]:


print(TSdata[53:66])
print(foresee)


# In[ ]:





# In[ ]:




