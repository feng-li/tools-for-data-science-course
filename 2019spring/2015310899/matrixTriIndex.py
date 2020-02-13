#!/usr/bin/env python
# coding: utf-8


def matrixTriIndex(n, diag = True, lower = True):
    """
    To print the indexes of an n-dimensional triangular matrix.
    diag = True/False  --->  print the indexes of diagonal elements or not
    lower = True/False  --->  the lower triangular matrix / the upper triangular matrix
    """
    return [(x,y) for x in range(1,n+1) for y in range(1,n+1)  if (diag and x == y) 
	      or (lower and x > y) or (lower == False and x < y)]

	
print(matrixTriIndex(4,True,False))