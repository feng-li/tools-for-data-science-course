import math
def my_quadratic(a,b,c):
    if not isinstance(a,(int,float)):  #判断是否是已知类型，对象类型与元组中类型名之一相同即返回True。
        raise TypeError('a is not a number,please try again')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number,please try again')
    if not isinstance(c,(int,float)):
        raise TypeError('b is not a number,please try again')
    d = b*b - 4*a*c
    if d < 0:
        return 'b*b-4*a*c= ',d,'<0,方程无解'
    else:
        if a == 0:
            if b == 0:
                if c == 0:
                    return '方程解为全体实数'
                else:
                    return '方程无解'
            else:
                x1 = -c/b
                x2 = x1
                return x1,x2
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            return x1,x2

print(my_quadratic(2,3,1))  #   (-0.5, -1.0)
print(my_quadratic(1,3,-4)) #   (1.0, -4.0)
print(my_quadratic(2,2,5))  #   ('b*b-4*a*c= ', -36, '<0,方程无解')
