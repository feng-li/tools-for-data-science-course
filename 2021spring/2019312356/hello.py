import math
print("乘方：a**b，加：a+b，减：a-b，乘积：a*b，除：a/b，地板除：a//b，取余:a%b")

n = int(input("请输入一个正整数n代表生成的个数"))
L = []
a = 1
b = 1
c = 0
L.append(a) #列表第一个值为1
L.append(b) #列表第二个值也为1
#c变量代表下一个值 
while len(L) < n:
    c = a + b#计算下一个值
    L.append(c)#存到列表下一个位置
    a = b#让a绑定的对象向后移动一个
    b = c#让b绑定的对象向后移动一个 
print(L)


