# 数学计算
1.0 / 3        
5.0 / 2.0
2**3
from math import sin
import math as m
m.cos(6)
m.ceil(2.9)
m.factorial(4)
m.sqrt(9.0)
m.pow(4, 1.0 / 2) 

# Leap Year Check
year=int(input("please input the year:"))
if year%4==0:
    if year%100!=0:
        print("True")
    elif year%400==0:
        print("True")
    else:
        print("False")
else:
    print("False")
