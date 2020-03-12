def equart(A,B,C):
    """
    Judge whether a quadratic equation like "Ax^2 + Bx + C = 0"
      has any root,and if so,find it.

    """
    import math
    for a in A:
        for b in B:
            for c in C:
                print('if a =',a,',b =',b,'c =',c,',',end = '')
                delta = b**2 - 4*a*c     #use the delta to judge whether the equation has any root
                x = -b/(2*a)
                if delta < 0:
                    print('The equation has no root.')
                elif delta == 0:
                    print('The equation has an equal real root，it is x=' + str(x) + '.')
                else:
                    x1 = x + math.sqrt(delta)/(2*a)
                    x2 = x - math.sqrt(delta)/(2*a)
                    print('The equation has two roots,they are x1=' + str(x1) + ', x2=' + str(x2)+ '.')



import random
a1 = random.sample(range(1,100),10)      #Generate three sets of random numbers
b1 = random.sample(range(1,100),10)
c1 = random.sample(range(1,100),10)
print('a1 = ',a1)
print('b1 = ',b1)
print('c1 = ',c1)
equart(a1,b1,c1)