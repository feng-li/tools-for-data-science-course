from math import sqrt
import numpy as np
def find_root(a, b, c):
    """
    get roots of a quadratic equation
    
    Usage
    
         find_root(a, b, c)
    """
    delta = b**2-4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                print('identical equation')
            else:
                print('ipossible equation')
            root = ''
        else:
            root = -c/b
    elif delta == 0:
        print('double roots')
        root = -b/2/a
    elif delta > 0:
        print('two different real roots')
        root = [(-b+sqrt(delta))/2/a, (-b-sqrt(delta))/2/a]
    else:
        print('two different complex roots')
        root = [complex(-b/2/a, sqrt(-delta)/2/a), complex(-b/2/a, -sqrt(-delta)/2/a)]
    return root

np.random.seed(0)
a = np.random.randint(0, 100, 10)
np.random.seed(1)
b = np.random.randint(0, 100, 10)
np.random.seed(2)
c = np.random.randint(0, 100, 10)

for i in range(10):
    print("parameters: " + ", ".join([str(a[i]), str(b[i]), str(c[i])]))
    print(str(find_root(a[i], b[i], c[i])))
