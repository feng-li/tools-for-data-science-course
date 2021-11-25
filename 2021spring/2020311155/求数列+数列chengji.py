# -*- coding = utf-8 -*-
# @Time :2021/4/6 9:38 pm
# @Author : Lily
# @File :求数列+数列乘积.py
# @Mac :PyCharm
'''
import numpy
a=numpy.mat([1,1],
            (1,0))
n=int(input("请输入一个数"))
F0=0
F1=1
if n%2==0: 不会写了
'''
n=int(input("请输入一个数"))
import math
def F():
    m=math.sqrt(5)
    result=1/m*(((1+m)/2)**n-((1-m)/2)**n)
    print(result)

