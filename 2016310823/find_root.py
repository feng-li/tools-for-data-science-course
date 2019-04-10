#求根函数
def find_root(a,b,c):
    """
    求一元二次方程ax^2+bx+c=0的根
    
    """
    #a,b,c numeric/a=0
    if not a.isnumeric() and not b.isnumeric() and not c.isnumeric():
        print('请输入三个数字') 
    delta = b**2-4*a*c
    expression = str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0"
    import math
    if delta < 0:
        print(expression,"无实数解\n")
    elif delta == 0:
        print(expression," 的解为: x = ",-b/(2*a),"\n",sep = '')
    elif delta > 0:
        print(expression," 的解为: x1 = ",(-b+math.sqrt(delta))/(2*a),", x2 = ",(-b-math.sqrt(delta))/(2*a),"\n",sep = '')

#构造十个一元二次方程
import numpy as np
A = range(2,12)
B = np.random.randint(15,size=10)
C = np.random.randint(15,size=10)

if [[not str(X[i]).isnumeric() for i in range(len(X))] for X in [A,B,C]]:
    print('y')
else:
    print('n')

def find_roots(A,B,C):
    

for i in range(len(A)):
    find_root(A[i],B[i],C[i])

['A[i]'.isnumeric() for i in range(len(A))]
