# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

 a=range(50) 
sum=0 
for x in a:
    sum=sum+x 
print(sum)
x=[value for value in range(1,50)]
a=['3k']
b=['3k+1']
c=['3k+2']
t=len(x)
k=1
while k<=t: #此处需要变量，t不能换为len(x)
    if x[0]%3==0:
         a.insert(0,x[0])
    elif  x[0]%3==1:
         b.insert(0,x[0])
    else:
         c.insert(0,x[0])
    k=k+1

else:
    print(a)
    print(b)
    print(c)
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,4,6,2,4,8]

plt.plot(x, y)
