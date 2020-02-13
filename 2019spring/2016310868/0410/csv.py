# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:39:14 2019

@author: dell
"""

import pandas
data2 = pandas.read_csv('FundData.csv', delimiter='\t',header=None) 
data2.values.shape
data = pandas.read_csv('FundData.csv',header=None)
data.values.shape

import zipfile
myzip = zipfile.ZipFile('FundData.zip')
myzip.filename()
myzip.namelist()
pandas.read_csv(myzip.open('FundData.csv'))