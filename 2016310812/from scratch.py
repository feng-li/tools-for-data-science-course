# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:03:30 2019

@author: tutuxy
"""

#3.10
5+2
5-2
5*2
5**2
#??5^2
5/2
5//2#取结果整数部分
5%2#取余数
_+3#??"_"调取上次的结果
tel = dict(Mike = 3759, Mary = 1462, Ning = 6839)
tel
print(tel.keys())
print(tel.values())
list(tel.keys())
sorted(tel.keys())
tel['Mike']
'Mike' in tel
tel['Ada'] = 8080
tel
tel['Ada'] = 8090
tel
del tel['Mary']
tel
if True:
    print('true')
n = 3
if n%2 == 0:
    print(n,'是偶数',sep = '')
elif n%2 == 1:
    print(n,'是奇数',sep = '')
else:
    print(n,'既不是奇数也不是偶数',sep = '')
a = [x**2 for x in range(1,10)]
n = 23
if n in a:
    print(repr(n)+' is a perfect square')
else:
    print(n,'is not a perfect square')
#repr变成字符串
for i in range(3):
    print(i)
list(range(3))
a = {3,2,5,7,9,10,8}
for x in a:
    if x%2 == 0:
        continue
    print(x)
for i in range(5):
    if 2**i <10:
        print(i,2**i)
    else:
        break
a = range(1,101)
sum = 0
for s in a:
    sum = sum+s
print(sum)
a = range(1,6)
factorial = 1
for s in a:
    factorial = factorial*s
print(factorial)

a = input('select a number:')
a
divisors = []
m = [value for value in range(1, int(a)+1)]
list(range(1, int(a)+1))
list(range(1))
for s in m:
    if int(a)%s == 0:
        divisors.append(s)
print(divisors)
        
a = input('select a number:')
divisors = []
m = [value for value in range(1,int(int(a)**(1/2))+1)]
for s in m:
    if int(a)%s == 0:
        divisors.append(s)
divisors.remove(1)
divisors
flag = 'true'
for divisor in divisors:
    if int(a)%divisor == 0:
        flag = 'false'
        break
if flag =='true':
    print(a,' is a prime')
else:
    print(a,' is not a prime')

a = 0
while 2**a <10:
    print(a,2**a)
    a = a+1
a = [1,1]
k = 3
x = input('请输入项数(>=3):')
while k<= int(x):
    b = a[-1]+a[-2]
    a.append(b)
    k = k+1
print(a)
#?for循环不需要加一，while需要
xx = input('select an integer:')
#xx是一个str
x = int(xx)
ans = 0
if x>0:
    while ans*ans < x:
        ans = ans+1
    if ans**2==x:
        print('its square root is '+repr(ans))
    else:
        print('its not a perfect square')
else:
    print('it is not a positive integer')

x = [value for value in range(1,50)]
a=['3k']
a
b=['3k+1']
c=['3k+2']
t=len(x)
t
k=1
while k<=t: #此处需要变量，t不能换为len(x)
    if x[0]%3==0:
         a.insert(0,x[0])
         x.remove(x[0])
    elif  x[0]%3==1:
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



import()

