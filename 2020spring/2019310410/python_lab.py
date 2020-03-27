#!/usr/bin/env python
# coding: utf-8

# ## 复习中感觉生疏的知识点

# + **在Python中，"_"可用于调用上次的结果**

# In[34]:


1+4


# In[35]:


_+1


# + **切片区间是左闭右开的**

# In[36]:


a='gao zhiyu'
a[3:5]


# + **在字符串前加入r，不处理特殊字符**

# In[37]:


print('gzy\nstudent')


# In[38]:


print(r'gzy\nstudent')


# + **用extend方法合并列表,返回值为none**

# In[39]:


import numpy as np


# In[40]:


c=list(range(3,7))
d=list(np.linspace(2,7,2))


# In[41]:


c.extend(d)
c


# + **列表的值传递与址传递**

# In[42]:


c1=c
c2=c[:]
c3=c.copy()
c1,c2,c3


# In[43]:


c1.append(7)


# In[44]:


print([c1,c2,c3])#c1与a同步变化，说明c1=a为地址传递，而c2，c3为值传递


# + **集合运算**

# In[45]:


a={'a','b',1,4,5}
b={'b','c',2,5}


# In[46]:


a|b #取并集


# In[47]:


a&b #取交集


# In[48]:


a^b #取a和b的异或，a^b=a|b-a&b


# + **集合的建立**

# set expected at most 1 arguments

# In[49]:


x=set('12345')
x


# 上述方法数字的类型是str而不是int，我感觉不是个很好的方法

# + **字典的构建**

# 将一个由键与值构成的元组对序列用dict函数变为字典

# In[50]:


dict_=dict([('gzy',88),('zjj',77),('xyf',66)])
dict_


# + **匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数，后面只能有一个表达式，不用写return，返回值就是该表达式的结果**

# In[51]:


f=lambda x:x**2


# In[52]:


f(2)


# + **functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单**

# In[53]:


import functools


# In[54]:


get_ipython().set_next_input('int2=functools.partial');get_ipython().run_line_magic('pinfo', 'functools.partial')


# In[ ]:


int2=functools.partial


# In[55]:


int2=functools.partial


# In[56]:


int2=functools.partial(int,base=2)


# In[57]:


int2('100')


# + **filter(函数，序列)：把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素**

# filter(函数，序列)：把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# Init signature: filter(self, /, *args, **kwargs)
# 
# Docstring:  filter(function or None, iterable) --> filter object
# 
# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.

# In[58]:


list(filter(lambda x:x%2==1,list(range(9))))


# ### 高阶函数

# 变量可以指向函数,函数名也是变量,一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

# + **map(函数,可迭代序列)作为高阶函数，将传入的函数依次作用到序列的每个元素，并把结果作为新的迭代器返回**

# In[59]:


list(map(str,list(range(9))))


# + **functools的reduce作用于高阶函数，其效果是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4) (f必须接收两个参数)**

# Docstring:
# reduce(function, sequence[, initial]) -> value
# 
# Apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
# ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
# of the sequence in the calculation, and serves as a default when the
# sequence is empty.
# 
# Type:builtin_function_or_method

# In[60]:


from functools import reduce


# In[61]:


def multiply(L):
    return reduce(lambda x,y:x*y,L)


# In[63]:


multiply(range(1,5))


# ***

# + **sorted函数的key参数**

# A custom key function can be supplied to customize the sort order, and the
# reverse flag can be set to request the result in descending order\

# In[64]:


print(sorted([12,34,6,-13],key=abs))


# 如果要倒序排列，参数加上**reverse=True**
