#!/usr/bin/env python
# coding: utf-8

# # python homework                                                              
# ##  by:2017310894

# In[1]:


5 ** 2


# In[2]:


5 // 2


# In[3]:


5 / 2


# In[4]:


5 % 2


# In[8]:


_ + 12


# In[7]:


m = "luofeng"


# In[11]:


type(m)


# In[12]:


a[0]


# In[13]:


m[0]


# In[14]:


m[2:]


# In[15]:


"5" * 4


# In[16]:


print("Hello \n world")


# In[18]:


print(r"Hello \n world")


# In[19]:


a = [1,2,3,4]


# In[20]:


a.append(9)


# In[21]:


a.insert(2,"mid")
a


# In[22]:


a.remove(2)
a


# In[24]:


b=[6,7,8]
a.append(b)
a


# In[25]:


a=[1,2,3,4,5]
a.extend(b)
a


# In[27]:


del a[7]
a


# In[28]:


a.pop(6)
a


# In[31]:


a.reverse()
a


# In[32]:


a.count(4)


# In[33]:


a.index(5)


# ###  列表的值传递和址传递

# In[34]:


c1 = a
c2 = a[:]
c3 = a.copy()
c1, c2, c3


# In[35]:


a.reverse()
a.append(7)
c1, c2, c3


# In[36]:


range(1,10,2)


# In[38]:


list(range(1,10,2))


# 列表生成！！

# In[39]:


[x * x for x in range(1, 20, 4)]

[m + n for m in  "QWE" for n in "ASD"]


# In[40]:


[x * x for x in range(1, 20, 4)]


# In[41]:


a = {"111", 5, "wudi", "这个课程真挺需要时间的", 110}
a


# In[42]:


type(a)


# In[43]:


"b" in a


# In[45]:


b = {1, 2, 3, 4, 5}
a | b
a & b


# In[46]:


a - b


# In[49]:


a ^ b     # =(a | b)-(a & b)


# In[50]:


a= 1,"a","b"


# In[51]:


a


# In[56]:


b=[1,"c"]
c=a,b
c


# In[57]:


c[1]


# In[59]:


c[0][2]


# In[63]:


c[1][1] = 2         #元组内元素不可变   所以第一个报错， 但是第二个列表可以
c


# In[64]:


tel = dict(Mike = 110, Mary = 119, Ning = 120)
tel


# In[65]:


tel = dict([('Mike',110),('Mary',119),('Ning',120)]) #将一个由关键字与值构成的元组对序列变成字典
tel


# In[66]:


print(tel.keys())
print(tel.values())


# In[67]:


list(tel.keys())


# In[68]:


sorted(tel.keys())


# In[69]:


tel['Mike']


# In[70]:


"Mike" in tel


# In[71]:


tel["luofeng"] = 666


# In[72]:


tel


# In[73]:


del tel["Mike"]
tel


# In[74]:


if True:
    print('True')  #基本语法    


# In[75]:


year = 2020
if year % 4 == 0:
    print("这是闰年")
else :
    print("可惜了，这不是闰年~")


# In[76]:


#判断一个100以内的数是否为完全平方数
a=[x**2 for x in range(1,10)]
n=23
if n in a :
    print(repr(n)+' is a perfect square') #n是一个int，不可以直接用加号连上字符串，可通过repr()函数将其变为字符串
else:
    print(n,' is not a perfect square')


# In[77]:


for i in range(66):
    print(i)


# In[78]:


a = {3,2,5,7,9,10,8}
for x in a:
    if x % 2 == 0:
        continue
    print(x)


# In[79]:


for i in range(5):
    if i < 4:
        print(i,i**2)                       #break
    else:
        break


# In[80]:


sum(a=range(1,101))


# In[81]:


a=range(1,101)  
sum=0
for s in a:
    sum=sum+s
print(sum)


# In[82]:


a=range(1,6)
b=1
for s in a :
    b=b*s
print(b)


# In[83]:


##进一步的我们可以判断一个数是否为素数
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
    


# # while 循环

# In[84]:


a = 0
while 2 ** a < 10:
    print(a,2 ** a)
    a = a + 1


# 求一个数的完全平方根

# In[86]:


xx=input('Select an integer:')
x=int(xx)                    #注意xx是一个str，要进行运算必须转成int
ans=0
if  x>0:
    while ans*ans<x:
        ans=ans+1
    if ans**2==x:
        print('Its square root is '+ repr(ans))
    else:
        print('Its not a perfect square ')#来自用户的输入可能并不是完全平方数，要考虑并返回一个相应的提示
else:
    print('It is not a positive integer')


# In[87]:


import math
math.exp(2)


# In[88]:


import math as mt
mt.exp(3)


# In[89]:


from math import exp
exp(4)


# In[90]:


from math import exp as myexp 
myexp(0)


# In[91]:


import numpy as np
A = np.array([[1,2],[3,4]])
A


# matplotlib：一个 Python 的 2D绘图库

# In[92]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,4,6,2,4,8]

plt.plot(x, y)


# 自定义函数

# In[98]:


def happy():
    xx = input("input a number")
    x = int(xx)
    if x % 2 == 0:
        print(x,"是偶数",sep = " ")
    elif x % 2 == 1:
        print(x,"是奇数",sep  = " ")
    else :
        print("Bad number")
    


# In[95]:


help(happy)


# In[96]:


happy()


# In[99]:


happy()


# 匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数，后面只能有一个表达式，不用写return，返回值就是该表达式的结果。

# In[101]:


f = lambda x: x ** 2
f(2)


# In[102]:


def make_incrementor(n):
    return lambda x: x + n  #返回一个函数


# In[103]:


f = make_incrementor(42)
f(0)


# In[ ]:




