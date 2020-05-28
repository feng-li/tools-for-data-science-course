from pandas_datareader.data import DataReader

Warning (from warnings module):
  File "C:\Users\Dell\AppData\Local\Programs\Python\Python38\lib\site-packages\>
    from pandas.util.testing import assert_frame_equal
FutureWarning: pandas.util.testing is deprecated. Use the functions in the publ>
>>> endog = DataReader('UNRATE', 'fred', start='1954-01-01')
>>> from pandas_datareader.data import DataReader
>>> import numpy as np
>>> from scipy import stats
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import statsmodels.api as sm
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import statsmodels.api as sm
ModuleNotFoundError: No module named 'statsmodels'
>>> import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

>>>
>>> print(sm.datasets.sunspots.NOTE)
::

    Number of Observations - 309 (Annual 1700 - 2008)
    Number of Variables - 1
    Variable name definitions::

        SUNACTIVITY - Number of sunspots for each year

    The data file contains a 'YEAR' variable that is not returned by load.

>>> print(sm.UNRATE.fred.NOTE)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(sm.UNRATE.fred.NOTE)
AttributeError: module 'statsmodels.api' has no attribute 'UNRATE'
>>> from pandas_datareader.data import DataReader
>>> endog = DataReader('UNRATE', 'fred', start='1954-01-01')
>>> print(sm.datasets.fred.NOTE)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(sm.datasets.fred.NOTE)
AttributeError: module 'statsmodels.datasets' has no attribute 'fred'
>>> print(sm.datasets.UNRATE.NOTE)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(sm.datasets.UNRATE.NOTE)
AttributeError: module 'statsmodels.datasets' has no attribute 'UNRATE'
>>> print(sm.datasets.enddog.NOTE)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(sm.datasets.enddog.NOTE)
AttributeError: module 'statsmodels.datasets' has no attribute 'enddog'
>>> dta = sm.datasets.sunspots.load_pandas().data
>>> print(sm.enddog.fred.NOTE)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(sm.enddog.fred.NOTE)
AttributeError: module 'statsmodels.api' has no attribute 'enddog'
>>> import logging
>>> import requests
>>> import sys
>>> import urllib
>>> from bs4 import BeautifulSoup
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'
>>> pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple
SyntaxError: invalid syntax
>>> bs4 import BeautifulSoup
SyntaxError: invalid syntax
>>> from bs4 import BeautifulSoup
>>> from collections import OrderedDict
>>> from urllib.parse import urlencode
>>> def needyvocab (word):
         newsData = OrderedDict()
         href = https://fanyi.baidu.com/?aldtype=16047#en/zh/'%s' % (word)
 def needyvocab (word):
         newsData = OrderedDict()
         href = 'https://fanyi.baidu.com/?aldtype=16047#en/zh/%s' % (word)
         html = requests.get(href)
         soup = BeautifulSoup(html.content, 'html.parser')
         nameList = bs.findAll('ol', {'class':'dictionary-tags'})
         for name in nameList:
                 print(name.get_text())


