# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:20:14 2021

@author: acer
"""

import numpy as np
import pandas as pd
user_info = pd.read_csv("D:\hero_info_o.csv")
user_info

backup_user_info = user_info.copy(deep = True)
backup_user_info

user_info.哪个星球 = user_info.哪个星球.replace({'地球':'earth','外星':'Alien'})
user_info

user_info = backup_user_info.copy()
user_info

user_info.哪个星球 = user_info.哪个星球.map({'地球':'earth','外星':'Alien'})
user_info

def 大写(x):
    return x.upper()
user_info.哪个星球 = user_info.哪个星球.map(大写)
user_info

user_info.哪个星球 = user_info.哪个星球.map(lambda x : x.lower())
user_info


user_info = pd.read_csv('hero_info_o.csv')
user_info

user_info = backup_user_info.copy()
user_info.身高 = user_info.身高.str.replace('cm','')
user_info

user_info.身高 = user_info.身高.astype('int32')
user_info

user_info['姓名长度'] = user_info.英雄姓名.str.len()
user_info.info()

user_info.年不年轻.str.replace('中年','中老年')
user_info.年不年轻.str.count('轻')

user_info.哪个星球.str.replace('R','r')
user_info.年不年轻 = user_info.年不年轻.str.split('年')
user_info

user_info.年不年轻[:]
user_info['爱人'] = ['小A,小B','小C,小D',]
user_info.爱人 = user_info.爱人.str.split(',')
user_info

user_info.英雄姓名.str.get_dummies()
user_info.哪个星球.str.get_dummies()

