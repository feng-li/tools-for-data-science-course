import time
import numpy as np
import sys
import datetime
import pandas as pd
import os

date2position = {}
datestr2dateint = {}
str2int = {}
for i in range(150):
 date = datetime.date(day=1, month=10, year=2018)+datetime.timedelta(days=i)
 #print(i,":",date)
 date_int = int(date.__str__().replace("-", ""))
 date2position[date_int] = [i%7, i//7]
 datestr2dateint[str(date_int)] = date_int
#print(datestr2dateint)
#
for i in range(24):
 str2int[str(i).zfill(2)] = i
f=open("D:\Data Science\studying material.txt")
#table = pd.read_csv(f, header=None,error_bad_lines=False)
table = pd.read_csv(f, header=None,sep='\t')
 
#print(table.shape)
#print(table.ix[1])
strings = table[1]
#print(strings)
init = np.zeros((7, 26, 24))
for string in strings:
 temp = []
 for item in string.split(','):
 temp.append([item[0:8], item[9:].split("|")])
 for date, visit_lst in temp:
 # x - 第几周
 # y - 第几天
 # z - 几点钟
 # value - 到访的总人数
 # print(visit_lst)
 print(date)
 x, y = date2position[datestr2dateint[date]]
 for visit in visit_lst: # 统计到访的总人数
  init[x][y][str2int[visit]] += 1
 #print(init[x][y][str2int[visit]])```
