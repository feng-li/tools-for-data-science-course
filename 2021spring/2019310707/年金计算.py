# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:11:05 2021

@author: Dell Wang
"""

import numpy as np 
c=np.array(c)
r=np.array(r)
if when==1:
n=np.arange(1,n+1)
else:
n=np.arange(0,n)
pv=c/(1+r)**n
return pv.sum()
pv1=pv_f(c,r,n,when=1)
print("普通年金现值（年末）：%.2f"% pv1)
pv2=pv_f(c,r,n,when=0)
print("预付年金现值（年初）：%.2f" % pv2)
import numpy as np
print("numpy自带公式计算（年末）：{:.2f}".format(np.pv(r,5,-c),when=0))
print("numpy自带公式计算（年初）：{:.2f}".format(np.pv(r,5,-c,when=1)))

