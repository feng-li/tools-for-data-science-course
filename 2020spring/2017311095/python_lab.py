Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5*2
10
>>> 5**3
125
>>> a="Steven"
>>> a
'Steven'
>>> type(a)
<class 'str'>
>>> len(a)
6
>>> a(1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a(1)
TypeError: 'str' object is not callable
>>> a[1]
't'
>>> a[-2]
'e'
>>> a[3:5]
've'
>>> a[3:]
'ven'
>>> b="Sun"+""*3+"Steven"
>>> b
'SunSteven'
>>> b="Sun"+" "*3+"Steven"
>>> b
'Sun   Steven'
>>> print("Steven")
Steven
>>> print("Hello \n World")
Hello 
 World
>>> a=[1,2,3]
>>> type(a)
<class 'list'>
>>> a{1}
SyntaxError: invalid syntax
>>> a[1]
2
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.insert(2,'a')
>>> a
[1, 2, 'a', 3, 4]
>>> a.remove('a')
>>> a
[1, 2, 3, 4]
>>> b=[4,5,6]
>>> b
[4, 5, 6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 4, 5, 6]
>>> a.remove(4)
>>> a
[1, 2, 3, 4, 5, 6]
>>> del a[5]
>>> a
[1, 2, 3, 4, 5]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> a.pop(2)
3
>>> a=[1,3,2,3]
>>> a
[1, 3, 2, 3]
>>> a.sort()
>>> a
[1, 2, 3, 3]
>>> a.reverse()
>>> a
[3, 3, 2, 1]
>>> a.count(2)
1
>>> a.index(2)
2
>>> c1=a
>>> c2=a[:]
>>> c3=a.copy()
>>> c1,c2,c3
([3, 3, 2, 1], [3, 3, 2, 1], [3, 3, 2, 1])
>>> a.append(4)
>>> a
[3, 3, 2, 1, 4]
>>> {c1,c2,c3}
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    {c1,c2,c3}
TypeError: unhashable type: 'list'
>>> [c1,c2,c3]
[[3, 3, 2, 1, 4], [3, 3, 2, 1], [3, 3, 2, 1]]
>>> matrix=[[1,2,3,4],[5,6,7,8,9],[10,11,12]]
>>> type(matrix)
<class 'list'>
>>> matrix[1][2]
7
>>> list(range(1,6,2))
[1, 3, 5]
>>> [x*x for x in range(1,12)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
>>> [m]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    [m]
NameError: name 'm' is not defined
>>> 

>>> 

>>> 


>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
>>> a={1,2,2,'a',}
>>> 
>>> a
{1, 2, 'a'}
>>> a={1,2,'a','bc'}
>>> type(a)
<class 'set'>
>>> 'a' in a
True
>>> b={a,3,'b','c'}
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b={a,3,'b','c'}
bTypeError: unhashable type: 'set'
>>> 
>>> b={1,3,'b','c'}
>>> b
{1, 3, 'c', 'b'}
>>> a|b
{1, 2, 3, 'b', 'c', 'bc', 'a'}
>>> a&b
{1}
>>> a-b
{2, 'bc', 'a'}
>>> a^b
{2, 3, 'b', 'c', 'bc', 'a'}
>>> a=set('122abb')
>>> a
{'1', 'b', '2', 'a'}
>>> a=1,'a','b'
>>> a
(1, 'a', 'b')
>>> b=[1,'c']
>>> c=a,b
>>> c
((1, 'a', 'b'), [1, 'c'])
>>> c[0]
(1, 'a', 'b')
>>> c[1][1]=2
>>> c
((1, 'a', 'b'), [1, 2])
>>> tel={'mike':3759,'mary':1462,'ning':6959}
>>> print(tel)
{'mike': 3759, 'mary': 1462, 'ning': 6959}
>>> print(tel.keys())
dict_keys(['mike', 'mary', 'ning'])
>>> print(tel.values())
dict_values([3759, 1462, 6959])
>>> list(tel.keys)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list(tel.keys)
TypeError: 'builtin_function_or_method' object is not iterable
>>> list(tel.keys())
['mike', 'mary', 'ning']
>>> sorted(tel.keys())
['mary', 'mike', 'ning']
>>> tel[Mike]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tel[Mike]
NameError: name 'Mike' is not defined
>>> tel['Mike']
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    tel['Mike']
KeyError: 'Mike'
>>> tel['mike']
3759
>>> tel('mike')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    tel('mike')
TypeError: 'dict' object is not callable
>>> 'mike' in tel
True
>>> tel['ada'=1002]
SyntaxError: invalid syntax
>>> tel['ada']=10008
>>> tel
{'mike': 3759, 'mary': 1462, 'ning': 6959, 'ada': 10008}
>>> del tel['mary']
>>> tel
{'mike': 3759, 'ning': 6959, 'ada': 10008}
>>> if true:
	print('True')

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    if true:
NameError: name 'true' is not defined
>>> if True:
	print("True")

True
>>> a=[x * x for x in range(1,11) ]
>>> n=25
>>> if n in a:
	print(n," is a perfect square")
else:
	print(n,' is not a perfect square')

25  is a perfect square
>>> a=[2,6,5,7,4,9,8]
>>> for x in a:
	if x % 2 ==0:
		print(x)

2
6
4
8
>>> for x in a:
	if x % 2==0:
		continue
	print(x)

5
7
9
>>> a=range(1,101)
>>> sum=0
>>> for x in :
	
SyntaxError: invalid syntax
>>> for x in a:
	sum=sum + x
print(sum)
SyntaxError: invalid syntax
>>> print(sum)
0
>>> a
range(1, 101)
>>> for x in a:
	sum=sum + x
print(sum)
SyntaxError: invalid syntax
>>> for x in a :
	sum=sum + x
	print(sum)

1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210
231
253
276
300
325
351
378
406
435
465
496
528
561
595
630
666
703
741
780
820
861
903
946
990
1035
1081
1128
1176
1225
1275
1326
1378
1431
1485
1540
1596
1653
1711
1770
1830
1891
1953
2016
2080
2145
2211
2278
2346
2415
2485
2556
2628
2701
2775
2850
2926
3003
3081
3160
3240
3321
3403
3486
3570
3655
3741
3828
3916
4005
4095
4186
4278
4371
4465
4560
4656
4753
4851
4950
5050
>>> for x in a :
	sum=sum+x
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> x=[value for value in range(1,51)]
>>> a=['3k']
>>> b=['3k+1']
>>> c=['3k+2']
>>> l=len
>>> l=len(x)
>>> k=1
>>> while k<=t:
	if x[0]%3==0:
		a.insert(0,x[0])
		x.remove(x[0])
	elif x[0]%3==1:
		b.insert(0,x[0])
		x.remove(x[0])
	else:
		c.insert(0,x[0])
		x.remove(x[0])
	k=k+1
else:
	print(a)
	print(b)
	print(c)

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    while k<=t:
NameError: name 't' is not defined
>>> while k<=l:
	if x[0]%3==0:
		a.insert(0,x[0])
		x.remove(x[0])
	elif x[0]%3==1:
		b.insert(0,x[0])
		x.remove(x[0])
	else:
		c.insert(0,x[0])
		x.remove(x[0])
	k=k+1
else:
	print(a)
	print(b)
	print(c)

[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, '3k']
[49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, '3k+1']
[50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, '3k+2']
>>> import math
>>> math.exp(e)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    math.exp(e)
NameError: name 'e' is not defined
>>> math.exp(0)
1.0
>>> math.exp(1)
2.718281828459045
7-2
Out[2]: 5

import numpy as np

A=np.array([[1,2],[3,4]])

A
Out[5]: 
array([[1, 2],
       [3, 4]])

A.T
Out[6]: 
array([[1, 3],
       [2, 4]])

from scipy import linalg

B=linalg.inv(A)

B
Out[9]: 
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

A.dot(B)
Out[10]: 
array([[1.0000000e+00, 0.0000000e+00],
       [8.8817842e-16, 1.0000000e+00]])

import matplotlib.pyplot as plt

x=[1,2,3,4,5]

y=[3,4,6,2,4,8]

x=[1,2,3,4,5,6]

plt.plot(x,y)
Out[15]: [<matplotlib.lines.Line2D at 0x274461031c8>]


图表现在默认显示于绘图窗格上。要想让其也在中断行中显示，请在绘图窗格选项菜单中取消勾选“禁用行内绘图”。 


 

plt.plot(x,y)
Out[16]: [<matplotlib.lines.Line2D at 0x27446a72a48>]
￼

def parity(n):
    if n%2==0:
        print(n,'是偶数')
    elif n%2==1:
        print(n,'是奇数')
    else:
        print(n,'既不是奇数也不是偶数')


help(parity)
Help on function parity in module __main__:

parity(n)


parity(3)
3 是奇数

parity(3.2)
3.2 既不是奇数也不是偶数

f=lambda x:x**2

f(2)
Out[22]: 4



def make_incrementor(n):
    return lambda x:x+n


f=make_incrementor(42)

f(0),f(1)
Out[25]: (42, 43)

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(3,'A','b','c')
A --> c
A --> b
c --> b
A --> c
b --> A
b --> c
A --> c

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s


power(5)
Out[29]: 25

power(5,4)
Out[30]: 625

import functoola
Traceback (most recent call last):

  File "<ipython-input-31-0de3e96729d0>", line 1, in <module>
    import functoola

ModuleNotFoundError: No module named 'functoola'


del triangles(n):
    L=[1]
  File "<ipython-input-32-a713df191e17>", line 1
    del triangles(n):
                    ^
SyntaxError: invalid syntax


def triangles(n):
    L=[1]
    for x in range(n):
        yield L
        L=[1]+[L[i]+L[i+1]for i in range(len(L)-1)+[1]]
for x in triangles(9):
    print(x)

[1]
Traceback (most recent call last):

  File "<ipython-input-33-fa7202bb6a0a>", line 6, in <module>
    for x in triangles(9):

  File "<ipython-input-33-fa7202bb6a0a>", line 5, in triangles
    L=[1]+[L[i]+L[i+1]for i in range(len(L)-1)+[1]]

TypeError: unsupported operand type(s) for +: 'range' and 'list'


def triangles(n):
    L=[1]
    for x in range(n):
        yield L
        L=[1]+[L[i]+L[i+1]for i in range(len(L)-1)]+[1]
for x in triangles(10):
    print(x)

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

def add(x,y,f):
    return f(x)+f(y)
add(-5,4,abs)
Out[35]: 9

list(map(str,[1,2,1,3,4,5]))
Out[36]: ['1', '2', '1', '3', '4', '5']

def norm(name):
    name=name.lower()
    name=name.capitalize()
    return name
list(map(name,['adam','LISA','barT']))
Traceback (most recent call last):

  File "<ipython-input-37-0d2f52b846cf>", line 5, in <module>
    list(map(name,['adam','LISA','barT']))

NameError: name 'name' is not defined


list(map(norm,['adam','LISA','barT']))
Out[38]: ['Adam', 'Lisa', 'Bart']

from functools import reduce

def pro(L):
    return reduce(lamba x,y:x*y,L)
  File "<ipython-input-40-4b44e5eaafc1>", line 2
    return reduce(lamba x,y:x*y,L)
                        ^
SyntaxError: invalid syntax


def pro(L):
    return reduce(lambda x,y:x*y,L)
pro([1,2,3,4])
Out[41]: 24
list(filter(lambda x: x % 2==1,[1,2,4,5,6,9,10,13]))
Out[46]: [1, 5, 9, 13]

sorted([36,4,-12,9,-21])
Out[47]: [-21, -12, 4, 9, 36]

sorted([36,4,-12,9,-21],key=abs)
Out[48]: [4, 9, -12, -21, 36]

students=[('bob',75),('adam',92),('bart',88)]

print(sorted(students,keys=lambda x:x{0}))
  File "<ipython-input-50-cad20295e517>", line 1
    print(sorted(students,keys=lambda x:x{0}))
                                         ^
SyntaxError: invalid syntax


print(sorted(students,key=lambda x:x{0}))
  File "<ipython-input-51-ba12ab506996>", line 1
    print(sorted(students,key=lambda x:x{0}))
                                        ^
SyntaxError: invalid syntax


print(sorted(students,key=lambda x:x[0]))
[('adam', 92), ('bart', 88), ('bob', 75)]

print(sorted(students,key=lambda x:x[1]))
[('bob', 75), ('bart', 88), ('adam', 92)]

print(sorted(students,key=lambda x:x[1],reverse=True))
[('adam', 92), ('bart', 88), ('bob', 75)]

class myclass:
    i=12345
    def f(self):
        return'hello class'


myclass.i
Out[56]: 12345

myclass.i=3

myclass.i
Out[58]: 3

class complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart


x=complex(3.0,-4.1)

x.r,x.i
Out[61]: (3.0, -4.1)

pwd
Out[62]: 'C:\\Users\\lenovo\\.spyder-py3'

pwd
Out[63]: 'C:\\Users\\lenovo\\.spyder-py3'

filer=open('test.txt','r')
Traceback (most recent call last):

  File "<ipython-input-64-fe75d5f3caeb>", line 1, in <module>
    filer=open('test.txt','r')

FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


filer=open('test.txt','r')

filer.read()
Out[66]: 'hello world'

filer.close()

filew=open('test.txt','w')

filew.write('i love python! \n')
Out[69]: 16

filew.close()

fi=open('test.txt','a')

fi.write('hello world! \n')
Out[72]: 14

fi.close()

with open('test.txt','a') as file:
    file.write('glad to see you')


import csv

data={'symbol':[],'date':[],'price':[]}

with open ('stocks.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader
  File "<ipython-input-77-bb12a6ec9416>", line 3
    for row in reader
                     ^
SyntaxError: invalid syntax


with open ('stocks.csv','r') as f :reader=csv.DictReader for row in reader
  File "<ipython-input-78-1bdc136484ca>", line 1
    with open ('stocks.csv','r') as f :reader=csv.DictReader for row in reader
                                                               ^
SyntaxError: invalid syntax


with open ('stocks.csv','r') as f
  File "<ipython-input-79-22fc983bb877>", line 1
    with open ('stocks.csv','r') as f
                                     ^
SyntaxError: invalid syntax


with open ('stocks.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        data['symbol'].append(row['symbol'])
      data['date'].append(row['date'])
  File "<tokenize>", line 5
    data['date'].append(row['date'])
    ^
IndentationError: unindent does not match any outer indentation level


data['price'].append(row['price'])
Traceback (most recent call last):

  File "<ipython-input-82-61ebe6c555e5>", line 1, in <module>
    data['price'].append(row['price'])

NameError: name 'row' is not defined


data['price'].append(float(row['price']))
Traceback (most recent call last):

  File "<ipython-input-83-4ba43098d6dd>", line 1, in <module>
    data['price'].append(float(row['price']))

NameError: name 'row' is not defined


data.keys()
Out[84]: dict_keys(['symbol', 'date', 'price'])

data['symbol']
Out[85]: []

for row in reader:
    data['symbol'].append(row['symbol'])
    data['date'].append(row['date'])
    data['price'].append(row['price'])

Traceback (most recent call last):

  File "<ipython-input-86-3a524cc41580>", line 1, in <module>
    for row in reader:

NameError: name 'reader' is not defined

import csv

data={'symbol':[],'date',[],'price':[]}
  File "<ipython-input-2-4749e6cbbcb9>", line 1
    data={'symbol':[],'date',[],'price':[]}
                            ^
SyntaxError: invalid syntax


data={'symbol':[],'date':[],'price':[]}

with open
  File "<ipython-input-4-3671784e1549>", line 1
    with open
             ^
SyntaxError: invalid syntax


with open('stocks.csv','r') as f:
    reader= csv.DictReader(f)
    for row in reader:
        data['symbol'].append(row['symbol'])
        data['date'].append(row['date'])
        data['price'].append(float(row['price']))

Traceback (most recent call last):

  File "<ipython-input-5-d343a06bdb7e>", line 1, in <module>
    with open('stocks.csv','r') as f:

FileNotFoundError: [Errno 2] No such file or directory: 'stocks.csv'


with open('stocks.csv','r')
  File "<ipython-input-6-aaf7e288c99a>", line 1
    with open('stocks.csv','r')
                               ^
SyntaxError: invalid syntax


with open('stocks.csv','r')as f
  File "<ipython-input-7-7bc4ee57f45c>", line 1
    with open('stocks.csv','r')as f
                                   ^
SyntaxError: invalid syntax


open('stocks.csv','r')
Out[8]: <_io.TextIOWrapper name='stocks.csv' mode='r' encoding='cp936'>

with open('stocks.csv','r') as f:
    reader=csv.DictReader(f)


for row in reader:
    data['symbol'].append(row['symbol'])
    data['date'].append(row['date'])
    data['price'].append(row['price'])

Traceback (most recent call last):

  File "<ipython-input-10-3a524cc41580>", line 1, in <module>
    for row in reader:

  File "C:\Users\lenovo\anaconda3\lib\csv.py", line 111, in __next__
    self.fieldnames

  File "C:\Users\lenovo\anaconda3\lib\csv.py", line 98, in fieldnames
    self._fieldnames = next(self.reader)

ValueError: I/O operation on closed file.


import pandas

data2=pandas.read_csv('stocks.csv')

print(len(data2))
5

print(type(data2))
<class 'pandas.core.frame.DataFrame'>

data2
Out[15]: 
   symbol      date  price
0     101  2020.1.1      1
1     102  2020.1.2      2
2     103  2020.1.3      3
3     104  2020.1.4      4
4     105  2020.1.5      5

data2.iloc[1]
Out[16]: 
symbol         102
date      2020.1.2
price            2
Name: 1, dtype: object

data2.iloc[1]['date']
Out[17]: '2020.1.2'

import nltk

nltk.download('punkt')
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\lenovo\AppData\Roaming\nltk_data...

para="Python is a widely used general-purpose, high-level programming␣ ,→language. Its design philosophy emphasizes code readability, and its syntax␣ ,→allows programmers to express concepts in fewer lines of code than would be␣ ,→possible in languages such as C++ or Java."

from nltk.tokenize import sent_tokenize
print(sent_tokenize(para))

from nltk.tokenize import word_tokenize
word_tokenize(para)

nltk.download('stopwords')

True

from nltk.corpus import stopwords
es=set(stopwords.words('english'))
print(english_stops)

from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer('[\w]'+'')
words=tokenizer.tokenize('smoking is now banned in many places')
print(words)

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
stemmer.stem('cooking')
