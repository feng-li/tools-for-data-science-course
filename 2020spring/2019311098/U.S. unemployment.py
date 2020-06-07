Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader.data import DataReader

Warning (from warnings module):
  File "C:\Users\think\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas_datareader\compat\__init__.py", line 7
    from pandas.util.testing import assert_frame_equal
FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
>>> endog=DataReader('UNRATE','fred',start='1954-01-01')
>>> endog
            UNRATE
DATE              
1954-01-01     4.9
1954-02-01     5.2
1954-03-01     5.7
1954-04-01     5.9
1954-05-01     5.9
...            ...
2020-01-01     3.6
2020-02-01     3.5
2020-03-01     4.4
2020-04-01    14.7
2020-05-01    13.3

[797 rows x 1 columns]
>>> plt.plot(endog)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    plt.plot(endog)
NameError: name 'plt' is not defined
>>> import matplotlib.pyplot as plt
>>> plt.plot(endog)
[<matplotlib.lines.Line2D object at 0x00000195C0A33D60>]
>>> plt.show()
>>> 