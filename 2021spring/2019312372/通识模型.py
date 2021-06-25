import sympy as sp
import numpy as np
print("数学简单求导积分模型")
print("A：求导，B:积分,Q:退出  :",end="")
while(True):
    q=input()
    if  q=='A':     
        print("依次输入三元二次函数的系数值(x,y 空格分隔）")
        print("例如,1 2 3 4 5 6 7 8 9 10,f=x^3+2x^2+3x+4y^3+5y^2+6y+7xy+8xy^2+9x^2y+10")
        j=input("输入系数：").split()
        i=[]
        for n in range(10):
            i.append(eval(j[n]))
        a=i[0];b=i[1];c=i[2];aa=i[3];bb=i[4];cc=i[5];e=i[6];ee=i[7];d=i[8];dd=i[9]
        x,y=sp.symbols('x y')
        f=a*x**3+b*x**2+c*x+aa*y**3+bb*y**2+cc*y+e*x*y+ee*x*y**2+d*y*x**2+dd
        print("原函数:",f)
        fx=sp.diff(f,x)
        fy=sp.diff(f,y)
        print("对x求一次偏导:",fx)
        print("对y求一次偏导:",fy)
        if fx!=0 or fy!=0:
            f2x=fx
            f2y=fy
            fxy=fx
            fxy=sp.diff(fxy,y)
            fx2=sp.diff(f2x,x)
            fy2=sp.diff(f2y,y)
            print("对xy求一次偏导:",fxy)
            print("对x求二次偏导:",fx2)
            print("对y求二次偏导:",fy2)
        if fxy!=0 or fx2!=0 or fy2!=0:
            f3x=fx2
            f3y=fy2
            f2xy=fxy
            fx22y=fxy
            fx2y=sp.diff(f2xy,y)
            fxy2=sp.diff(fx22y,y)
            fx3=sp.diff(f3x,x)
            fy3=sp.diff(f3y,y)
            print("对x^2y求一次偏导:",fx2y)
            print("对xy^2求一次偏导:",fxy2)
            print("对x求三次偏导:",fx3)
            print("对y求三次偏导:",fy3)
    elif q=='B':
        print("依次输入三元二次函数的系数值(x,y 空格分隔）")
        print("例如,1 2 3 4 5 6 7 8 9 10,f=x^3+2x^2+3x+4y^3+5y^2+6y+7xy+8xy^2+9x^2y+10")
        j=input("输入系数：").split()
        i=[]
        for n in range(10):
            i.append(eval(j[n]))
        a=i[0];b=i[1];c=i[2];aa=i[3];bb=i[4];cc=i[5];e=i[6];ee=i[7];d=i[8];dd=i[9]
        x,y=sp.symbols('x y')
        f=a*x**3+b*x**2+c*x+aa*y**3+bb*y**2+cc*y+e*x*y+ee*x*y**2+d*y*x**2+dd
        print("原函数:",f)
        fx=sp.integrate(f,x)
        fy=sp.integrate(f,y)
        print("对x求一次积分:",fx)
        print("对y求一次积分:",fy)
        
    elif q=='Q':
        print("退出！！")
        break
    print("程序运行完毕请再次选择!!!") 
    print("A：求导，B:积分,Q:退出  :",end="")
