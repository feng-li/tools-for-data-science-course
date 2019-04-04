#!/usr/bin/env python
# coding: utf-8



def find_root(a,b,c):
    """
    To find the roots of ax2+bx+c=0.
    """
    if (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)) and a!= 0):
	from math import sqrt
	delta = b**2-4*a*c
	if delta > 0:
		x1 = -(b + sqrt(delta))/(2*a)
		x2 = -(b - sqrt(delta))/(2*a)
		print("If a="+repr(a)+",b="+repr(b)+",c="+repr(c)+",the roots are"+repr(x1)+","+repr(x2)+".")
	elif delta == 0:
		x1 = -(b + sqrt(delta))/(2*a)
		print("If a="+repr(a)+",b="+repr(b)+",c="+repr(c)+",the roots are same："+repr(x1)+".")
	else:
		print("If a="+repr(a)+",b="+repr(b)+",c="+repr(c)+",the equation doesn't have real root.")
    else:
        print("Please input three numbers,and 'a' can't be zero.")
		

s = [[0,-2,1],[2,1,4],['a',4,0],[1,3,2],[3,11,10],[6,-7,-5],[2,15,7],[4,-12,9]]
for i in range(len(s)):
    find_root(s[i][0],s[i][1],s[i][2])



