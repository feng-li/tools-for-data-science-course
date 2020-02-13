#!/usr/bin/env python
# coding: utf-8


import os
os.chdir("C:\\Users\\Administrator\\Desktop")

import zipfile
datazip = zipfile.ZipFile("data.zip")

import pandas as pd
data = pd.read_csv(datazip.open('data.csv'))