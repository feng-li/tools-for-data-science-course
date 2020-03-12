#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile
import pandas as pd

myzip = zipfile.ZipFile('mycsv.zip')
print(myzip.namelist())
mycsv = pd.read_csv(myzip.open('mycsv.csv'))

