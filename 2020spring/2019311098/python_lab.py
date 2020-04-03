Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+2
7
>>> 5-2
3
>>> 5*2
10
>>> 3**3
27
>>> 5^2
7
>>> 3^2
1
>>> 3^3
0
>>> 5^5
0
>>> 2^3
1
>>> 2^5
7
>>> 5/2
2.5
>>> 5//2
2
>>> 3//2
1
>>> 3/2
1.5
>>> 5%2
1
>>> 5%3
2
>>> _+4
6
>>> _*2
12
>>> a='A cat'
>>> a
'A cat'
>>> type(a)
<class 'str'>
>>> a="A cat"
>>> a
'A cat'
>>> type(a)
<class 'str'>
>>> len(a)
5
>>> a[0]
'A'
>>> a[-1]
't'
>>> a[2:]
'cat'
>>> a[1:]
' cat'
>>> a[2:4]
'ca'
>>> a[2:7]
'cat'
>>> b="A"+" "+
SyntaxError: invalid syntax
>>> b="A"+" "+"cat"
>>> b
'A cat'
>>> '7'*3
'777'
>>> b="A"+" "*3+"cat"
>>> b
'A   cat'
>>> print("A cat")
A cat
>>> print("3+2")
3+2
>>> print("A \n cat")
A 
 cat
>>> print(r"A \n cat")
A \n cat
>>> a=[1,2,3]
>>> a
[1, 2, 3]
>>> type(a)
<class 'list'>
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[-1]
3
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append(6,7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.append(6,7)
TypeError: append() takes exactly one argument (2 given)
>>> a.append(6)
>>> a
[1, 2, 3, 4, 6]
>>> a.insert(4,'b')
>>> a
[1, 2, 3, 4, 'b', 6]
>>> a.remove('b')
>>> a
[1, 2, 3, 4, 6]
>>> b=[4,5,6]
>>> b
[4, 5, 6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 6, 4, 5, 6]
>>> a.remove(4)
>>> a
[1, 2, 3, 6, 4, 5, 6]
>>> a.remove(6)
>>> a
[1, 2, 3, 4, 5, 6]
>>> del a[3]
>>> a
[1, 2, 3, 5, 6]
>>> a.pop()
6
>>> a
[1, 2, 3, 5]
>>> a.pop(1)
2
>>> a
[1, 3, 5]
>>> a=[1,3,2,3,4]
>>> a
[1, 3, 2, 3, 4]
>>> a.sort()
>>> a
[1, 2, 3, 3, 4]
>>> a.reverse()
>>> a
[4, 3, 3, 2, 1]
>>> a=[1,2,13,5,7]
>>> a.sort()
>>> a
[1, 2, 5, 7, 13]
>>> a=[1,3,2,3,4]
>>> a.sort()
>>> a
[1, 2, 3, 3, 4]
>>> a.reverse()
>>> a
[4, 3, 3, 2, 1]
>>> a.count(3)
2
>>> a.count(1)
1
>>> a.index(3)
1
>>> a.index(2)
3
>>> c1=a
>>> c2=a[:]
>>> c3=a.copy()
>>> c1,c2,c3
([4, 3, 3, 2, 1], [4, 3, 3, 2, 1], [4, 3, 3, 2, 1])
>>> a.append(4)
>>> a
[4, 3, 3, 2, 1, 4]
>>> [c1,c2,c3]
[[4, 3, 3, 2, 1, 4], [4, 3, 3, 2, 1], [4, 3, 3, 2, 1]]
>>> matrix=[[1,2,3,4],[5,6,7,8,9],[10,11,12]]
>>> type(matrix)
<class 'list'>
>>> matrix[1][2]
7
>>> matrix[0][1]
2
>>> matrix[-1][-2]
11
>>> matrix[-2][-1]
9
>>> matrix[2][1]
11
>>> matrix[1][2]
7
>>> list(range(1,6,2))
[1, 3, 5]
>>> list(range(1,7,2))
[1, 3, 5]
>>> list(range(1,8,2))
[1, 3, 5, 7]
>>> list(range(1,5,2))
[1, 3]
>>> list(range(1,16,3))
[1, 4, 7, 10, 13]
>>> [x*x for x in range(1,10)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x*x for x in range(1,10.1)]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    [x*x for x in range(1,10.1)]
TypeError: 'float' object cannot be interpreted as an integer
>>> [m+n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
>>> a={1,2,2,'a','a','bc'}
>>> a
{1, 2, 'a', 'bc'}
>>> a=[1,2,2,'a','a','bc']
>>> a
[1, 2, 2, 'a', 'a', 'bc']
>>> {a}
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    {a}
TypeError: unhashable type: 'list'
>>> a={a}
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a={a}
TypeError: unhashable type: 'list'
>>> a
[1, 2, 2, 'a', 'a', 'bc']
>>> a={1,2,2,'a','a','bc'}
>>> a
{1, 2, 'a', 'bc'}
>>> type(a)
<class 'set'>
>>> 'a' in a
True
>>> 'b' in a
False
>>> b={1,3,'b','c'}
>>> b
{1, 'b', 3, 'c'}
>>> a|b
{1, 2, 'a', 3, 'bc', 'c', 'b'}
>>> b={1,3,'b','c'}
>>> b
{1, 'b', 3, 'c'}
>>> a&b
{1}
>>> a-b
{2, 'a', 'bc'}
>>> a^b
{2, 3, 'a', 'c', 'bc', 'b'}
>>> a=set('122abb')
>>> a
{'1', '2', 'b', 'a'}
>>> a=1,'a','b'
>>> a
(1, 'a', 'b')
>>> type(a)
<class 'tuple'>
>>> b=[1,'c']
>>> b
[1, 'c']
>>> c=a,b
>>> c
((1, 'a', 'b'), [1, 'c'])
>>> c[0]
(1, 'a', 'b')
>>> c[1][1]
'c'
>>> c[1][1]`
SyntaxError: invalid syntax
>>> c[0]=1
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    c[0]=1
TypeError: 'tuple' object does not support item assignment
>>> c[1][1]=2
>>> c
((1, 'a', 'b'), [1, 2])
>>> tel={'Mike':3759,'Mary':1462,'Ning':6839}
>>> print(tel)
{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}
>>> type(tel)
<class 'dict'>
>>> tel=dict(Mike=3759,Mary=1462,Ning=6839)
>>> tel
{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}
>>> tel=dict([('Mike',3759),('Mary',1462),('Ning',6839)])
>>> tel
{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}
>>> print(tel.keys())
dict_keys(['Mike', 'Mary', 'Ning'])
>>> print(tel.values())
dict_values([3759, 1462, 6839])
>>> list(tel.keys())
['Mike', 'Mary', 'Ning']
>>> sorted(tel.keys())
['Mary', 'Mike', 'Ning']
>>> reversed(tel.keys())
<dict_reversekeyiterator object at 0x0000020C319308B0>
>>> sorted(tel.keys())
['Mary', 'Mike', 'Ning']
>>> tel['Mike']
3759
>>> 'Mike' in tel
True
>>> tel['Ada']=8080
>>> tel
{'Mike': 3759, 'Mary': 1462, 'Ning': 6839, 'Ada': 8080}
>>> sorted(tel.keys())
['Ada', 'Mary', 'Mike', 'Ning']
>>> del tel['Mary']
>>> tel
{'Mike': 3759, 'Ning': 6839, 'Ada': 8080}
>>> if True:
	print('True')

	
True
>>> n=3
>>> if n%2=0:
	
SyntaxError: invalid syntax
>>> n=3
>>> if n%2==0:
	print(n,'是偶数',sep=' ')
    elif n%2==1:
	    
SyntaxError: unindent does not match any outer indentation level
>>> n=3
>>> if n%2 == 0:
	print(n,'是偶数',sep='')
	elif n%2 == 1:
		
SyntaxError: invalid syntax
>>> n=3
>>> if n%2==0:
	print(n,'是偶数'，sep='')
	
SyntaxError: invalid character in identifier
>>> n=3
>>> if n%2==0:
	print(n,'是偶数',sep='')
    elif n%2==1:
	    
SyntaxError: unindent does not match any outer indentation level
>>> n = 3
if n % 2 == 0:
    print(n,'是偶数',sep = '')
elif n % 2 == 1:
    print(n,'是奇数',sep = '')
else:
    print(n,'既不是奇数也不是偶数',sep = '')
    
SyntaxError: multiple statements found while compiling a single statement
>>> n=3
>>> if n % 2 == 0:
    print(n,'是偶数',sep = '')
elif n % 2 == 1:
    print(n,'是奇数',sep = '')
else:
    print(n,'既不是奇数也不是偶数',sep = '')

    
3是奇数
>>> n=3
>>> if n%2==0:
	print(n,'是偶数',sep='')
elif n%2==1:
	print(n,'是奇数',sep='')
else:
	print(n,'既不是奇数也不是偶数',sep='')

	
3是奇数
>>> a=[x**2 for x in range(1,10)]
>>> n=23
>>> if n in a:
	print(repr(n)+'is a perfect square')
else:
	print(n,'is not a perfect square')

	
23 is not a perfect square
>>> for i in range(3):
	print(i)

	
0
1
2
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(1,6,2):
	print(i)

	
1
3
5
>>> a=[1,4,5]
>>> for i in range(a):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    for i in range(a):
TypeError: 'list' object cannot be interpreted as an integer
>>> list(range(a))
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    list(range(a))
TypeError: 'list' object cannot be interpreted as an integer
>>> a={3,2,5,7,9,10,8}
>>> for x in a:
	if x%2==0:
		continue
	print(x)

	
3
5
7
9
>>> for i in range(5):
	if 2**i<10:
		print(i,2**i)
	else:
		break

	
0 1
1 2
2 4
3 8
>>> a={2,4,6,5,13,8}
>>> for x in a:
	if x%3==2
	
SyntaxError: invalid syntax
>>> a={2,4,5,6,9,13}
>>> for x in a:
	if x%3==2:
		continue
	print(x)

	
4
6
9
13
>>> for i in range(5):
	if 2**i<10:
		print(i,2**i)
	else:
		break

	
0 1
1 2
2 4
3 8
>>> for i in range(5):
	if 2**i>10:
		print(i)
	else:
		break

	
>>> for i in range(5):
	if 2**i>10:
		print(i,2**i)
	else:
		break

	
>>> for i in range(5):
	if 2**i<10:
		print(i)
	else:
		break

	
0
1
2
3
>>> range(3)
range(0, 3)
>>> a=range(3)
>>> a
range(0, 3)
>>> list(range(3))
[0, 1, 2]
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> for i in range(5):
	if 2**i>10:
		print(i,2**i)
	else:
		break

	
>>> 
KeyboardInterrupt
>>> for i in range(5):
	if 2**i>5:
		print(i,2**i)
	else:
		break

	
>>> 
>>> a=range(1,101)
>>> sum=0
>>> for s in a:
	sum=sum+s
print(sum)
SyntaxError: invalid syntax
>>> a=range(1,101)
>>> sum=0
>>> for s in a:
	sum=sum+s
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
>>>  a=range(1,101)
>>> sum=0
>>> for s in a:
	sum=sum+s
	until s=100
	print(sum)
	
SyntaxError: unexpected indent
>>> a=range(1,101)
>>> sum=0
>>> for s in a:
	sum=sum+s
	until s=100
	print(sum)
	
SyntaxError: multiple statements found while compiling a single statement
>>> a=range(1,6)
>>> factorial=1
>>> for s in a:
	factorial=factorial*s
	print(factorial)

	
1
2
6
24
120
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(a)+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	print(divisors)

	
[1]
[1]
[1, 3]
[1, 3]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5, 15]
>>> a=input('Select a number :')
Select a number :15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
divisors.remove(1)
SyntaxError: invalid syntax
>>> a=input('Select a number :')
Select a number :15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
		
SyntaxError: multiple statements found while compiling a single statement
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
		divisors remove(1)
		
SyntaxError: invalid syntax
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor=0:
			
SyntaxError: invalid syntax
>>>  a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			
SyntaxError: unexpected indent
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			
SyntaxError: multiple statements found while compiling a single statement
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			flag='false'
			break
	if flag=='true':
		print(a,'is a prime')
	else:
		print(a,'is not a prime')

		
15 is a prime
Traceback (most recent call last):
  File "<pyshell#337>", line 4, in <module>
    divisors.remove(1)
ValueError: list.remove(x): x not in list
>>> a=input('Select a number:')
Select a number:15
>>>  divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			flag='false'
			break
	        if flag=='true':
		        print(a,'is a prime')
	        else:
		        print(a,'is not a prime')
		        
SyntaxError: unexpected indent
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			flag='false'
			break
	        if flag=='true':
		        print(a,'is a prime')
	        else:
		        print(a,'is not a prime')
		        
SyntaxError: multiple statements found while compiling a single statement
>>> a=input('Select a number:')
Select a number:15
>>> divisors=[]
>>> m=[value for value in range(1,int(int(a)**(1/2))+1)]
>>> for s in m:
	if int(a)%s==0:
		divisors.append(s)
	divisors.remove(1)
	flag='true'
	for divisor in divisors:
		if int(a)%divisor==0:
			flag='false'
			break
		if flag=='true':
			print(a,' is a prime')
		else:
			print(a,' is not a prime')

			
Traceback (most recent call last):
  File "<pyshell#358>", line 4, in <module>
    divisors.remove(1)
ValueError: list.remove(x): x not in list
>>> a=input('Select a number :')
divisors=[]
m=[value for value in range (1,int(int(a)**(1/2))+1)]
for s in m:
    if int(a)%s==0:
        divisors.append(s)
divisors.remove(1)
flag='true'
for divisor in divisors:
    if int(a)%divisor==0:
        flag='false'
        break
if flag=='true':
    print(a,' is a prime')
else:
    print(a,' is not a prime')
    
SyntaxError: multiple statements found while compiling a single statement
>>> a=input('Select a number :')
divisors=[]
m=[value for value in range (1,int(int(a)**(1/2))+1)]
for s in m:
    if int(a)%s==0:
        divisors.append(s)
divisors.remove(1)
flag='true'
for divisor in divisors:
    if int(a)%divisor==0:
        flag='false'
        break
if flag=='true':
    print(a,' is a prime')
else:
    print(a,' is not a prime')
    
SyntaxError: multiple statements found while compiling a single statement
>>> a=0
>>> while 2**a<10:
	print(a,2**a)
	a=a+1

	
0 1
1 2
2 4
3 8
>>> a=[1,1]
>>> k=3
>>> x=input('请输入项数(>=3):')
请输入项数(>=3):15
>>> while k<=int(x):
	b=a[-1]+a[-2]
	a.append(b)
	k=k+1
	print(a)

	
[1, 1, 2]
[1, 1, 2, 3]
[1, 1, 2, 3, 5]
[1, 1, 2, 3, 5, 8]
[1, 1, 2, 3, 5, 8, 13]
[1, 1, 2, 3, 5, 8, 13, 21]
[1, 1, 2, 3, 5, 8, 13, 21, 34]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
>>> a=[1,1]
>>> b=a[-1]+a[-2]
>>> b
2
>>> a=[1,1]
>>> xx=input('Select an integer:')
Select an integer:24
>>> x=int(xx)
>>> ans=0
>>> if x>0:
	while ans*ans<x:
		ans=ans+1
		if ans**2==x:
			print('Its square root is '+repr(ans))
		else:
			print('Its not a perfect square')
	else:
		print('It is not a positive integer')

		
Its not a perfect square
Its not a perfect square
Its not a perfect square
Its not a perfect square
Its not a perfect square
It is not a positive integer
>>> x=[value for value in range(1,50)]
>>> a=['3k']
>>> b=['3k+1']
>>> c=['3k+2']
>>> t=len(x)
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

	
[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, '3k']
[49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, '3k+1']
[47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, '3k+2']
>>> import math
>>> math.exp(0)
1.0
>>> import math
>>> math.exp(1)
2.718281828459045
>>> import math as mt
>>> mt.exp(0)
1.0
>>> from math import exp
>>> exp(0)
1.0
>>> from math import exp
>>> exp(1)
2.718281828459045
>>> from math import exp as myexp
>>> myexp
<built-in function exp>
>>> myexp(0)
1.0
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#427>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#428>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> A=np.array([[1,2],[3,4]])
Traceback (most recent call last):
  File "<pyshell#429>", line 1, in <module>
    A=np.array([[1,2],[3,4]])
NameError: name 'np' is not defined
>>> A
Traceback (most recent call last):
  File "<pyshell#430>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> import numpy as np \nA=np.array([[1,2],[3,4]])
SyntaxError: unexpected character after line continuation character
>>> A
Traceback (most recent call last):
  File "<pyshell#432>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> A.T
Traceback (most recent call last):
  File "<pyshell#433>", line 1, in <module>
    A.T
NameError: name 'A' is not defined
>>> from scipy import linalg
Traceback (most recent call last):
  File "<pyshell#434>", line 1, in <module>
    from scipy import linalg
ModuleNotFoundError: No module named 'scipy'
>>> pwd
Traceback (most recent call last):
  File "<pyshell#435>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> 