print("1000内的斐波那契数乘积")
L = []
a = 1
b = 1
c = 0
L.append(a) #列表第一个值为1
L.append(b) #列表第二个值也为1
#c变量代表下一个值 
while len(L) < 1000:
    c=a+b
    L.append(c)
    a=b
    b=c
    
for i in range(1000):
    temp=1
    temp=L[i]*temp
    print(temp)
   
