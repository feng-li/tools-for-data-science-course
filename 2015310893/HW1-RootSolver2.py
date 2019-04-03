#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np


def __root_solver_2_single(a, b, c):
    """
    Solve the two real roots for a single equation ax**2 + bx + c = 0
    :param a: a
    :param b: b
    :param c: b
    :return: (x1, x2)
    """
    delta = b * b - 4 * a * c
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b / 2, -b / 2
    else:
        return (-b + np.sqrt(delta)) / 2, (-b - np.sqrt(delta)) / 2


def __print_roots(a, b, c):
    """
    print coefs and roots for a single equation
    :param a: a
    :param b: b
    :param c: c
    :return: None
    """
    print('The equation is % g x^2%+g x%+g = 0. ' % (a, b, c), end='\n    ')
    x1, x2 = __root_solver_2_single(a, b, c)
    if x1 and x2:
        print('The two roots are %7g, %7g.' % (x1, x2))
    else:
        print('There is no real root.')
    return None


def HW1_root_solver(coef):
    """
    Solve the real roots for a set of equations a_i x ** 2 + b_i x + c_i = 0,
    where a_i, b_i, c_i is stored in coef matrix.
    :param coef: An n by 3 matrix. a_i, b_i and c_i should respectively stored in the 1st, 2nd and 3rd column
    :return: None, roots would be print
    """
    coef = list(coef)
    _ = list(map(__print_roots, *zip(*coef)))
    return None


if __name__ == '__main__':
    data = np.random.randn(100, 3)
    HW1_root_solver(data)
