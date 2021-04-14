#!/usr/bin/env python
# coding: utf-8
'''法1：迭代法，写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O（1.618^n）,而且最深度1000 '''
# In[22]:


def fibonacci(n):
    
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
re=[]
x=int(input("请输入需要的斐波那契数的项数："))
for i in range(1,x+1):
    re.append(fibonacci(i))
print(re)

'''法2：递推法，就是递增法，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢'''
# In[11]:


def fibonacci2(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
    return a
re2=[]
x=int(input("请输入需要的斐波那契数的项数："))
for i in range(1,x+1):
    re2.append(fibonacci2(i))
print(re2)

'''法3(网络方法，并不十分懂)：带有yield的函数都被看成生成器，生成器是可迭代对象，
且具备__iter__和 __next__方法， 可以遍历获取元素, python要求迭代器本身也是可迭代的，
所以我们还要为迭代器实现__iter__方法，而__iter__方法要返回一个迭代器，
迭代器自身正是一个迭代器，所以迭代器的__iter__方法返回自身即可，速度快'''
# In[18]:


#生成100个斐波那契数，也可以生成自定义个
def fib_yield_while(max):
      a, b = 0, 1
      while max > 0:
        a, b = b, a+b
        max -= 1
        yield a
        
def fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

re3=[]
for i in fib_yield_for(100):
    re3.append(i)
print(re3)

'''法4：（网络方法）类实现内部魔法方法'''
# In[29]:


#生成500个斐波那契数，也可以生成自定义个

class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self

re4=[]
if __name__ == '__main__':
    fib = Fibonacci(500)
    for num in fib:
        re4.append(num)
print(re4)
       # print(num)

'''法5：矩阵（并不十分懂）'''
# In[28]:


import numpy as np

### 1

def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        
        print(int(res[0][0]))

# 调用
fib_matrix(20)
#fib_matrix(20)

### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list


    

# 调用
Fibonacci_Matrix(50)

### pow 速度 比 双**号快, np.linalg.matrix_power也是一种方法

