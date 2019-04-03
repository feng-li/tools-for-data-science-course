#%%
def sol_equ(a,b,c):
    """
    Solve a*x^2+b*x+c=0
    list a,b,c 
    
    Usage
    
         sol_equ(a,b,c)
    """
    import math
    n = len(a)
    i=0
    while i<n:
        if b[i]**2-4*a[i]*c[i] >= 0:
            x1 = (-b[i]+math.sqrt(b[i]**2-4*a[i]*c[i]))/(2*a[i])
            x2 = (-b[i]-math.sqrt(b[i]**2-4*a[i]*c[i]))/(2*a[i])
            print("第"+repr(i+1)+"个方程存在实根,为：x1=" + repr(x1) + ",x2=" + repr(x2))
        else:
            print("第"+repr(i+1)+"个方程不存在实根")
        i=i+1
        
#%%
#test sol_equ
a = list([1,1,3,4,5,6,2,8,9,1])
b = list([5,-2,9,8,7,4,3,2,1,9])
c = list([1,1,6,9,8,4,1,2,5,2])
sol_equ(a,b,c)
