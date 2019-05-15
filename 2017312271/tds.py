import numpy
import scipy
import scipy.linalg
import scipy.optimize
import matplotlib
import pandas
import re
import zipfile


starts_with_hash = 0
with open("hash file.txt", 'r') as file:
    for line in file:
        if re.match("#", line):
            starts_with_hash +=1

print(starts_with_hash)

# pandas.read_csv()
# pandas.read_clipboard()
# pandas.read_pickle()

myzip = zipfile.ZipFile("hash file.zip")
ziphash = myzip.open("hash file.txt", 'r')
for line in ziphash:
    print(line)
print(myzip.namelist())
