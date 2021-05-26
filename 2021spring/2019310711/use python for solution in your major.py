#计算现金流现值
def pv_f(c,r,n,op):
    '''
    c：每期现金流
    r：贴现率
    n：为期数
    op=1表示期末支付
    op=0表示期初支付
    '''
    import numpy as np
    c=np.array(c)
    r=np.array(r)
    if op==1:
        n=np.arange(1,n+1)
    else:
        n=np.arange(0,n)
    pv=c/(1+r)**n
    return pv.sum()

c=[100,85,110,163]
r=[0.01,0.01,0.02,0.03]
print(pv_f(c,r,4,1))
