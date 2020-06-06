Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> from scipy import linalg
>>> A=np.array([[1,2],[3,4]])
>>> A
array([[1, 2],
       [3, 4]])
>>> A.T
array([[1, 3],
       [2, 4]])
>>> linalg.inv(A)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
>>> b=np.array([[5,6]])
>>> b
array([[5, 6]])
>>> b.T
array([[5],
       [6]])
>>> b.t
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.t
AttributeError: 'numpy.ndarray' object has no attribute 't'
>>> A*b
array([[ 5, 12],
       [15, 24]])
>>> A.dot(b.T)
array([[17],
       [39]])
>>> b=np.array([[5],[6]])
>>> b
array([[5],
       [6]])
>>> b.T
array([[5, 6]])
>>> linalg.inv(A).dot(b)
array([[-4. ],
       [ 4.5]])
>>> A.dot(linalg,inv(A).dot(b))-b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    A.dot(linalg,inv(A).dot(b))-b
NameError: name 'inv' is not defined
>>> A.dot(linalg.inv(A).dot(b))-b
array([[0.],
       [0.]])
>>> np.linalg.solve(A,b)
array([[-4. ],
       [ 4.5]])
>>> A.dot(np.linalg.solve(A,b))-b
array([[0.],
       [0.]])
>>> linalg.det(A)
-2.0
>>> linalg.det(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    linalg.det(b)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\scipy\linalg\basic.py", line 1036, in det
    raise ValueError('expected square matrix')
ValueError: expected square matrix
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
>>> c1,c2=5.0,2.0
>>> i=np.r_[1:11]
>>> xi=0.1*i
>>> yi=c1*np.exp(-xi)+c2*xi
>>> zi=yi+0.05*np.max(yi)*np.random.randn(len(yi))
>>> A=np.c_[np.exp(-xi)[:,np.newaxis],xi[:,np.newaxis]]
>>> c,resid,rank,sigma=linalg.lstsq(A,zi)
>>> xi2=np.r_[0.1:1.0:100j]
>>> yi2=c[0]*np.exp(-xi2)+c[1]*xi2
>>> plt.plot(xi,zi,'x',xi2yi2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    plt.plot(xi,zi,'x',xi2yi2)
NameError: name 'xi2yi2' is not defined
>>> plt.plot(xi,zi,'x',xi2,yi2)
[<matplotlib.lines.Line2D object at 0x000001BDFA1D9AF0>, <matplotlib.lines.Line2D object at 0x000001BDFA1D9BE0>]
>>> plt.axis([0,1.1,3.0,5.5])
(0.0, 1.1, 3.0, 5.5)
>>> plt.xlabel('$x_i$')
Text(0.5, 0, '$x_i$')
>>> plt.title('Data fitting with linalg.lstsq')
Text(0.5, 1.0, 'Data fitting with linalg.lstsq')
>>> plt.show()
>>> A=np.array([[1,2],[3,4]])
>>> la,v=linalg.eig(A)
>>> l1,l2=la
>>> print(l1,l2)
(-0.3722813232690143+0j) (5.372281323269014+0j)
>>> print(v[:,0])
[-0.82456484  0.56576746]
>>> print(v[:,1])
[-0.41597356 -0.90937671]
>>> print(np.sum(abs(v**2),axis=0))
[1. 1.]
>>> v1=np.array(v[:,0]).T
>>> print(linalg.norm(A.dot(v1)-l1*v1))
5.551115123125783e-17
>>> A=np.array(9[[1,2,3],[4,5,6]])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    A=np.array(9[[1,2,3],[4,5,6]])
TypeError: 'int' object is not subscriptable
>>> A=np.array([[1,2,3],[4,5,6]])
>>> M,N=A.shape
>>> U,s,Vh=linalg.svd(A)
>>> Sig=linalg.diagsvd(s,M,N)
>>> U,Vh=U,Vh
>>> U
array([[-0.3863177 , -0.92236578],
       [-0.92236578,  0.3863177 ]])
>>> Sig
array([[9.508032  , 0.        , 0.        ],
       [0.        , 0.77286964, 0.        ]])
>>> Vh
array([[-0.42866713, -0.56630692, -0.7039467 ],
       [ 0.80596391,  0.11238241, -0.58119908],
       [ 0.40824829, -0.81649658,  0.40824829]])
>>> U.dot(Sig.dot(Vh))
array([[1., 2., 3.],
       [4., 5., 6.]])
>>> from scipy import stats
import n
>>> from scipy import stats
>>> import numpy as np
>>> x=np.random.random(10)
>>> y=np.random.random(10)
>>> slope,intercept,r_value,p_value,std_err=stats.linregress(x,y)
>>> print({'slope
       
SyntaxError: EOL while scanning string literal
>>> print({'slope':slope,'intercept':intercept})
{'slope': 0.2621656255076302, 'intercept': 0.21381219542868496}
>>> print({'p_value':p_value,'r-squared':round(r_value**2,2)})
{'p_value': 0.5078940430434242, 'r-squared': 0.06}
>>> x=np.random.random(10）
		   
SyntaxError: invalid character in identifier
>>> x=np.random.random(10)
>>> y=np.random.random(10)
>>> slope,intercept,r_value,p_value,std_err=stats.linregress(x,y)
>>> print({'slope':slope,'intercept':interceprt})
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print({'slope':slope,'intercept':interceprt})
NameError: name 'interceprt' is not defined
>>> print({'slope':slope,'intercept':intercept})
{'slope': -0.24530867500522882, 'intercept': 0.6353820088362432}
>>>  x=np.random.random(10)
 
SyntaxError: unexpected indent
>>> x=np.random.random(10)
>>> y=np.random.random(10)
>>> slope,intercept,r_value,p_value,std_err=stats.linregress(x,y)
>>> print({'slope':slope,'intercept':intercept})
{'slope': 0.028585081218506968, 'intercept': 0.5236210332772653}
>>> print({'slope':slope,'intercept':intercept})
{'slope': 0.028585081218506968, 'intercept': 0.5236210332772653}
>>> print({'slope':slope,'intercept':intercept})
{'slope': 0.028585081218506968, 'intercept': 0.5236210332772653}
>>> print({'p_value':p_value,'r-squared':round(r_value**2,2)})
{'p_value': 0.925324244572681, 'r-squared': 0.0}
>>> print({'p_value':p_value,'r-squared':round(r_value**2,2)})
{'p_value': 0.925324244572681, 'r-squared': 0.0}
>>> import numpy as np
>>> from scipy.optimize import minimize
>>> def rosen(x):
	"""The Rosenbrock function"""
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
x0=np.array([1.3,0.7,0.8,1.9,1.2])
SyntaxError: invalid syntax
>>> def rosen(x):
	"""The Rosenbrock function"""
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
x0=np.array([1.3,0.7,0.8,1.9,1.2])
SyntaxError: invalid syntax
>>> def rosen(x):
	"""The Rosenbrock function"""
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
x0=np.array([1.3,0.7,0.8,1.9,1.2])
SyntaxError: invalid syntax
>>> res=minimize(rosen,x0,method='nelder-mead',
	     options={'xtol':le-8,'disp':True})
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    res=minimize(rosen,x0,method='nelder-mead',
NameError: name 'rosen' is not defined
>>> print(res.x)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(res.x)
NameError: name 'res' is not defined
>>> import numpy as np
from scipy.optimize import minimize
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
SyntaxError: multiple statements found while compiling a single statement
>>> import numpy as np
from scipy.optimize import minimize
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
SyntaxError: multiple statements found while compiling a single statement
>>> import numpy as np
>>> from scipy.optimize import minimize
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
SyntaxError: multiple statements found while compiling a single statement
>>> from scipy.optimize import minimize
>>> def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
SyntaxError: invalid syntax
>>> def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
SyntaxError: invalid syntax
>>> import numpy as np
>>> from scipy import stats
>>> import pandas as pd
import matplo
>>> tlib.pyplot as plt
SyntaxError: invalid syntax
>>> import matpltlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    import matpltlib.pyplot as plt
ModuleNotFoundError: No module named 'matpltlib'
>>> import matplotlib.pyplot as plt
>>> import statsmodels.api as sm
from statsmodels.graphics.api impor
>>> from statsmodels.graphics.api import qqplot
>>> print(sm.datasets.sunspots.NOTE)
::

    Number of Observations - 309 (Annual 1700 - 2008)
    Number of Variables - 1
    Variable name definitions::

        SUNACTIVITY - Number of sunspots for each year

    The data file contains a 'YEAR' variable that is not returned by load.

>>> import statsmodels.api as sm
>>> import statsmodels.formula.api as smf
>>> star98=sm.datasets.star98.load_pandas().data
>>> formula='SUCCESS~LOWINC+PERASIAN+PERBLACK+PERHISP+PCTCHRT+\PCTYRRND+PERMINTE*AVYRSEXP*AVSALK+PERSPENK*PTRATIO*PCTAF'
>>> dta=star98[['NABOVE','NBELOW','LOWINC','PERASIAN','PERBLACK','PERHISP','PCTCHRT','PCTYRRND','PERMINTE','AVYRSEXP','AVSALK','PERSPENK','PTRATIO','PCTAF']].copy()
>>> endog=dta['NABOVE']/(dta['NABOVE']+dta.pop('NBELOW'))
>>> del dta['NABOVE']
>>> dta['SUCCESS']=endog
>>> mod1=smf.glm(formula=formula,data=dta,family=sm.families.Binomial()).fit()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    mod1=smf.glm(formula=formula,data=dta,family=sm.families.Binomial()).fit()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\base\model.py", line 168, in from_formula
    tmp = handle_formula_data(data, None, formula, depth=eval_env,
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\formula\formulatools.py", line 64, in handle_formula_data
    result = dmatrices(formula, Y, depth, return_type='dataframe',
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\highlevel.py", line 309, in dmatrices
    (lhs, rhs) = _do_highlevel_design(formula_like, data, eval_env,
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\highlevel.py", line 164, in _do_highlevel_design
    design_infos = _try_incr_builders(formula_like, data_iter_maker, eval_env,
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\highlevel.py", line 62, in _try_incr_builders
    formula_like = ModelDesc.from_formula(formula_like)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\desc.py", line 164, in from_formula
    tree = parse_formula(tree_or_string)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\parse_formula.py", line 146, in parse_formula
    tree = infix_parse(_tokenize_formula(code, operator_strings),
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\infix_parser.py", line 210, in infix_parse
    for token in token_source:
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\parse_formula.py", line 89, in _tokenize_formula
    for pytype, token_string, origin in it:
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\util.py", line 349, in next
    return six.advance_iterator(self._it)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\patsy\tokens.py", line 40, in python_tokenize
    raise PatsyError("error tokenizing input "
patsy.PatsyError: error tokenizing input (maybe an unclosed string?)
    SUCCESS~LOWINC+PERASIAN+PERBLACK+PERHISP+PCTCHRT+\PCTYRRND+PERMINTE*AVYRSEXP*AVSALK+PERSPENK*PTRATIO*PCTAF
                                                     ^
>>> mod1.summary()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    mod1.summary()
NameError: name 'mod1' is not defined
>>> dta=sm.datasets.sunspots.load_pandas().data
>>> dta.index=pd.Index(sm.tsa.datetools.dates_from_range('1700','2008'))
>>> del dta["YEAR"]
>>> dta.plot(figsize=(12,8)):
	
SyntaxError: invalid syntax
>>> dta.plot(figsize=(12,8));
<matplotlib.axes._subplots.AxesSubplot object at 0x000001BD856ACDC0>

>>> dta=sm.datasets.sunspots.load_pandas().data
>>> dta.index=pd.Index(sm.tsa.datetools.dates_from_range('1700','2008'))
>>> del dta["YEAR"]
>>> dta.plot(figsize=(12,8));
<matplotlib.axes._subplots.AxesSubplot object at 0x000001BD865B9F10>
>>> ss.show()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    ss.show()
NameError: name 'ss' is not defined
>>> dta.show()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    dta.show()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'show'
>>> plot.show()
Traceback (most recent call last):

  File "<pyshell#131>", line 1, in <module>
    plot.show()
NameError: name 'plot' is not defined
>>> pd.show()
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    pd.show()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\__init__.py", line 263, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'show'
>>> import pylab
>>> pylab.show()
>>> dta.plot(figsize=(12,8));
<matplotlib.axes._subplots.AxesSubplot object at 0x000001BD865D1640>

>>> fig=plt.figure(figsize=(12,8))
>>> axl=fig.add_subplot(211)
>>> fig=sm.graphics.tsa.plot_acf(dta.values.squeeze(0,lags=40,ax=axlaxl=fig.add_subplot(211)
						
SyntaxError: invalid syntax
>>> fig=plt.figure(figsize=(12,8))
>>> ax1=fig.add_subplot(211)
>>> fig=sm.graphics.tsa.plot_acf(dta.values.squeeze(),lags=40,ax=ax1)
>>> ax2=fig.add_subplot(212)
>>> fig=sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)
>>> 
>>> import pylab
>>> pylab.show()
>>> arma_mod20=sm.tsa.ARMA(dta,(2,0)).fit(disp=False)

Warning (from warnings module):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\tsa\base\tsa_model.py", line 159
    warnings.warn('No frequency information was'
ValueWarning: No frequency information was provided, so inferred frequency A-DEC will be used.
>>> print(arma_mod20.params)
const                49.659748
ar.L1.SUNACTIVITY     1.390656
ar.L2.SUNACTIVITY    -0.688571
dtype: float64
>>> arma_mod30=sm.tsa.ARMA(dta,(3,0)).fit(disp=False)

Warning (from warnings module):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\tsa\base\tsa_model.py", line 159
    warnings.warn('No frequency information was'
ValueWarning: No frequency information was provided, so inferred frequency A-DEC will be used.
>>> resid=arma_mod30.resid
>>> stats.normaltest(resid)
NormaltestResult(statistic=49.84501940098131, pvalue=1.5006919810670537e-11)
>>> fig=plt.figure(figsize=(12,8))
>>> ax=fig.add_subplot(111)
>>> fig=qqplot(resid,line='q',ax=ax,fit=True)
>>> 
>>> import pylab
>>> pylab.show()
>>> predict_sunspots=arma_mod30.predict('1990','2012',dynamic=True)
>>> print(predict_sunspots)
1990-12-31    167.047416
1991-12-31    140.993000
1992-12-31     94.859113
1993-12-31     46.860902
1994-12-31     11.242589
1995-12-31     -4.721287
1996-12-31     -1.166905
1997-12-31     16.185697
1998-12-31     39.021886
1999-12-31     59.449873
2000-12-31     72.170141
2001-12-31     75.376781
2002-12-31     70.436455
2003-12-31     60.731583
2004-12-31     50.201794
2005-12-31     42.076025
2006-12-31     38.114287
2007-12-31     38.454644
2008-12-31     41.963817
2009-12-31     46.869287
2010-12-31     51.423260
2011-12-31     54.399716
2012-12-31     55.321687
Freq: A-DEC, dtype: float64
>>> fig,ax=plt.subplots(figsize=(12,8))
>>> ax=dta.ix['1950':].plot(ax=ax)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    ax=dta.ix['1950':].plot(ax=ax)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'ix'
>>> fig=arma_arma_mod30.plot_predict('1990','2012',dynamic=True,ax=ax,plot_insample=False)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    fig=arma_arma_mod30.plot_predict('1990','2012',dynamic=True,ax=ax,plot_insample=False)
NameError: name 'arma_arma_mod30' is not defined
>>> pylab.show()
>>> pylab.show()
>>> 
>>> import pylab
>>> pylab.show()
>>> fig.show()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    fig.show()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 443, in show
    manager.show()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 476, in show
    self.canvas.manager.window.attributes('-topmost', 1)
AttributeError: 'NoneType' object has no attribute 'attributes'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 10, in draw
    _backend_tk.blit(self._tkphoto, self.renderer._renderer, (0, 1, 2, 3))
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 76, in blit
    photoimage.blank()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 4065, in blank
    self.tk.call(self.name, 'blank')
_tkinter.TclError: invalid command name "pyimage86"
1
1
>>> import statsmodels.api as sm
import statsmodels.formula.api as smf
star98 = sm.datasets.star98.load_pandas().data
formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',
              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',
              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()
endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))
del dta['NABOVE']
dta['SUCCESS'] = endog
SyntaxError: multiple statements found while compiling a single statement
>>> import statsmodels.api as sm
import statsmodels.formula.api as smf
star98 = sm.datasets.star98.load_pandas().data
formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',
              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',
              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()
endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))
del dta['NABOVE']
dta['SUCCESS'] = endog
mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
mod1.summary()
SyntaxError: multiple statements found while compiling a single statement
>>> import statsmodels.api as sm
>>> import statsmodels.formula.api as smf
>>> star98 = sm.datasets.star98.load_pandas().data
>>> formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
>>> dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',
              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',
              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()
>>> endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))
>>> del dta['NABOVE']
>>> dta['SUCCESS'] = endog
>>> mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
>>> mod1.summary()
<class 'statsmodels.iolib.summary.Summary'>
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:                SUCCESS   No. Observations:                  303
Model:                            GLM   Df Residuals:                      282
Model Family:                Binomial   Df Model:                           20
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -127.33
Date:                Sat, 06 Jun 2020   Deviance:                       8.5477
Time:                        16:16:08   Pearson chi2:                     8.48
No. Iterations:                     4                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                    0.4037     25.036      0.016      0.987     -48.665      49.472
LOWINC                      -0.0204      0.010     -1.982      0.048      -0.041      -0.000
PERASIAN                     0.0159      0.017      0.910      0.363      -0.018       0.050
PERBLACK                    -0.0198      0.020     -1.004      0.316      -0.058       0.019
PERHISP                     -0.0096      0.010     -0.951      0.341      -0.029       0.010
PCTCHRT                     -0.0022      0.022     -0.103      0.918      -0.045       0.040
PCTYRRND                    -0.0022      0.006     -0.348      0.728      -0.014       0.010
PERMINTE                     0.1068      0.787      0.136      0.892      -1.436       1.650
AVYRSEXP                    -0.0411      1.176     -0.035      0.972      -2.346       2.264
PERMINTE:AVYRSEXP           -0.0031      0.054     -0.057      0.954      -0.108       0.102
AVSALK                       0.0131      0.295      0.044      0.965      -0.566       0.592
PERMINTE:AVSALK             -0.0019      0.013     -0.145      0.885      -0.028       0.024
AVYRSEXP:AVSALK              0.0008      0.020      0.038      0.970      -0.039       0.041
PERMINTE:AVYRSEXP:AVSALK  5.978e-05      0.001      0.068      0.946      -0.002       0.002
PERSPENK                    -0.3097      4.233     -0.073      0.942      -8.606       7.987
PTRATIO                      0.0096      0.919      0.010      0.992      -1.792       1.811
PERSPENK:PTRATIO             0.0066      0.206      0.032      0.974      -0.397       0.410
PCTAF                       -0.0143      0.474     -0.030      0.976      -0.944       0.916
PERSPENK:PCTAF               0.0105      0.098      0.107      0.915      -0.182       0.203
PTRATIO:PCTAF               -0.0001      0.022     -0.005      0.996      -0.044       0.044
PERSPENK:PTRATIO:PCTAF      -0.0002      0.005     -0.051      0.959      -0.010       0.009
============================================================================================
"""
>>> predict_sunspots=arma_mod30.predict('1990','2012',dynamic=True)
>>> print(predict_sunspots)
1990-12-31    167.047416
1991-12-31    140.993000
1992-12-31     94.859113
1993-12-31     46.860902
1994-12-31     11.242589
1995-12-31     -4.721287
1996-12-31     -1.166905
1997-12-31     16.185697
1998-12-31     39.021886
1999-12-31     59.449873
2000-12-31     72.170141
2001-12-31     75.376781
2002-12-31     70.436455
2003-12-31     60.731583
2004-12-31     50.201794
2005-12-31     42.076025
2006-12-31     38.114287
2007-12-31     38.454644
2008-12-31     41.963817
2009-12-31     46.869287
2010-12-31     51.423260
2011-12-31     54.399716
2012-12-31     55.321687
Freq: A-DEC, dtype: float64
>>> fig,ax=plt.subplots(figsize=(12,8))
a
>>> ax=dta.ix['1950':].plot(ax=ax)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    ax=dta.ix['1950':].plot(ax=ax)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'ix'
>>> fig=arma_mod30.plot_predict('1990','2012',dynamic=True,ax=ax,plot_insample=False)
>>> 
>>> import pylab
>>> pylab.show()
>>> ax = dta.ix['1950':].plot(ax=ax)
fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
SyntaxError: multiple statements found while compiling a single statement
>>> ax = dta.ix['1950':].plot(ax=ax)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    ax = dta.ix['1950':].plot(ax=ax)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'ix'
>>> fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
>>> pylab.show()
>>> pylab.show()
>>> ax = dta.x['1950':].plot(ax=ax)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    ax = dta.x['1950':].plot(ax=ax)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'x'
>>> ax = dta.ax['1950':].plot(ax=ax)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    ax = dta.ax['1950':].plot(ax=ax)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'ax'
>>> predict_sunspots = arma_mod30.predict('1990', '2012', dynamic=True)
>>> print(predict_sunspots)
1990-12-31    167.047416
1991-12-31    140.993000
1992-12-31     94.859113
1993-12-31     46.860902
1994-12-31     11.242589
1995-12-31     -4.721287
1996-12-31     -1.166905
1997-12-31     16.185697
1998-12-31     39.021886
1999-12-31     59.449873
2000-12-31     72.170141
2001-12-31     75.376781
2002-12-31     70.436455
2003-12-31     60.731583
2004-12-31     50.201794
2005-12-31     42.076025
2006-12-31     38.114287
2007-12-31     38.454644
2008-12-31     41.963817
2009-12-31     46.869287
2010-12-31     51.423260
2011-12-31     54.399716
2012-12-31     55.321687
Freq: A-DEC, dtype: float64
>>> fig, ax = plt.subplots(figsize=(12, 8))
>>> ax = dta.loc['1950':].plot(ax=ax)
>>> fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\tsa\arima_model.py", line 1824, in plot_predict
    ax = forecast.plot(ax=ax, label='forecast')
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_core.py", line 847, in __call__
    return plot_backend.plot(data, kind=kind, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\__init__.py", line 61, in plot
    plot_obj.generate()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 269, in generate
    self._post_plot_logic_common(ax, self.data)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 437, in _post_plot_logic_common
    self._apply_axis_properties(ax.xaxis, rot=self.rot, fontsize=self.fontsize)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 520, in _apply_axis_properties
    labels = axis.get_majorticklabels() + axis.get_minorticklabels()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1276, in get_majorticklabels
    ticks = self.get_major_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
>>> plt.show()
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 259, in resize
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 259, in resize
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 196, in process
    func(*args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backend_bases.py", line 1681, in pick
    self.figure.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 505, in pick
    for a in self.get_children():
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 839, in get_children
    *self.get_major_ticks(), *self.get_minor_ticks()]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 196, in process
    func(*args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backend_bases.py", line 1681, in pick
    self.figure.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 505, in pick
    for a in self.get_children():
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 839, in get_children
    *self.get_major_ticks(), *self.get_minor_ticks()]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 196, in process
    func(*args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backend_bases.py", line 1681, in pick
    self.figure.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 505, in pick
    for a in self.get_children():
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 839, in get_children
    *self.get_major_ticks(), *self.get_minor_ticks()]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 196, in process
    func(*args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backend_bases.py", line 1681, in pick
    self.figure.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 505, in pick
    for a in self.get_children():
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 839, in get_children
    *self.get_major_ticks(), *self.get_minor_ticks()]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 196, in process
    func(*args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backend_bases.py", line 1681, in pick
    self.figure.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 516, in pick
    a.pick(mouseevent)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 505, in pick
    for a in self.get_children():
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 839, in get_children
    *self.get_major_ticks(), *self.get_minor_ticks()]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 259, in resize
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 259, in resize
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
>>> plt.show()
>>> predict_sunspots = arma_mod30.predict('1990', '2012', dynamic=True)
>>> print(predict_sunspots)
1990-12-31    167.047416
1991-12-31    140.993000
1992-12-31     94.859113
1993-12-31     46.860902
1994-12-31     11.242589
1995-12-31     -4.721287
1996-12-31     -1.166905
1997-12-31     16.185697
1998-12-31     39.021886
1999-12-31     59.449873
2000-12-31     72.170141
2001-12-31     75.376781
2002-12-31     70.436455
2003-12-31     60.731583
2004-12-31     50.201794
2005-12-31     42.076025
2006-12-31     38.114287
2007-12-31     38.454644
2008-12-31     41.963817
2009-12-31     46.869287
2010-12-31     51.423260
2011-12-31     54.399716
2012-12-31     55.321687
Freq: A-DEC, dtype: float64
>>> fig, ax = plt.subplots(figsize=(12, 6))
>>> ax = dta.loc['1950':].plot(ax=ax)
>>> fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insampl)
SyntaxError: positional argument follows keyword argument
>>> fig, ax = plt.subplots(figsize=(12, 8))
>>> ax = dta.loc['1950':].plot(ax=ax)
>>> fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\statsmodels\tsa\arima_model.py", line 1824, in plot_predict
    ax = forecast.plot(ax=ax, label='forecast')
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_core.py", line 847, in __call__
    return plot_backend.plot(data, kind=kind, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\__init__.py", line 61, in plot
    plot_obj.generate()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 269, in generate
    self._post_plot_logic_common(ax, self.data)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 437, in _post_plot_logic_common
    self._apply_axis_properties(ax.xaxis, rot=self.rot, fontsize=self.fontsize)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\plotting\_matplotlib\core.py", line 520, in _apply_axis_properties
    labels = axis.get_majorticklabels() + axis.get_minorticklabels()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1276, in get_majorticklabels
    ticks = self.get_major_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1431, in get_major_ticks
    numticks = len(self.get_majorticklocs())
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
>>> plt.show()
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 804, in callit
    func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 270, in idle_draw
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\_backend_tk.py", line 259, in resize
    self.draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 9, in draw
    super(FigureCanvasTkAgg, self).draw()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\backends\backend_agg.py", line 393, in draw
    self.figure.draw(self.renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\figure.py", line 1735, in draw
    mimage._draw_list_compositing_images(
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 2630, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\image.py", line 137, in _draw_list_compositing_images
    a.draw(renderer)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1227, in draw
    ticks_to_draw = self._update_ticks()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1103, in _update_ticks
    major_locs = self.get_majorticklocs()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axis.py", line 1348, in get_majorticklocs
    return self.major.locator()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1338, in __call__
    self.refresh()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1364, in refresh
    dmin, dmax = self.viewlim_to_dt()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\dates.py", line 1094, in viewlim_to_dt
    raise ValueError('view limit minimum {} is less than 1 and '
ValueError: view limit minimum -36537.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
>>> from pandas_datareader.data import DataReader
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    from pandas_datareader.data import DataReader
ModuleNotFoundError: No module named 'pandas_datareader'
>>> from pandas_datareader.data import DataReader

Warning (from warnings module):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas_datareader\compat\__init__.py", line 7
    from pandas.util.testing import assert_frame_equal
FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
>>> from pandas_datareader.data import DataReader
>>> endog=DataReader('UNRATE','fred',start='1954-01-01')
>>> import pylab
>>> pylab.show()
>>> 
>>> 
>>> from pandas_datareader.data import DataReader
>>> endog=DataReader('UNRATE','fred',start='1954-01-01')
>>> del dta["YEAR"]
Traceback (most recent call last):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'YEAR'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    del dta["YEAR"]
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 3759, in __delitem__
    self._data.delete(key)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\internals\managers.py", line 1002, in delete
    indexer = self.items.get_loc(item)
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'YEAR'
>>> dta.plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x000001BD861EF5B0>
>>> show()
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    show()
NameError: name 'show' is not defined
>>> plt.show()
>>> dta.show()
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    dta.show()
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'show'
>>> plot.()
SyntaxError: invalid syntax
>>> plot()
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    plot()
NameError: name 'plot' is not defined
>>> import numpy as ny
>>> import pandas as pd
>>> from pandas_datareader.data import DataReader
>>> endog=DataReader('UNRATE','fred',start='1954-01-01')
>>> import matplotlib.pylab as plt
>>> from datetime import datetiome
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    from datetime import datetiome
ImportError: cannot import name 'datetiome' from 'datetime' (C:\Users\think\AppData\Local\Programs\Python\Python38\lib\datetime.py)
>>> from datetime import datetime
>>> ts=endog('x')
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    ts=endog('x')
TypeError: 'DataFrame' object is not callable
>>> 