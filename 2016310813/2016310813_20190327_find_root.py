
# coding: utf-8

# In[11]:

# ax^2 + bx + c = 0
import math
abc = [2,3,1];
def find_root(abc):
    a = abc[0];b = abc[1];c = abc[2];
    x = [0,0];
    if a == 0:
        x[0] = -c/b;x[1] = x[0];
    else:
        delta = b**2-4*a*c;
        if  delta < 0:
            print("方程无实数解");
        else:
            x[0] = (-b+math.sqrt(delta))/(2*a);
            x[1] = (-b-math.sqrt(delta))/(2*a);
    return x
find_root(abc)

