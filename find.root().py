import math
a = [1,2,3,4,5,6,7,8,9,10]
b = [3,4,5,6,7,8,9,10,11,12]
c = [-4,-3,-2,-1,0,1,2,3,4,5]
def find.root(a,b,c):
    p=b*b-4*a*c
    if p>=0 and a!=0:
        x1 = (-b+math.sqrt(p))/(2*a)
        x2 = (-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif a==0:
        x1=x2=-c/b
        return x1
    else:
        return("this is a wrong number")

for i in a:
    for j in b:
        for k in c:
            print(quad(i,j,k))
