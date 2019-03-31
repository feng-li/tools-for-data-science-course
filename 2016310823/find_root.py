#求根函数
def find_root(a,b,c):
    """
    求一元二次方程ax^2+bx+c=0的根
    
    """
    delta = b**2-4*a*c
    expression = str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0"
    import math
    if delta < 0:
        print(expression,"无实数解\n")
    elif delta == 0:
        print(expression," 的解为: x = ",-b/(2*a),"\n",sep = '')
    elif delta > 0:
        print(expression," 的解为: x1 = ",(-b+math.sqrt(delta))/2*a,", x2 = ",(-b-math.sqrt(delta))/2*a,"\n",sep = '')

#构造十个一元二次方程
import numpy as np
A = range(2,12)
B = np.random.randint(15,size=10)
C = np.random.randint(15,size=10)

for i in range(10):
    find_root(A[i],B[i],C[i])
    