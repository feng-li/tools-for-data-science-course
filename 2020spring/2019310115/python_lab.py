5 + 2
7

a = "Li Feng"
a
'Li Feng'

a = [1,2,3]

a = {1,2,2,'a','a','bc'} # 集合中元素不重复
a
{1, 2, 'a', 'bc'}

a = 1,'a','b' # 元组由逗号分隔的多个值组成
a
(1, 'a', 'b')

tel = {'Mike':3759, 'Mary':1462, 'Ning':6839}
print(tel)
type(tel)
{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}

if True:
    print('True') # 基本语法
True

for i in range(3):
    print(i)
0
1
2

a = 0
while 2 ** a < 10:
    print(a,2 ** a)
    a = a + 1
0 1
1 2
2 4
3 8

import math
math.exp(0)
1.0

def parity(n):
    """To judge whether an integer is odd or even.""" # the function help
    if n % 2 == 0:
        print(n,'是偶数',sep = '')
    elif n % 2 == 1:
        print(n,'是奇数',sep = '')
    else:
        print(n,'既不是奇数也不是偶数',sep = '')

def triangles(n): # 杨辉三角
    L = [1]
    for x in range(n):
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

def add(x, y, f):
    return f(x) + f(y)

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

pwd
'C:\\Users\\Administrator\\Desktop'

import csv

data = {'symbol':[], 'date':[], 'closing_price' : []}
with open('stocks.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data['symbol'].append(row["symbol"])
        data['date'].append(row["date"])
        data['closing_price'].append(float(row["closing_price"]))

import nltk

