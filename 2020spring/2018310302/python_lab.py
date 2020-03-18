def test1():
    #numpy（Numerical Python）  python对多为数组对象的支持
    import numpy as np
    A=np.array([[1,2],[3,4]])
    print(A)
    print(A.T)#求矩阵转置

    #Scipy（Scientific Python）  可以利用numpy做更高级的数学，信号处理，优化，统计等
    from scipy import linalg
    B=linalg.inv(A) #求矩阵的逆
    print(B)
    print(A.dot(B)) #求矩阵的逆

#----------------------------------------------------------------------
def test2():
    #固定住原函数的部分参数，从而调用起来更加方便
    import functools
    int2=functools.partial(int,base=2) # 相当于 int('1000000',base = 2)，即默认二进制转换为十进制
    print(int2('1000000'))

#-----------------------------------------------------------------------
def triangles(n):
    #如果一个函数定义中包含 yield 关键字，
    #那么这个函数就不再是一个普通函数，而是一个 generator, 可通过 for 循环来迭代它
    L=[1]
    for x in range(n):
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
def test3():
    for x in triangles(10):
        print(x)

#-----------------------------------------------------------------------
def add(x,y,f):
    #高阶函数，将函数名作为变量传给另一个函数作为参数，这个函数就称为高阶函数
    return f(x)+f(y)
def test4():
    print(add(-5,-6,abs))

#-----------------------------------------------------------------------
def test5():
    #map(函数, 可迭代序列)作为高阶函数，将传入的函数依次作用到序列的每个元素，把结果作为新的迭代器返回
    print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#------------------------------------------------------------------------
from functools import reduce
def prod(L):
    # 求 list 中所有数的乘积
    return reduce(lambda x, y: x * y, L )
def test6():
    print(prod([3, 5, 7, 9]))

#-------------------------------------------------------------------------
#Nested List Comprehensions （内嵌列表推导式）
def test7():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    b=[[row[i] for row in matrix] for i in range(4)]
    c=list(zip(*matrix))
    print(b)  #这里会输出列表的列表
    print(c)  #这里会输出元组的列表
