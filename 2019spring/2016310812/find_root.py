import math
def find_root(a,b,c):
    x = [0,0]
    delta = b**2-4*a*c
    if delta<0:
        print("输入有误,方程没有实数解")
    elif a==0:
        if b==0:
            if c!=0:
                print("输入有误，方程不成立")
            else:
                print("x有无数解")
        else:
            x= -c/b
            print("解为"+repr(x))
    else:
        x[0] = (-b+math.sqrt(delta))/2/a
        x[1] = (-b-math.sqrt(delta))/2/a
        print("解为"+repr(x[0])+"和"+repr(x[1]))