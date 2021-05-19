# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:35:28 2021

@author: Vicky Lamperouge
"""

import jieba
txt=open(r'E:\##个人##\大一学习\数据科学工具\小说.txt','r',encoding='utf-8').read()

for ch in '-)(*&^%$#@!~\[]{}_':
    txt=txt.replace(ch," ")
    
wordsls=jieba.lcut(txt)
wcdict={}
for word in wordsls:
    if len(word)==1:
        continue
    else:
        wcdict[word]=wcdict.get(word,0)+1
#word在wcdict中没有找到对应的词语，则返回0
wcdict.sort(key=lambda x:x[1],reverse=True)

for i in range(25):
    print(wcdict[i])
