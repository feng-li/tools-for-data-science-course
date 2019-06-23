#! /usr/bin/env python3

from zipfile import ZipFile
from pandas import read_csv

M_Zip = zipfile.ZipFile('/Users/mukatatsu/roe.csv.zip')
M_Zip.namelist()

read_csv(M_Zip.open('roe.csv'))
