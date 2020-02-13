#! /usr/bin/env python3
def F_Root(a, b, c):
    """
    Judge the root of a random quadric equation in one variable.
    The quadratic coefficient is a.
    The primary coefficient is b.
    And the constant is c.
    """
    Delta = b**2 - 4*a*c
    if a == 0:
        print("The equation whose a = ", a, " is not a quadric equation.")
    else:
        if Delta < 0:
            print("The equation whose a = ", a, ", b = ", b, ", and c = ", c, " is rootless.")
        elif Delta == 0:
            x1 = -b/(2*a)
            print("The equation whose a = ", a, ", b = ", b, " and c = ", c, " has only one root.")
            print("And it's ", x1, ".")
        else:
            from math import sqrt
            x1 = (-b + sqrt(Delta))/(2*a)
            x2 = (-b - sqrt(Delta))/(2*a)
            print("The equation whose a = ", a, ", b = ", b, " and c = ", c, " has two different roots.")
            print("One is ", x1, " and another is ", x2, ".")
from random import sample
A = sample(range(-10, 10), 10)
B = sample(range(-10, 10), 10)
C = sample(range(-10, 10), 10)
for i in range(10):
    F_Root(A[i], B[i], C[i])
