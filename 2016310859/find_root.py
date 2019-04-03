from math import  sqrt

def find_root(A, B, C):
    for i in range(len(A)):
        a, b, c = A[i], B[i], C[i]
        delta = b**2 - 4*a*c
        if delta < 0:
            print(a,'X^2+',b,'X+',c,'=0','无实数解')
        elif delta == 0:
            print(a,'X^2+',b,'X+',c,'=0','有一个解：', -b/(2*a))
        else:
            print(a,'X^2+',b,'X+',c,'=0','有两个解：', (-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a))

A=[1,2,3]; B=[2,8,4]; C=[1,1,3]

find_root(A,B,C)