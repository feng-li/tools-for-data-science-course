# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#在网上看到用python和机器学习训练中文文本情感分类模型，尝试模仿搭建，但因知识储备和技术有限，只能还原一部分内容
import pandas as pd
import numpy as np
from pandas import DataFrame,Series

data = pd.read_csv("data.csv",encoding='')
data

#使用lambda匿名函数，把评分》3的，取值1，当作正向情感，评分《3的，取值0，当作负向情感
def make_label(df):
    df["sentiment"]=df["star"].apply(lambda x:1 if x >3 else 0)
    
make_label(data)
data

X = data[["comment"]]
y = data.sentiment

#导入jieba分词库，创建分词函数，将评论拆分，用空格连接
import jieba
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))
#调用函数，新增列，填充值
X["cuted_comment"] = X.comment.apply(chinese_word_cut)

