#!/usr/bin/env python
# coding: utf-8

# ![http://feng.li/](logo.png)Brought to you by [Dr. Feng Li](http://feng.li)
# 
# **{Other Formats Available: [PDF](http://feng.li/python) | [HTML](http://feng.li/python) | [SLIDES](http://feng.li/python)}**

# # Major Python modules for Data Wrangling
# 
# ## `NumPy`
# 
# `NumPy` is short for Numerical Python, is the foundational package for scientific computing in Python. It contains among other things:
# 
# - a powerful N-dimensional array object **（n维数组——矩阵）**
# - sophisticated (broadcasting) functions
# - tools for integrating *C/C++ and Fortran code* **（语言更加高效）**
# - useful linear algebra, Fourier transform, and random number capabilities
# 
# Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases. 
# 
# - [NumPy Reference](http://docs.scipy.org/doc/numpy/reference/)
# - [NumPy User Guide](http://docs.scipy.org/doc/numpy/user/index.html)

# ## `SciPy` 
# 
# `SciPy` is a *collection of packages*（比NumPy更多的包） addressing a number of different standard problem domains in scientific computing. Here is a sampling of the packages included:
# **（与NumPy结合使用）**
# 
# - `scipy.integrate` : numerical integration（数值积分） routines and differential equation solvers.
# - `scipy.linalg` : linear algebra（线性积分） routines and matrix decompositions extending beyond those provided in `numpy.linalg`.
# - `scipy.optimize` : function optimizers (minimizers) and root finding algorithms.（数值优化：牛顿迭代、梯度下降、信号处理、稀疏矩阵处理）
# - `scipy.signal` : signal processing tools.
# - `scipy.sparse` : sparse matrices and sparse linear system solvers.
# - `scipy.special` : wrapper around SPECFUN, a Fortran library implementing many common mathematical functions, such as the gamma function.
# - `scipy.stats` : standard continuous and discrete probability distributions (density functions, samplers, continuous distribution functions), various statistical tests, and more descriptive statistics.（概率、分布表达）
# - `scipy.weave` : tool for using inline C++ code to accelerate array computations.
# 
# - `scipy.cluster` :	Clustering algorithms
# - `scipy.fftpack` : Fast Fourier Transform routines
# - `scipy.integrate` : Integration and ordinary differential equation solvers
# - `scipy.interpolate` : Interpolation and smoothing splines
# - `scipy.ndimage` : N-dimensional image processing（n维图片使用）
# optimize 	Optimization and root-finding routines
# - `scipy.spatial` : Spatial data structures and algorithms
# 
# [SciPy Reference Guide](http://docs.scipy.org/doc/scipy/reference/)

# ## `pandas`
# 
# `pandas` provides rich data structures（数据结构） and functions designed to make working with structured data fast, easy, and expressive. It is, as you will see, one of the critical in-gredients enabling Python to be a powerful and productive data analysis environment. pandas combines the high performance array-computing features of `NumPy` with the flexible data manipulation capabilities of spreadsheets and relational databases (such as SQL). It provides sophisticated indexing functionality to make it easy to reshape, slice and dice, perform aggregations, and select subsets of data.
# （数据框——不同列是不同的数据类型——类似Excel）
# pandas consists of the following things
# 
# - A set of labeled array data structures, the primary of which are Series and DataFrame
# - Index objects enabling both simple axis indexing and multi-level / hierarchical axis indexing
# - An integrated group by engine for aggregating and transforming data sets
# - Date range generation (date_range) and custom date offsets enabling the implementation of customized frequencies
# - Input/Output tools: loading tabular data from flat files (CSV, delimited, Excel 2003), and saving and loading pandas objects from the fast and efficient PyTables/HDF5 format.
# - Memory-efficient “sparse” versions of the standard data structures for storing data that is mostly missing or mostly constant (some fixed value)
# - Moving window statistics (rolling mean, rolling standard deviation, etc.)
# - Static and moving window linear and panel regression
# 
# [pandas Documentation](http://pandas.pydata.org/pandas-docs/version/0.17.0/)
# 
# ***NumPy+SciPy+Pandas=数据分析基础工具***

# ## `statsmodels`
# 
# The `statsmodels` is a Python module（模型） that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. 
# （最简单的模型的探索）
# The `statsmodels` module covers the following topics
# 
# - Linear Regression Models
# - Plotting
# - Discrete Choice Models
# - Nonparametric Statistics
# - Generalized Linear Models
# - Robust Regression
# - Statistics
# - Time Series Analysis（时间序列）
# - State space models

# # Linear Algebra （线性代数）
# 
# Linear algebra can be done conveniently via `scipy.linalg`. When SciPy is built using the optimized **ATLAS LAPACK and BLAS libraries**, it has very fast linear algebra capabilities. If you dig deep enough, all of the raw lapack and blas libraries are available for your use for even more speed. In this section, some easier-to-use interfaces to these routines are described.
# 
# All of these linear algebra routines expect an object that can be converted into a 2-dimensional array. The output of these routines is also a two-dimensional array.

# ## Matrices and n-dimensional array （矩阵和多维数组）

# In[1]:


import numpy as np #建立缩写
from scipy import linalg
A = np.array([[1,2],[3,4]])#将列表套列表转化成矩阵
A


# In[2]:


linalg.inv(A) # inverse(转置) of a matrix；linalg是SciPy的指令


# In[3]:


b = np.array([[5,6]]) #2D array
b


# In[4]:


b.T #".T"可对某列向量、行向量做转置运算； "."的意思是原来的数据结构（b）支持一定的数据操作（T），此处"."就是调用这种数据操作


# In[5]:


A*b #not matrix multiplication!（非矩阵乘法，而是前行乘后列）


# In[6]:


A.dot(b.T) #matrix multiplication


# In[7]:


b = np.array([5,6]) #1D array
b


# In[8]:


b.T  #not matrix transpose!（一维矩阵不能转置——怎么转都一样）


# In[9]:


A.dot(b)  #does not matter for multiplication（不影响矩阵乘法）


# ## Solving linear system （求解线性方程组）

# In[10]:


import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
A


# In[11]:


b = np.array([[5],[6]])
b


# In[12]:


linalg.inv(A).dot(b) #slow（合并步骤）


# In[13]:


A.dot(linalg.inv(A).dot(b))-b #check（检验）


# In[14]:


np.linalg.solve(A,b) #fast solve(a,b)——ax=b


# In[15]:


A.dot(np.linalg.solve(A,b))-b #check


# ## Determinant （行列式）

# In[16]:


import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
linalg.det(A) #.det——行列式


# ## Least-squares problems and pseudo-inverses （最小二乘和广义逆）

# In[17]:


import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


# In[18]:


c1, c2 = 5.0, 2.0
i = np.r_[1:11]
xi = 0.1*i
yi = c1*np.exp(-xi) + c2*xi
zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi))


# In[19]:


A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
c, resid, rank, sigma = linalg.lstsq(A, zi)
#.lstsq——最小二乘法


# In[20]:


xi2 = np.r_[0.1:1.0:100j]
yi2 = c[0]*np.exp(-xi2) + c[1]*xi2


# In[22]:


plt.plot(xi,zi,'x',xi2,yi2)
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Data fitting with linalg.lstsq')
plt.show()


# ## Eigenvalues and eigenvectors （特征向量和特征值）

# In[23]:


import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
la,v = linalg.eig(A) #.eig特征向量特征值
l1,l2 = la
print(l1, l2)  #eigenvalues特征值

print(v[:,0])  #first eigenvector第一个特征向量

print(v[:,1])  #second eigenvector

print(np.sum(abs(v**2),axis=0)) #eigenvectors（特征向量） are unitary（单一）

v1 = np.array(v[:,0]).T
print(linalg.norm(A.dot(v1)-l1*v1)) #check the computation（计算）


# ## Singular Value Decomposition (SVD) （奇异值分解）

# In[24]:


import numpy as np
from scipy import linalg
A = np.array([[1,2,3],[4,5,6]])


# In[25]:


M,N = A.shape
U,s,Vh = linalg.svd(A) #.svd
Sig = linalg.diagsvd(s,M,N)


# In[30]:


U, Vh = U, Vh
U


# In[26]:


Sig


# In[27]:


Vh


# In[28]:


U.dot(Sig.dot(Vh)) #check computation


# ## QR decomposition （QR分解）
# 
# The command for QR decomposition is **`linalg.qr`**.

# ## LU decomposition （LU分解）
#     
# The SciPy command for this decomposition is `linalg.lu`.  If the intent for performing LU decomposition is for solving linear systems then the command `linalg.lu_factor` should be used followed by repeated applications of the command `linalg.lu_solve` to solve the system for each new right-hand-side.

# ## Cholesky decomposition （乔列斯基分解）
# 
# The command `linalg.cholesky` computes the cholesky factorization. For using Cholesky factorization to solve systems of equations there are also `linalg.cho_factor` and `linalg.cho_solve` routines that work similarly to their LU decomposition counterparts.

# # Statistical Distributions （统计分布函数）
# 
# A large number of probability distributions as well as a growing library of statistical functions are available in `scipy.stats`. See http://docs.scipy.org/doc/scipy/reference/stats.html for a complete list.
# 正态分布等

# Generate random numbers from normal distribution:

# In[29]:


from scipy.stats import norm #morm函数
r = norm.rvs(loc=0, scale=1, size=1000)
#rvs正态分布，loc均值，scale标准差，size生成多少个随机数——r即生成的随机数


# Calculate a few first moments:

# In[30]:


mean, var, skew, kurt = norm.stats(moments='mvsk')
#统计：四阶矩


# # Linear regression model （线性回归模型）
# 
# This example computes a least-squares regression for two sets of measurements.

# In[31]:


from scipy import stats
import numpy as np
x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)#.linregress：做简单线性模型；std_err：标准差
print({'slope':slope,'intercept':intercept})
print({'p_value':p_value,'r-squared':round(r_value**2,2)})


# ## Optimization （优化）
# 
# The `minimize` function provides a common interface to unconstrained and constrained minimization algorithms for multivariate scalar functions in `scipy.optimize`
# 牛顿迭代等

# In[32]:


import numpy as np
from scipy.optimize import minimize
#.optimize求最大值
## Define the function
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])

## Calling the minimize() function
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)


# # Generalized Linear Models（广义线性模型.glm）

# In[34]:


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


# In[2]:


mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
mod1.summary()
#.summary展示


# ## Autoregressive Moving Average (ARMA)
# 时间序列

# In[35]:


import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

print(sm.datasets.sunspots.NOTE)
#varible变量


# Let's first make the time series plot

# In[5]:


dta = sm.datasets.sunspots.load_pandas().data
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
del dta["YEAR"]
dta.plot(figsize=(12,8));
#绘制时间序列图
#.dates_from_range('1700', '2008')年限范围


# The ACF and PACF 各时间点之间值的联系

# In[37]:


fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)
#tsa.plot_acf打印出此时间序列的所有自回归表达式
#acf=autocorrelation(自相关); pacf=partial autocorrelation


# Fit an ARIMA model

# In[39]:


arma_mod20 = sm.tsa.ARMA(dta, (2,0)).fit(disp=False)
print(arma_mod20.params)#arma自回归移动平均


# In[40]:


arma_mod30 = sm.tsa.ARMA(dta, (3,0)).fit(disp=False)
resid = arma_mod30.resid
stats.normaltest(resid)
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
#resid残差项
#qqplot绘制qq图


# Let's then do some predictions

# In[41]:


predict_sunspots = arma_mod30.predict('1990', '2012', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['1950':].plot(ax=ax)
fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)


# # Lab
# 
# Use the data from cycle in the U.S. unemployment rate to model the rrends and cycles in unemployment.
# 
# ```python
# from pandas_datareader.data import DataReader
# endog = DataReader('UNRATE', 'fred', start='1954-01-01')
# ```
