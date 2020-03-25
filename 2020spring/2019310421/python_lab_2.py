Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '已学过，但是部分内容还需温习'
'已学过，但是部分内容还需温习'
4
>>> 5**2 #求幂
25
>>> _ + 3 #'_'在Python中用于调用上一次结果
28
>>> a=[1,3,5]
>>> a[1:2] #[1:2]表示[1:2)
[3]
>>> a.append(4) #在末尾追加元素 4
>>> a
[1, 3, 5, 4]
>>> a.insert(2,'a') #在指定的位置添加元素 a
>>> a
[1, 3, 'a', 5, 4]
>>> del a[0] #移除指定位置的元素
>>> a
[3, 'a', 5, 4]
>>> a.pop()  #默认移除list的最后一个元素，并返回该元素的值
4
>>> a
[3, 'a', 5]
>>> a.pop(2)  #移除指定位置上的元素，也返回
5
>>> a
[3, 'a']
>>> '列表的值传递与址传递'
'列表的值传递与址传递'
>>> a=[1,2,6,2,4,9]
>>> c1=a
>>> c2=a[:]
>>> c3=a.copy()
>>> c1,c2,c3
([1, 2, 6, 2, 4, 9], [1, 2, 6, 2, 4, 9], [1, 2, 6, 2, 4, 9])
>>> a.append(00)
>>> a
[1, 2, 6, 2, 4, 9, 0]
>>> c1,c2,c3
([1, 2, 6, 2, 4, 9, 0], [1, 2, 6, 2, 4, 9], [1, 2, 6, 2, 4, 9])
>>> '可以看出c1与a同步变化，说明c1=a为地址传递，而c2,c3为值传递'
'可以看出c1与a同步变化，说明c1=a为地址传递，而c2,c3为值传递'
>>> '列表嵌套的使用'
'列表嵌套的使用'
>>> matrix=[[1,2,3,4],[5,6,7,8,9],[10,11,12]]
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12]]
>>> type(matrix)
<class 'list'>
>>> type(matrix)  #查看类型
<class 'list'>
>>> matrix[1][2]
7
>>> list(range(1,6,2)) #range(1,6,2)表示从1开始，每次加2，直到5；list[]则将前者的结果以列表的形式返回
[1, 3, 5]
>>> [x*x for x in range(1,69)]#列表生成式
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624]
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
>>> a={1,2,2,'a','a','bc'}  #几何中元素不重复
>>> a
{1, 2, 'a', 'bc'}
>>> type(a)
<class 'set'>
>>> #set 表示集合
>>> a=1,'a','b'
>>> a
(1, 'a', 'b')
>>> #元组
>>> type(a)
<class 'tuple'>
>>> #tuple 元组
>>> #元祖中可以嵌套不同类型的数据
>>> '元组中的元素不可变‘
SyntaxError: EOL while scanning string literal
>>> '元组中的元素不可变’
SyntaxError: EOL while scanning string literal
>>> '元组中的元素不可变'
'元组中的元素不可变'
>>> if True:
	print('True')

	
True
>>> n=3 #判断奇偶
>>> if n %2 =0:
	
SyntaxError: invalid syntax
>>> if n %2 == 0:
	print(n,'是偶数',sep='')
    elif n % 2 ==1 :
	    
SyntaxError: unindent does not match any outer indentation level
>>> if n %2 == 0:
	print(n,'是偶数',sep='')
    elif n % 2 == 1 :
	    
SyntaxError: unindent does not match any outer indentation level
>>> if n %2 == 0:
	print(n,'是偶数',sep='')
	elif n % 2 == 1 :
		
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
3is jishu
>>> n = 3 #判断奇偶性
if n %2 ==0 :
    print(n,'is oushu',sep='')
elif n %2 == 1 :
    print(n,'is jishu',sep='')
else:
    print(n,'neither jishu nor oushu',sep='')
    

SyntaxError: multiple statements found while compiling a single statement
>>> if n %2 ==0 :
    print(n,'is oushu',sep='')
elif n %2 == 1 :
    print(n,'is jishu',sep='')
else:
    print(n,'neither jishu nor oushu',sep='')

    
3is jishu
>>> for i in range(3):
	print(i)

	
0
1
2
>>> a={3,2,5,7,9,10,8}
>>> for x in a:
	if x % 2== 0 :
		continue
	print(x)

	
3
5
7
9
>>> for x in a:
	if x % 2== 0 :
		continue
		print(x)

		
>>> 'if 余数 is 0 ，判断下一个'
'if 余数 is 0 ，判断下一个'
>>> for i in range(5):
	if 2**i <10:
		print(i ,2 **i)
	else:
		break

	
0 1
1 2
2 4
3 8
>>> a= range(1,101)  #sum 1 to 100   range(a,b) : shows[a,b)
>>> sum=0
>>> for s in a :
	sum = sum + s
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> for s in a :
	sum = sum + s
print(sum)
SyntaxError: invalid syntax
>>> for s in a :
	sum = sum + s
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
5050
>>> a=range(1,101)
>>> sum=0
>>> for s in a :
    sum = sum + s
print(sum)
SyntaxError: invalid syntax
>>> 
for s in a :
    sum = sum + s
print(sum)
SyntaxError: invalid syntax
>>> a=range(1,101)  
sum=0
for s in a:
    sum=sum+s
print(sum)
SyntaxError: multiple statements found while compiling a single statement
>>> for s in a:
	    sum=sum+s
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> for s in range(1,101)
SyntaxError: invalid syntax
>>> for s in range(1,101):
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
>>> for s in range(1,101):
	sum=sum+s
print(sum)
SyntaxError: invalid syntax
>>> for s in range(1,101):
	sum=sum+s
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
Select a number :15
[1, 3, 5, 15]
>>> ##进一步的我们可以判断一个数是否为素数
a=input('Select a number :')
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
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
Select a number :15
15  is not a prime
>>> tel= dict(mike=3759,mary=1462,ning=6839)
>>> tel
{'mike': 3759, 'mary': 1462, 'ning': 6839}
>>> tel= dict([('mike',3759),('mary',1462),('ning'=6839)])
SyntaxError: invalid syntax
>>> tel= dict([('mike',3759),('mary',1462),('ning',6839)])
>>> tel
{'mike': 3759, 'mary': 1462, 'ning': 6839}
>>> tel= dict([('mike',3759,2),('mary',1462,3),('ning',6839,6)])
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    tel= dict([('mike',3759,2),('mary',1462,3),('ning',6839,6)])
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> tel= dict([('mike',3759),('mary',1462),('ning',6839)])
>>> tel
{'mike': 3759, 'mary': 1462, 'ning': 6839}
>>> print(tel.keys())
dict_keys(['mike', 'mary', 'ning'])
>>> print(tel.values())
dict_values([3759, 1462, 6839])
>>> #前者反馈关键字，后者返回值
>>> list(tel.keys())
['mike', 'mary', 'ning']
>>> list(tel())
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    list(tel())
TypeError: 'dict' object is not callable
>>> list(tel.values())
[3759, 1462, 6839]
>>> sorted(tel.keys())
['mary', 'mike', 'ning']
>>> tel['mike']
3759
>>> 'mike' in tel
True
>>> tel['ada']=8080
>>> tel
{'mike': 3759, 'mary': 1462, 'ning': 6839, 'ada': 8080}
>>> ##进一步的我们可以判断一个数是否为素数
a=input('Select a number :')
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
>>> a= input('Select a number:
	 
SyntaxError: EOL while scanning string literal
>>> a= input('Select a number:'
	 divisors=[]
	 
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
Select a number :15
15  is not a prime
>>> cat JiOuXing.py
SyntaxError: invalid syntax
>>> source JiOuXing.py
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
0 1
1 2
2 4
3 8
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
Select an integer:15
Its not a perfect square 
>>> 
= RESTART: C:/Users/Asus/AppData/Local/Programs/Python/Python37/JiOuXing.py =
Select an integer:121
Its square root is 11
>>> import math
>>> math.exp(0)
1.0
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir (print)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> import math as mt
>>> mt.exp(0)
1.0
>>> from math import exp
>>> exp(0)
1.0
>>> from math improt exp as myexp
SyntaxError: invalid syntax
>>> from math import exp as myexp
>>> myexp(0)
1.0
>>> '以上为四种导入math的方法'
'以上为四种导入math的方法'
>>> 'again'
'again'
>>> import math
>>> math.exp(0)
1.0
>>> import math as mt
>>> mt.exp(0)
1.0
>>> from math import exp
>>> exp(0)
1.0
>>> from math import exp as myexp
>>> myexp(0)
1.0
>>> "mastered
SyntaxError: EOL while scanning string literal
>>> "mastered
SyntaxError: EOL while scanning string literal
>>> "mastered"
'mastered'
>>> 'numpy (Numerical Python) 提供了Pyhon对多维数组对象的支持'
'numpy (Numerical Python) 提供了Pyhon对多维数组对象的支持'
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> pip install numpy
SyntaxError: invalid syntax
>>> 
