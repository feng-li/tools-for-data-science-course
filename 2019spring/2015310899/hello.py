#!/usr/bin/env python
# coding: utf-8



def parity(n):
    """To judge whether an integer is odd or even."""      # the function help
    if n%2==0:
        print(repr(n)+' is even.')
    elif n%2==1:
        print(repr(n)+' is odd.')
    else:
        print(repr(n)+' is neither odd nor even.') 

parity(3)





