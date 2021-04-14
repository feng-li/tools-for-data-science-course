# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:11:37 2019

@author: Lee Oscar
"""

import zipfile
myzip = zipfile.ZipFile('package.zip')  #读取压缩包
myzip.namelist()    #查看压缩包内文件

import pandas
pandas.read_csv(myzip.open(""))     #读取压缩包内文件