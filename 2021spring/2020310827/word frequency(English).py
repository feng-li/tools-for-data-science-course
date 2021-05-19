# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:33:26 2021

@author: Vicky Lamperouge
"""

with open('E:\##个人##\大一学习\数据科学工具\news.txt') as read_file:
    txt=read_file.read()
    
def getText():
    txt=txt.lower()
    for ch in '!"@#$%^&*()_[\\]~'{|}',./?><':
        txt=txt.replace(ch," ")
    return txt
    
newsTxt=getText()
words=newsTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word.count))
    