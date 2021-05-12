# -*- coding: utf-8 -*-
"""
Some useful functions concerning financial calculation.
"""

#ri-rate of an investment
#rf-rate of risk-free
#rm-rate of market portfolios
import numpy as np
import pandas as pd

#calculate the beta rate against the market portfolios
def beta(rm,ri):
    covar=np.cov(rm,ri)
    #print('Convar=',covar)
    
    variance=np.var(rm)
    beta=covar[0][1]/variance#访问列表的数据要用方括号访问而不是圆括号
    return beta

#calculate the sharpe rate of a certain asset given the rate of risk-free
def sharpe(ri,rf):
    return (np.mean(ri)-rf)/np.std(ri)

if __name__=='__main__':
    data=pd.read_excel('FundData.xls')
    #print(data)
    sandp=((data.iloc[:,[1]]).values).transpose()#将数据框转化为数组
    apple=((data.iloc[:,[2]]).values).transpose()
    #apple.head()
    citi=((data.iloc[:,[3]]).values).transpose()
    cisco=((data.iloc[:,[4]]).values).transpose()
    company=[apple,citi,cisco]
    comName=['Apple','Citi','Cisco']
    rf=0.03
    j=0
    #print(beta(sandp,apple))
    for i in company:
        mybeta=beta(sandp,i)
        mysharpe=sharpe(i, rf)
        print("The beta for %s is %4.2f"%(comName[j],mybeta))
        print("The sharpe rate for %s is %4.2f"%(comName[j],mysharpe))
        j+=1