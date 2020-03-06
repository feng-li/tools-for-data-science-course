#张韵文 2017310819
#打开文件
#================================
#方法一
#! /Usr/bin/ecv python3
# hash_check.py
import re
starts_with_hash = 0
with open('方程有无解.py','r',encoding='gb18030',errors='ignore') as file:  
    for line in file:
        if re.match('#',line):
            starts_with_hash += 1
print(starts_with_hash)


#===============================
#方法二
starts_with_hash2 = 0
file2 = open("方程有无解.py",encoding='gb18030',errors='ignore')
cf = file2.read()
for line in cf:
    if re.match('#',line):
        starts_with_hash2 += 1
print(starts_with_hash2)
file2.close()
