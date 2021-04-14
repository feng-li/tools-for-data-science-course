def equsol():
    """
    find the solution of a random equation
    """
    
    import random
    import math
    al = random.sample(range(1,100),10)
    bl = random.sample(range(1,100),10)
    cl = random.sample(range(1,100),10)
    print("al=",al,"bl=",bl,"cl=",cl)   #将a,b,c的是个随机数列出来
#random.randint(1,100) 生成一个
    for a in al:
        for b in bl:
            for c in cl:
                print("a=",a,"b=",b,"c=",c)
                derta = b**2-4*a*c
                x = -b/2*a
                if derta < 0:
                    print("方程没有实数根")
                elif derta ==0:
                    print("方程有一个实数根，根为" + repr(x))
                else:
                    x1 = x + math.sqrt(derta)
                    x2 = x - math.sqrt(derta)
                    print("方程有两个实数根，分别为" + repr(x1) +'、' + repr(x2))



	
