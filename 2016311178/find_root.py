def qua():
    """
    find the roots of a random equation
    """

    import math
    import random
    a = random.randint(1,100)
    b = random.randint(-100,100)
    c = random.randint(-100,100)
    print("a=",a,"b=",b,"c=",c) #生成随机数a,b,c
    
    delta= b**2 - 4*a*c
    if a == 0:
        print("方程不是一元二次方程")
    else:
        if delta < 0:
            print("方程无实数根")
        elif delta == 0:
            x = -b/2*a
            print("方程只有同一个实数根，为",x)
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("方程有两个不同根，分别为x1=",x1,"x2=",x2)
