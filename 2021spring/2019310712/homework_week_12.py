# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:24:51 2021

@author: acer
"""

import jieba

txt = open("三国演义.txt","r", encoding='utf-8')
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
        
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(3):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word,count))
    
