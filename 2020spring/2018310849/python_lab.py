#!/usr/bin/env python
# coding: utf-8

# ## 基本运算

# In[4]:


5**2


# In[5]:


5/2#实数


# In[7]:


5//2


# In[8]:


5%2


# In[9]:


_+3


# ## 数据类型

# ### 字符串

# In[10]:


a="Li Feng"
a


# In[11]:


type(a)


# In[12]:


length(a)


# In[13]:


len(a)


# In[14]:


a="Li Feng"
a[1]#索引从0开始


# In[15]:


a[-2]


# In[16]:


a[3:5]#不包括最后一个


# In[17]:


a[3:100]


# In[18]:


a[3:]


# In[19]:


"Li"+" "*3 +"Feng"


# In[20]:


'6'*3


# In[21]:


print("Li Feng")


# In[22]:


print("Hello \n World!")  #'\n'为特殊字符，表示换行


# In[23]:


print(r"Hello \n World!")  #加入r，不处理为特殊字符


# ## 列表 

# In[24]:


a=[1,2,3]


# In[25]:


type(a)


# In[26]:


a[0]


# In[27]:


a.append(4)


# In[28]:


a


# In[29]:


a.insert(2,'a')#把元素插入到指定的位置


# In[30]:


a


# In[31]:


a.remove('a')  #移除列表中第一个指定元素
a


# In[32]:


b = [4,5,6]
a.extend(b)  #将两个列表合并
a


# In[33]:


a.remove(4)  
a


# In[34]:


del a[5]  #移除指定位置上的元素
a


# In[35]:


a.pop()  #移除list中的最后一个元素，并且返回该元素的值。


# In[36]:


a


# In[37]:


a.pop(2)  #移除指定位置元素，并返回该元素的值


# In[38]:


a = [1,3,2,3]
a


# In[39]:


a.sort()  #按从小到大顺序排列
a


# In[40]:


a.reverse()  #将列表顺序颠倒
a


# In[41]:


a.count(3)  #计算列表中指定元素的个数


# In[42]:


a.index(3)  #求列表中第一个指定元素的索引


# #### 列表的值传递与址传递：

# In[43]:


c1 = a
c2 = a[:]
c3 = a.copy()
c1,c2,c3


# In[44]:


a.append(4)
a


# In[45]:


[c1,c2,c3]  #c1与a同步变化，说明c1=a为地址传递，而c2，c3为值传递


# 列表的嵌套使用：

# In[46]:


matrix = [[1, 2, 3, 4],[5, 6, 7, 8, 9],[ 10, 11, 12]]
type(matrix)


# In[47]:


matrix[1][2]#第2个列表的第三个元素


# range经常无法使用某些方法，可以转成list进行操作：

# In[49]:


list(range(1,6,2))


# 列表生成式:把要生成的元素放到前面，后面跟for

# In[50]:


[x * x for x in range(1, 11)]


# In[51]:


[m + n for m in 'ABC' for n in 'XYZ']


# ### 集合

# In[52]:


a = {1,2,2,'a','a','bc'}  #集合中元素不能重复
a


# In[53]:


type(a)#set是集合


# In[54]:


'a' in a  #用in判断是否在a中，返回true 或 false


# In[55]:


b = {1,3,'b','c'}
b


# In[56]:


a | b #求集合的并


# In[57]:


a & b  #求集合的交


# In[58]:


a - b  #求集合的差，a-b表示在a中，不在b中的元素的集合


# In[59]:


a ^ b   #求两集合的异或，a^b=(a | b)-(a & b)


# In[60]:


a = set('122abb')
a


# ### 元组

# In[61]:


a = 1,'a','b'   #元组由逗号分隔的多个值组成


# In[62]:


a


# In[63]:


type(a)


# In[71]:


b= [1,'c']
c = a,b  #元组中可以嵌套不同类型的数据
c


# In[72]:


c[0]


# In[73]:


c[1][1]


# 元组是不可变的，但是它们可以包含可变对象。

# In[74]:


c[0] = 1


# In[75]:


c[1][1]=2
c#列表可以变


# ### 字典

# In[76]:


tel = {'Mike':3759, 'Mary':1462, 'Ning':6839}
print(tel)
type(tel)


# In[77]:


tel = dict(Mike = 3759, Mary = 1462, Ning = 6839)
tel#字典的两种写法


# In[78]:


tel = dict([('Mike',3759),('Mary',1462),('Ning',6839)])
#将一个由关键字与值构成的元组对序列变成字典
tel


# In[79]:


print(tel.keys())
print(tel.values())  #分别访问关键字与值


# In[80]:


list(tel.keys())


# In[81]:


sorted(tel.keys())  #排序


# In[82]:


tel['Mike']


# In[83]:


tel['Ada'] = 8080  #添加元素
tel


# In[84]:


del tel['Mary']  #删除指定元素
tel


# ## 基本语句

# ### 条件语句

# In[85]:


if True:
    print('True')  #基本语法


# In[86]:


n = 3  #判断奇偶性
if n % 2 == 0:
    print(n,'是偶数',sep = '')
elif n % 2 == 1:
    print(n,'是奇数',sep = '')
else:
    print(n,'既不是奇数也不是偶数',sep = '')


# In[87]:


#判断一个100以内的数是否为完全平方数
a=[x**2 for x in range(1,10)]
n=23
if n in a :
    print(repr(n)+' is a perfect square') 
    #n是一个int，不可以直接用加号连上字符串，可通过repr()函数将其变为字符串
else:
    print(n,' is not a perfect square')


# ### for循环

# In[88]:


for i in range(3):
    print(i)


# In[89]:


a = {3,2,5,7,9,10,8}
for x in a:
    if x % 2 == 0:
        continue
    print(x)


# In[90]:


for i in range(5):                  
    if 2 ** i < 10:
        print(i,2 ** i)
    else:
        break


# In[91]:


a=range(1,101)  
sum=0
for s in a:
    sum=sum+s
print(sum)


# In[92]:


a=range(1,6)
factorial=1
for s in a :
    factorial=factorial*s
print(factorial)


# In[93]:


a=input('Select a number :')#求所有因子
divisors=[]
m=[value for value in range (1,int(a)+1)]
for s in m:
    if int(a)%s==0:
        divisors.append(s)
print(divisors)#find the set of divisors of a specific a given by users


# In[94]:


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


# ### while 循环

# In[95]:


a = 0
while 2 ** a < 10:
    print(a,2 ** a)
    a = a + 1


# In[96]:


a=[1,1]#斐波那契数列
k=3
x=input('请输入项数(≥3)：')
while k<=int(x):
    b=a[-1]+a[-2]
    a.append(b)
    k=k+1
print(a)


# In[97]:


xx=input('Select an integer:')#求平方根
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


# 用while 配合 k的计数器，进行数的分组操作

# In[98]:


x=[value for value in range(1,50)]
a=['3k']
b=['3k+1']
c=['3k+2']
t=len(x)
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


# ## 导入模块及函数

# In[99]:


import math


# In[100]:


math.exp(0)


# In[101]:


import math as mt
mt.exp(0)


# In[102]:


from math import exp 
exp(0) 


# In[103]:


from math import exp as myexp 
myexp(0)


# numpy（Numerical Python）提供了python对多维数组对象的支持

# In[104]:


import numpy as np
A = np.array([[1,2],[3,4]])
A


# In[105]:


A.T  #求矩阵转置


# Scipy（Scientific Python）:可以利用numpy做更高级的数学，信号处理，优化，统计等

# In[106]:


from scipy import linalg
B = linalg.inv(A) # 求矩阵的逆
B


# In[107]:


A.dot(B)   #矩阵乘法,不是点点对应


# matplotlib：一个 Python 的 2D绘图库

# In[108]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,4,6,2,4,8]

plt.plot(x, y)


# ## 函数

# ### 自定义函数

# In[109]:


def parity(n):
    """To judge whether an integer is odd or even."""      # the function help
    if n % 2 == 0:
        print(n,'是偶数',sep = '')
    elif n % 2 == 1:
        print(n,'是奇数',sep = '')
    else:
        print(n,'既不是奇数也不是偶数',sep = '')


# 匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数，后面只能有一个表达式，不用写return，返回值就是该表达式的结果。

# In[110]:


f = lambda x: x ** 2
f(2)


# In[111]:


def make_incrementor(n):
    return lambda x: x + n  #返回一个函数


# In[112]:


f = make_incrementor(42)


# In[113]:


f(0),f(1)


# 汉诺塔问题：定义一个函数，接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

# In[114]:


def move(n, a, b, c):
    if n == 1:
            print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


# functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单

# In[115]:


import functools
int2 = functools.partial(int, base=2)
int2('1000000')     #相当于int('1000000',base = 2)，即默认二进制转换为十进制


# ### 生成器(generator)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator,可通过for循环来迭代它

# In[116]:


def triangles(n):    #杨辉三角
    L = [1]
    for x in range(n):
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
for x in triangles(10):     
    print(x)


# ### 高阶函数

# 变量可以指向函数,函数名也是变量,一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

# In[117]:


def add(x, y, f):
    return f(x) + f(y)
add(-5, 6, abs)


# map(函数,可迭代序列)作为高阶函数，将传入的函数依次作用到序列的每个元素，并把结果作为新的迭代器返回。

# In[118]:


list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# In[119]:


def normalize(name):  #将名字中的字母大小写规范化
    name = name.lower()
    name = name.capitalize()
    return name


# reduce作为高阶函数，其效果是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4) (f必须接收两个参数)

# In[120]:


from functools import reduce
def prod(L):  #求list中所有数的乘积
    return reduce(lambda x, y: x * y, L )


# In[121]:


prod([3, 5, 7, 9])


# filter(函数，序列)：把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# In[122]:


list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15]))  #返回list中的奇数


# sorted(序列，keys)：按照keys中函数作用后的结果进行排序，并按照对应关系返回list相应的元素

# In[124]:


sorted([36, 5, -12, 9, -21], key=abs)


# In[125]:


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=lambda x: x[0]))  #按名字
print(sorted(students, key=lambda x: x[1]))  #按成绩从低到高
print(sorted(students, key=lambda x: x[1], reverse=True))  #按成绩从高到低


# ## Python的类

# 面向对象的程序设计思想，是把对象作为程序的基本单元：类是抽象的模板，实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# In[1]:


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'


# In[2]:


MyClass()
MyClass.i  #引用属性
MyClass.f


# In[3]:


MyClass.i  #引用属性


# In[4]:


MyClass.f


# In[5]:


MyClass.i = 3  #更改属性值
MyClass.i


# In[6]:


MyClass.x = 1  #根据需要添加定义中没有的属性
MyClass.x


# 在创建实例的时候，定义一个特殊的init方法，把一些我们认为必须绑定的属性强制填写进去，可以起到模板的作用。

# In[7]:


class Complex:
    def __init__(self, realpart, imagpart):  
        self.r = realpart
        self.i = imagpart


# In[8]:


x = Complex(3.0, -4.5)
x.r, x.i


# ## 读取文件

# ### txt

# In[9]:


file_for_reading = open('test.txt', 'r')  #‘r’表示read


# In[10]:


file_for_reading.read()


# In[11]:


file_for_reading.close()


# In[12]:


file_for_writing = open('test.txt', 'w')  #‘w’表示write


# In[13]:


file_for_appending = open('test.txt','a') #‘a’表示append


# In[14]:


file_for_appending.close()


# 由于close()很容易忘记，故推荐采用with语句，在语句执行完毕后自动关闭：

# In[15]:


with open('test.txt','a') as file:
    file.write('Nice to meet you! \n')


# ### csv

# 也可使用pandas包中的read_csv()函数读取csv文件

# ## 文本处理

# In[16]:


import nltk


# In[17]:


nltk.download('punkt')


# In[18]:


nltk.download('punkt')


# In[19]:


import nltk


# In[20]:


nltk.download('punkt')


# In[21]:


nltk.download('punkt')


# In[22]:


import nltk


# In[23]:


nltk.download('punkt')


# In[24]:


nltk.download('punkt')


# In[25]:


para = "Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java."


# In[26]:


from nltk.tokenize import sent_tokenize 
sent_tokenize(para)


# In[27]:


from nltk.tokenize import word_tokenize
word_tokenize(para)


# In[28]:


nltk.download('stopwords')


# In[29]:


from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
print(english_stops)  #输出stopwords


# In[30]:


from nltk.tokenize import RegexpTokenizer 
tokenizer = RegexpTokenizer("[\w']+") 
words = tokenizer.tokenize("Smoking is now banned in many places of work.") 
words


# In[31]:


[word for word in words if word not in english_stops]


# In[32]:


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmer.stem('cooking')


# In[ ]:




