def find_root(a,b,c):
    #判断方程是否有解
    delta_2=b**2-4*a*c
    if delta_2<0:
       print("由如下参数构成的一元二次方程无解：\n","a=",a,"\nb=",b,"\nc=",c)
    elif delta_2==0:
        print("由如下参数构成的一元二次方程有一解：\n","a=",a,"\nb=",b,"\nc=",c)
    else:
        print("由如下参数构成的一元二次方程有两解：\n","a=",a,"\nb=",b,"\nc=",c)
#随机生成三十个数字
import random as r
A=[r.random() for _ in range(10)]
B=[r.random() for _ in range(10)]
C=[r.random() for _ in range(10)]
for i in range(10):
    find_root(A[i],B[i],C[i])
#考虑输入的维度不同，数字类型，a=0

    
