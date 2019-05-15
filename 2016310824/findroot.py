#找二次方程的根
def rt(a,b,c):
    import math
    if a == 0:
        print('a值不能为0')
        
    elif a!= 0:
        delta = b**2 - 4*a*c
        
        if delta < 0:
            print(a,"x^2+",b,"x+c=0","没有根",sep='')
            
        elif delta > 0:
            x1 = (-b+math.sqrt(delta))/2*a
            x2 =(-b-math.sqrt(delta))/2*a
            print(a,"x^2+",b,"x+c=0","有两个根,x1 =", x1 , ",  x2 = " ,x2,sep='')       #输出方式
            
        elif delta == 0:
            x = -b/2*a
            print(a,"x^2+",b,"x+c=0","有一个根,x =" ,x,sep='' )

rt(0,2,1)

import random
n = 10
a = np.array([random.randint(1,10) for i in range(n)])
b = np.array([random.randint(1,10) for i in range(n)])
c = np.array([random.randint(1,10) for i in range(n)])

for i in range(10):
    rt(a[i],b[i],c[i])