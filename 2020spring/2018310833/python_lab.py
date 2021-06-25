Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "Li Feng"
>>> type(a)
<class 'str'>
>>> len(a)
7
>>> a[1]
'i'
>>> a[1;4]
SyntaxError: invalid syntax
>>> a[1:4]
'i F'
>>> a[2:]
' Feng'
>>> b = "L"+""*3+"F"
>>> b
'LF'
>>> print("LF")
LF
>>> print("L\nF")
L
F
>>> print(r"L\nF")
L\nF
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a[0]
1
>>> a.insert(2,'a')
>>> a
[1, 2, 'a', 3, 4]
>>> b = [4,5,6]
>>> a.extend(b)
>>> a
[1, 2, 'a', 3, 4, 4, 5, 6]
>>> a.remove(4)
>>> a
[1, 2, 'a', 3, 4, 5, 6]
>>> del a[4]
>>> 
>>> a
[1, 2, 'a', 3, 5, 6]
>>> a.pop(-1)
6
>>> a
[1, 2, 'a', 3, 5]
>>> c =[342114,4234,234,2323,3423435,34,23,123]
>>> c.sort()
>>> c
[23, 34, 123, 234, 2323, 4234, 342114, 3423435]
>>> c.reverse()
>>> c
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> c.count(10)
0
>>> c.index(234)
4
>>> c1 =c
>>> c2 =c[:]
>>>  c3 =c.copy()
 
SyntaxError: unexpected indent
>>> c3 =c.copy()
>>> c1
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> x2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x2
NameError: name 'x2' is not defined
>>> c2
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> c3
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> c.append(4)
>>> c
[3423435, 342114, 4234, 2323, 234, 123, 34, 23, 4]
>>> c1
[3423435, 342114, 4234, 2323, 234, 123, 34, 23, 4]
>>> c2
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> c3
[3423435, 342114, 4234, 2323, 234, 123, 34, 23]
>>> matrix = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
>>> type(matrix)
<class 'list'>
>>> matrix[1][2]
4
>>> list(range(1,6,2))
[1, 3, 5]
>>> [x * x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [m + n for m in 'ABC'for n in 'EDF']
['AE', 'AD', 'AF', 'BE', 'BD', 'BF', 'CE', 'CD', 'CF']
>>> a = {1,2,3,'a','b','c'}
>>> a
{1, 2, 3, 'b', 'a', 'c'}
>>> type(a)
<class 'set'>
>>> 'a' in a
True
>>> 4 in a
False
>>> b = {3,5,'g','a'}
>>> b
{'g', 3, 5, 'a'}
>>> a | b
{1, 2, 3, 5, 'b', 'a', 'c', 'g'}
>>> a&b
{3, 'a'}
>>> a-b
{1, 2, 'c', 'b'}
>>> a^b
{1, 2, 5, 'b', 'c', 'g'}
>>> a = set('122add')
>>> a
{'2', 'd', 'a', '1'}
>>> a = 1,'a','b'
>>> a
(1, 'a', 'b')
>>> type(a)
<class 'tuple'>
>>> b = [1,'c']
>>> c = a,b
>>> c
((1, 'a', 'b'), [1, 'c'])
>>> c[0]
(1, 'a', 'b')
>>> c[0][2]
'b'
>>> c[0][2] =2
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    c[0][2] =2
TypeError: 'tuple' object does not support item assignment
>>> c [1][0]=2
>>> c
((1, 'a', 'b'), [2, 'c'])
>>> tel = {'mike':324,'mary':2343,'jack':5636}
>>> print(tel)
{'mike': 324, 'mary': 2343, 'jack': 5636}
>>> tel = dict(mike = 324,mary = 2343,jack =5636)
>>> tel
{'mike': 324, 'mary': 2343, 'jack': 5636}
>>> tel = dict([('mike',342),('mary',32432),('jack',7686)])
>>> tel
{'mike': 342, 'mary': 32432, 'jack': 7686}
>>> print(tel.keys)
<built-in method keys of dict object at 0x00000297A81D9E00>
>>> print(tel.values())
dict_values([342, 32432, 7686])
>>> sorted(tel.keys())
['jack', 'mary', 'mike']
>>> tel['mike']
342
>>>  'miky' in tel
 
SyntaxError: unexpected indent
>>> 'miky' in tel
False
>>> tel['ada'] = 34534
>>> tel
{'mike': 342, 'mary': 32432, 'jack': 7686, 'ada': 34534}
>>> del tel['mike']
>>> tel
{'mary': 32432, 'jack': 7686, 'ada': 34534}
>>> if True:
	print('True')

	
True
>>> n = 3
>>> if n % 2 == 0:
    print(n,'是偶数',sep = '')
elif n % 2 == 1:
    print(n,'是奇数',sep = '')
else:
    print(n,'既不是奇数也不是偶数',sep = '')

    
3是奇数
>>> n=23
>>> a=[x**2 for x in range(1,10)]
>>> if n in a :
    print(repr(n)+' is a perfect square')
else:
    print(n,' is not a perfect square')

    
23  is not a perfect square
>>> for i in range(3): print(i)

0
1
2
>>> a = {3,2,5,7,9,10,8}
>>> for x in a:
	if x % 2 == 0:
		continue
	print(x)

	
3
5
7
9
>>> for i in range(5):
	if 2 ** i < 10:
		print(i,2 ** i)
	else: break

	
0 1
1 2
2 4
3 8
>>> a = range(1,101)
>>> sum = 0
>>> for s in a:
	sum = sum + s

	
>>> print(sum)
5050
>>> a=range(1,6)
>>> fac = 1
>>> for s in a:
	fac = fac * s

	
>>> print(fac)
120
>>> a = input('select a number:')
select a number:15
SyntaxError: multiple statements found while compiling a single statement
>>> a = input('select a number:')
select a number:15
>>> div = []
>>> m = [value for value in range (1,int(a)+1]
     
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> m = [value for value in range (1,int(a)+1)]
>>> for s in m:
	if int(a)%s == 0:
		div.append(s)

		
>>> print(div)
[1, 3, 5, 15]
>>> a = input('select a munber:')
select a munber:12903
>>> div = []
>>> m = [value for value in range (1,int(int(a)**0.5)+1)]
>>> divs = []
>>> for s in m:
	if int(a)%s == 0:
		divs.append(s)

		
>>> divs.remove(1)
>>> flag = 'true'
>>> for div in divs:
    if int(a)%div == 0:
        flag = 'false'
        break

>>> if flag == 'true':
    print(a,' is a prime')
else:
    print(a,' is not a prime')

    
12903  is not a prime
>>> a =0
>>> while 2 ** a < 10:
	print(a,2 ** a)
	a = a+1

	
0 1
1 2
2 4
3 8
>>> a = [1,1]
>>> k = 3
>>> x = input('shuru:')
shuru:234
>>> while k <= int(x):
	b = a[-1] + a[-2]
	a.append(b)
	k=k+1

	
>>> print(a)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026, 354224848179261915075, 573147844013817084101, 927372692193078999176, 1500520536206896083277, 2427893228399975082453, 3928413764606871165730, 6356306993006846248183, 10284720757613717413913, 16641027750620563662096, 26925748508234281076009, 43566776258854844738105, 70492524767089125814114, 114059301025943970552219, 184551825793033096366333, 298611126818977066918552, 483162952612010163284885, 781774079430987230203437, 1264937032042997393488322, 2046711111473984623691759, 3311648143516982017180081, 5358359254990966640871840, 8670007398507948658051921, 14028366653498915298923761, 22698374052006863956975682, 36726740705505779255899443, 59425114757512643212875125, 96151855463018422468774568, 155576970220531065681649693, 251728825683549488150424261, 407305795904080553832073954, 659034621587630041982498215, 1066340417491710595814572169, 1725375039079340637797070384, 2791715456571051233611642553, 4517090495650391871408712937, 7308805952221443105020355490, 11825896447871834976429068427, 19134702400093278081449423917, 30960598847965113057878492344, 50095301248058391139327916261, 81055900096023504197206408605, 131151201344081895336534324866, 212207101440105399533740733471, 343358302784187294870275058337, 555565404224292694404015791808, 898923707008479989274290850145, 1454489111232772683678306641953, 2353412818241252672952597492098, 3807901929474025356630904134051, 6161314747715278029583501626149, 9969216677189303386214405760200, 16130531424904581415797907386349, 26099748102093884802012313146549, 42230279526998466217810220532898, 68330027629092351019822533679447, 110560307156090817237632754212345, 178890334785183168257455287891792, 289450641941273985495088042104137, 468340976726457153752543329995929, 757791618667731139247631372100066, 1226132595394188293000174702095995, 1983924214061919432247806074196061, 3210056809456107725247980776292056, 5193981023518027157495786850488117, 8404037832974134882743767626780173, 13598018856492162040239554477268290, 22002056689466296922983322104048463, 35600075545958458963222876581316753, 57602132235424755886206198685365216, 93202207781383214849429075266681969, 150804340016807970735635273952047185, 244006547798191185585064349218729154, 394810887814999156320699623170776339, 638817435613190341905763972389505493, 1033628323428189498226463595560281832, 1672445759041379840132227567949787325, 2706074082469569338358691163510069157, 4378519841510949178490918731459856482, 7084593923980518516849609894969925639, 11463113765491467695340528626429782121, 18547707689471986212190138521399707760, 30010821454963453907530667147829489881, 48558529144435440119720805669229197641, 78569350599398894027251472817058687522, 127127879743834334146972278486287885163, 205697230343233228174223751303346572685, 332825110087067562321196029789634457848, 538522340430300790495419781092981030533, 871347450517368352816615810882615488381, 1409869790947669143312035591975596518914, 2281217241465037496128651402858212007295, 3691087032412706639440686994833808526209, 5972304273877744135569338397692020533504, 9663391306290450775010025392525829059713, 15635695580168194910579363790217849593217, 25299086886458645685589389182743678652930, 40934782466626840596168752972961528246147, 66233869353085486281758142155705206899077, 107168651819712326877926895128666735145224, 173402521172797813159685037284371942044301, 280571172992510140037611932413038677189525, 453973694165307953197296969697410619233826, 734544867157818093234908902110449296423351, 1188518561323126046432205871807859915657177, 1923063428480944139667114773918309212080528, 3111581989804070186099320645726169127737705, 5034645418285014325766435419644478339818233, 8146227408089084511865756065370647467555938, 13180872826374098837632191485015125807374171, 21327100234463183349497947550385773274930109, 34507973060837282187130139035400899082304280, 55835073295300465536628086585786672357234389, 90343046356137747723758225621187571439538669, 146178119651438213260386312206974243796773058, 236521166007575960984144537828161815236311727, 382699285659014174244530850035136059033084785, 619220451666590135228675387863297874269396512, 1001919737325604309473206237898433933302481297, 1621140188992194444701881625761731807571877809, 2623059926317798754175087863660165740874359106, 4244200115309993198876969489421897548446236915, 6867260041627791953052057353082063289320596021, 11111460156937785151929026842503960837766832936, 17978720198565577104981084195586024127087428957, 29090180355503362256910111038089984964854261893, 47068900554068939361891195233676009091941690850, 76159080909572301618801306271765994056795952743, 123227981463641240980692501505442003148737643593, 199387062373213542599493807777207997205533596336, 322615043836854783580186309282650000354271239929, 522002106210068326179680117059857997559804836265, 844617150046923109759866426342507997914076076194, 1366619256256991435939546543402365995473880912459, 2211236406303914545699412969744873993387956988653, 3577855662560905981638959513147239988861837901112]
>>> xx = input('select a integer:')
select a integer:30
>>> x = int (xx)
>>> if x>0:
    while ans*ans<x:
        ans=ans+1 
    if ans ** 2 == x:
        print('its square root is'+repr(ans))
    else:
        print("it's not a pefect square")
else:
    print("it's not a positive integer")

    
Traceback (most recent call last):
  File "<pyshell#154>", line 2, in <module>
    while ans*ans<x:
NameError: name 'ans' is not defined
>>> ans = 0
>>> 
KeyboardInterrupt
>>> if x>0:
    while ans*ans<x:
        ans=ans+1 
    if ans ** 2 == x:
        print('its square root is'+repr(ans))
    else:
        print("it's not a pefect square")
else:
    print("it's not a positive integer")

    
it's not a pefect square
>>> x = [value for value in range(1,50)]
>>> a = ['3k']
>>> b = ['3k+1']
>>> c = ['3k+2']
>>> t = len(x)
>>> k = 1
>>> while k <= t:
    if x[0]%3==0:
        a.insert(0,x[0])
        x.remove(x[0])
    elif x[0]%3 == 1:
        b.insert(0,x[0])
        x.remove(x[0])
    else:
        c.insert(0,x[0])
        x.remove(x[0])
    k = k+1
else:
    print(a)
    print(b)
    print(c)

    
[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, '3k']
[49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, '3k+1']
[47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, '3k+2']
>>> import math as mt
>>> mt.exp(0)
1.0
>>> from math import exp
>>> exp(0)
1.0
>>> from math import exp as myexp
>>> myexp(0)

1.0
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
>>> A = np.array([[1,2],[3,4]])
>>> a
[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, '3k']
>>> A
array([[1, 2],
       [3, 4]])
>>> A.T
array([[1, 3],
       [2, 4]])
>>> from scipy import linalg
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    from scipy import linalg
ModuleNotFoundError: No module named 'scipy'
>>> from scipy import linalg
>>> B = linalg.inv(A)
>>> B
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
>>> A.dot(B)
array([[1.0000000e+00, 0.0000000e+00],
       [8.8817842e-16, 1.0000000e+00]])
>>> import functools
>>>  import pandas
 
SyntaxError: unexpected indent
>>> import pandas
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
>>> import nltk
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    import nltk
ModuleNotFoundError: No module named 'nltk'
>>> import matplotlib.pyplot as plt
>>> x = [1,2,3,4,5,6]
>>> y = [3,4,5,6,7,8]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000297C21C9700>]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000297C21C9A60>]
>>> plt.show()
>>> def parity(n)
SyntaxError: invalid syntax
>>> def parity(n):
	if n%2 == 0:
		print(n,'shioushu',sep = '')
	elif n%2 == 1:
		print(n,'shijishu',sep = '')
	else:
		print(n,'jibuhsioushuyebushijishu',sep = '')

		
>>> help(parity)
Help on function parity in module __main__:

parity(n)

>>> parity(3)
3shijishu
>>> parity(243.3242)
243.3242jibuhsioushuyebushijishu
>>> f = lambda x :x ** 2
>>> f(2)
4
>>> def make_incrementor(n):
	return lambda x:x+n

>>> f = make_incrementor(234）
		     
SyntaxError: invalid character in identifier
>>> f = make_incrementor(234)
>>> f(0)
234
>>> def move(n,a,b,c):
	if n==1:
		print(a.'-->',c)
		
SyntaxError: invalid syntax
>>> def move(n,a,b,c):
	if n==1:
		print(a.'-->',c)\
				  
SyntaxError: invalid syntax
>>> def move(n,a,b,c):
	if n==1:
		print(a.'-->',c
		      
SyntaxError: invalid syntax
>>> def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c,)
		move(n-1,b,a,c)

		
>>> move(3,'A','B','C')
A --> C
A --> B
C --> B
A --> C
B --> A
B --> C
A --> C
>>> def power(x,n=2):
	s=1
	while n > 0:
		s = s*x
		n = n-1
	return s

>>> power(5)
25
>>> power(5,3)
125
>>> import functools
>>> int2 = functools.partial(int,base = 2)
>>> int('1000000')
1000000
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> def tri(n):
	L = [i]
	for x in range(n):
		yield L
		L = [1] + [L[i]+L[i+1]for i in range(len(L)-1]+[1]
			   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> def tri(n):
	L = [i]
	for x in range(n):
		yield L
		L = [1] + [L[i]+L[i+1]for i in range(len(L)-1)]+[1]

		
>>> for x in tri(10):
	print(x)

	
[4]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
>>> def tri(n):
	L = [1]
	for x in range(n):
		yield L
		L = [1] + [L[i]+L[i+1]for i in range(len(L)-1)]+[1]

		
>>> for x in tri(10):
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
>>> [1]+[2]
[1, 2]
>>> [1]+[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> [1]+[1]
[1, 1]
>>> def add(x,y,f):
	return f(x)+f(y)

>>> add(5,6,abs)
11
>>> list(map(str,[1,2,3,4,5,6,7,8,9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> def normalize(name):
	name = name.lower()
	name = name.capitalize()
	return name

>>> L = ['adam','JACK','KAas']
>>> list(map(normalize,L))
['Adam', 'Jack', 'Kaas']
>>> from functools import reduce
>>> def prod(L):
	return reduce(lambda x,y:x*y,L)

>>> prod([3,5,7,9])
945
>>> list(filter(lambda x ))
SyntaxError: invalid syntax
>>> list(filter(lambda x: x%2 ==1,[1,2,,4,5,6,9,10,15]))
SyntaxError: invalid syntax
>>> list(filter(lambda x: x%2 ==1,[1,2,6534,4,5,6,9,10,15]))
[1, 5, 9, 15]
>>> sorted([35,5,-23,4,-234],key = abs)
[4, 5, -23, 35, -234]
>>> students = [('bob',75),('adam',92),('brt',66),('lisa',88)]
>>> print(sorted(students,key = lambda x : x[0]))
[('adam', 92), ('bob', 75), ('brt', 66), ('lisa', 88)]
>>> print(sorted(students,key = lambda x : x[1]))
[('brt', 66), ('bob', 75), ('lisa', 88), ('adam', 92)]
>>> print(sorted(students,key = lambda x : x[1],reverse = True))
[('adam', 92), ('lisa', 88), ('bob', 75), ('brt', 66)]
>>> class MyClass:
	i = 12345
	def f(self):
		return 'hello world'

	
>>> MyClass()
<__main__.MyClass object at 0x00000297C05ED0A0>
>>> MyClass.i
12345
>>> MyClass.f
<function MyClass.f at 0x00000297C0A76550>
>>> MyClass.f=3
>>> MyClass.f
3
>>> MyClass.x=1
>>> MyClass
<class '__main__.MyClass'>
>>> class Complex:
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart

		
>>> x = Complex(3.0,-4.5)
>>> x.r,x.i
(3.0, -4.5)
>>> pwd
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>>  pwd

SyntaxError: unexpected indent
>>> pwd
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> cd
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    cd
NameError: name 'cd' is not defined
>>> cd ~
SyntaxError: invalid syntax
>>> import sys
>>> print sys.argv[0]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sys.argv[0])?
>>> yes
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
>>> print(sys.argv[0])

>>> 
>>> import os
>>> print(os.getcwd)
<built-in function getcwd>
>>> 
print os.path.abspath
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(os.path.abspath)?
>>> 
print(os.path.abspath)
<function abspath at 0x00000297A7953550>
>>> os.show
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    os.show
AttributeError: module 'os' has no attribute 'show'
>>> os.show()
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    os.show()
AttributeError: module 'os' has no attribute 'show'
>>> os.getenv("windir")
'C:\\Windows'
>>> f_for_r = open('1.txt','r')
>>> f_for_r.read()
Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    f_for_r.read()
UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 13: incomplete multibyte sequence
>>> f_for_r = open('2.txt','r')
>>> f_for_r.read()
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    f_for_r.read()
UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 13: incomplete multibyte sequence
>>> f_for_r = open('2.txt','r',encoding = 'utf-8')
>>> f_for_r.read()
'Hello world！'
>>> f_for_r = open('2.txt','r')
>>> f_for_r.read()
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    f_for_r.read()
UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 13: incomplete multibyte sequence
>>> f_for_r.close()
>>> f_for_w = open('2.txt','w')
>>> f_for_r.write('i love u')
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    f_for_r.write('i love u')
ValueError: I/O operation on closed file.
>>> f_for_r = open('2.txt','w',encoding = 'utf-8')
>>> f_for_w.write('i love u')
8
>>> f_for_w.close()
>>> ffa = open('2.txt','a')
>>> ffa.write('hello world!\n')
13
>>> ffa.close()
>>> with open('2.txt','a')as f:
	f.write('nice!\n')

	
6
>>> import csv
>>> data = {'symbol':[],'data':[],'closing_price':[]}
>>> data = {'symbol':[],'date':[],'closing_price':[]}
>>> 
>>> with open('stocks.csv','r') as f:
	reader = csv.DictReader(f)
	for row in reader:
		data['symbol'].append(row["symbol"])
		data['date'].append(row['date'])
		data['closing_price'].append(float(row["closing_price"]))

		
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    with open('stocks.csv','r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stocks.csv'
>>> with open('stocks.csv','r') as f:
	reader = csv.DictReader(f)
	for row in reader:
		data['symbol'].append(row["symbol"])
		data['date'].append(row['date'])
		data['closing_price'].append(float(row["closing_price"]))

		
>>> data.keys()
dict_keys(['symbol', 'date', 'closing_price'])
>>> data['closing_price']
[647.0, 35.0, 653.0, 678.0, 4365.0, 2.0, 245.435, 245.0, 867.0, 13.0, 345.0, 645.0, 243.0, 64.86, 1423.0, 1512.0, 134.0, 4634.0, 25.0, 745.0]
>>> import pandas
>>> data2 = pandas,read_csv('stocks.csv')
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    data2 = pandas,read_csv('stocks.csv')
NameError: name 'read_csv' is not defined
>>> data2 = pandas.read_csv('stocks.csv')
'
>>> data2 = pandas.read_csv('stocks.csv')
>>> print(len(data2))
20
>>> print(type(data2))
<class 'pandas.core.frame.DataFrame'>
>>> data2
    symbol       date  closing_price
0       wr  2020/3/23        647.000
1       pp  2020/3/24         35.000
2      erw  2020/3/25        653.000
3    dfsad  2020/3/26        678.000
4       fg  2020/3/27       4365.000
5   dsfgsd  2020/3/28          2.000
6      sdf  2020/3/29        245.435
7      sdf  2020/3/30        245.000
8    rytio  2020/3/31        867.000
9     sjrg   2020/4/1         13.000
10   tutys   2020/4/2        345.000
11     ewq   2020/4/3        645.000
12     sgq   2020/4/4        243.000
13     sgf   2020/4/5         64.860
14    dbfg   2020/4/6       1423.000
15     wey   2020/4/7       1512.000
16   tyuje   2020/4/8        134.000
17     sgf   2020/4/9       4634.000
18    tryq  2020/4/10         25.000
19    ryjh  2020/4/11        745.000
>>> data2.iloc[1]
symbol                  pp
date             2020/3/24
closing_price           35
Name: 1, dtype: object
>>> data2.iloc[i]['date']
'2020/3/27'
>>> import nltk
>>> nltk.download('punkt')
[nltk_data] Error loading punkt: <urlopen error [WinError 10054]
[nltk_data]     远程主机强迫关闭了一个现有的连接。>
False
>>> nltk.download('punkt')
[nltk_data] Error loading punkt: <urlopen error [WinError 10054]
[nltk_data]     远程主机强迫关闭了一个现有的连接。>
False
>>> pip install nltk
SyntaxError: invalid syntax
>>> nltk.download('punkt')
IDLE internal error in runcode()
Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 342, in putmessage
    r, w, x = select.select([], [self.sock], [])
TypeError: argument must be an int, or have a fileno() method.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 243, in asyncqueue
    self.putmessage((seq, request))
  File "D:\python\lib\idlelib\rpc.py", line 345, in putmessage
    raise OSError("socket no longer exists")
OSError: socket no longer exists
>>> 1+1
IDLE internal error in runcode()
Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 342, in putmessage
    r, w, x = select.select([], [self.sock], [])
TypeError: argument must be an int, or have a fileno() method.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 243, in asyncqueue
    self.putmessage((seq, request))
  File "D:\python\lib\idlelib\rpc.py", line 345, in putmessage
    raise OSError("socket no longer exists")
OSError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 342, in putmessage
    r, w, x = select.select([], [self.sock], [])
TypeError: argument must be an int, or have a fileno() method.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 243, in asyncqueue
    self.putmessage((seq, request))
  File "D:\python\lib\idlelib\rpc.py", line 345, in putmessage
    raise OSError("socket no longer exists")
OSError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 342, in putmessage
    r, w, x = select.select([], [self.sock], [])
TypeError: argument must be an int, or have a fileno() method.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 243, in asyncqueue
    self.putmessage((seq, request))
  File "D:\python\lib\idlelib\rpc.py", line 345, in putmessage
    raise OSError("socket no longer exists")
OSError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 342, in putmessage
    r, w, x = select.select([], [self.sock], [])
TypeError: argument must be an int, or have a fileno() method.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python\lib\idlelib\rpc.py", line 243, in asyncqueue
    self.putmessage((seq, request))
  File "D:\python\lib\idlelib\rpc.py", line 345, in putmessage
    raise OSError("socket no longer exists")
OSError: socket no longer exists
>>> 