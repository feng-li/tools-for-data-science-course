#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy import linalg
A=np.array([[1,2],[3,4]])
A


# In[3]:


linalg.inv(A)


# In[4]:


A.T


# In[5]:


b=np.array([[1,2]])
A*b


# In[6]:


A.dot(b.T)


# In[11]:


b=np.array([[5],[6]])
b


# In[12]:


linalg.inv(A).dot(b)


# In[14]:


A.dot(linalg.inv(A).dot(b))-b


# In[15]:


np.linalg.solve(A,b)


# In[16]:


linalg.det(A)


# In[18]:


A=np.array([[1,5,3],[2,7,9]])
M,N=A.shape
U,s,Vh=linalg.svd(A)
Sig=linalg.diagsvd(s,M,N)
Sig


# In[19]:


U


# In[20]:


Vh


# In[21]:


U.dot(Sig.dot(Vh))


# In[29]:


from scipy.stats import norm

mean, var, skew, kurt = norm.stats(moments='mvsk')
print(mean,var,skew,kurt)


# In[28]:


from scipy import stats
x = np.random.random(1000)
y = np.random.random(1000)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print({'slope':slope,'intercept':intercept})
print({'p_value':p_value,'r-squared':round(r_value**2,2)})


# In[30]:


import statsmodels.api as sm
import statsmodels.formula.api as smf
star98 = sm.datasets.star98.load_pandas().data
formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT +            PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',
              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',
              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()
endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))
del dta['NABOVE']
dta['SUCCESS'] = endog
mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
mod1.summary()


# In[34]:


from statsmodels.graphics.api import qqplot
import pandas as pd
print(sm.datasets.sunspots.NOTE)


# In[42]:


dta = sm.datasets.sunspots.load_pandas().data
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
del dta["YEAR"]
dta.plot(figsize=(12,8));


# In[47]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,20))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=30, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=30, ax=ax2)


# In[ ]:


arma_mod20 = sm.tsa.ARMA(dta, (2,0)).fit(disp=False)
print(arma_mod20.params)


# In[ ]:


arma_mod30 = sm.tsa.ARMA(dta, (4,0)).fit(disp=False)
resid = arma_mod30.resid
stats.normaltest(resid)
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True) 


# In[ ]:




