import numpy
import scipy
import scipy.linalg
import scipy.optimize
import matplotlib
import re


starts_with_hash = 0
with open("hash file.txt", 'r') as file:
    for line in file:
        if re.match("#", line):
            starts_with_hash +=1

print(starts_with_hash)
