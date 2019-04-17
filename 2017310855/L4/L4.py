#! /usr/bin/env python3
from zipfile import ZipFile
M_Zip = zipfile.ZipFile('/Users/mukatatsu/roe.csv.zip')
M_Zip.namelist()
from pandas import read_csv
read_csv(M_Zip.open('roe.csv'))
