# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:52:14 2019

@author: youra
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
titanic_data = sns.load_dataset("titanic")
sns.lmplot(x = "age", y = "survived",
           logistic = True,
           hue = "sex",
           data = titanic_data, y_jitter = .03)
