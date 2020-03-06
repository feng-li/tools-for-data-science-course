#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:36:49 2019

@author: lvanzhu
"""

import numpy
import scipy
import pandas
import matplotlib
import re


import os
os.chdir('/Users/lvanzhu/Documents')
file_reading = open("0403..py",'r') #打开数据

file_reading.close() #关闭数据

start_hash = 0

with open('0403..py','r') as file:
    for line in file:
        if re.match("#",line):
           start_hash += 1
print(start_hash)

#有问题
with open('0403..py','r') as file:
     if file.read() == "^#":
        start_hash += 1
print(start_hash)
                    
import os
os.chdir('/Users/lvanzhu/Documents/2018大三下/python/Python-for-Statisticians/L3')
data2 = pandas.read_csv('stocks.csv',delimiter = '\t')
data2 = pandas.read_csv('stocks.csv') #\t表示分割

#读取zip
import zipfile
os.chdir('/Users/lvanzhu/Documents/2018大三下/python/Python-for-Statisticians/L3')

myzip = zipfile.ZipFile('stocks.csv.zip') #读取压缩文件

f=myzip.open('stocks.csv') #打开压缩文件
f.close()#关闭

myzip.namelist() #读出压缩文件中的所有文件名字

stocks = pandas.read_csv(myzip.open("stocks.csv")) #open函数可以读取文件
myzip.close()

myzip.filename #zip压缩文件的名字





















