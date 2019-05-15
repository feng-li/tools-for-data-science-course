def mfindroot(a,b,c):
    """
    formula of roots of a quadric equation
    ax^2 + bx +c = 0
    """
    import math
    import pandas
    x1 = [0]*len(a)
    x2 = [0]*len(a)
    for i in range(len(a)):
        if a[i] == 0:
            x1[i] = "Not quadric"
            x2[i] = x1[i]
        else:
            delta = b[i]**2 - 4*a[i]*c[i]
            if delta < 0:
                x1[i] = "No roots"
                x2[i] = x1[i]
            elif delta == 0:
                x1[i] = -b[i]/(2*a[i])
                x2[i] = x1[i]
            else:
                x1[i] = (-b[i] + math.sqrt(delta))/(a[i]*2)
                x2[i] = (-b[i] - math.sqrt(delta))/(a[i]*2)
    x = {"x1":x1,"x2":x2}
    x = pandas.DataFrame(x)
    print(x)

#输入非二次方程、无解、一解、两解检验
a = [0,1,1,1]
b = [2,2,2,3]
c = [1,6,1,1]
mfindroot(a,b,c)

                 
            
            
            
            

