#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
jieba分词
by Luo Jun QI （SN：2020310987）
'''

import jieba.analyse
sentence = (
"一条大河波浪宽，\
风吹稻花香两岸，\
我家就在岸上住，\
听惯了艄公的号子，\
看惯了船上的白帆，\
一条大河波浪宽，\
风吹稻花香两岸，\
我家就在岸上住，\
听惯了艄公的号子，\
看惯了船上的白帆")

jieba.analyse.extract_tags(sentence, topK=15, withWeight=False, allowPOS=())


# In[2]:


jieba.analyse.textrank(sentence, topK=15, withWeight=False, 
                       allowPOS=('ns', 'n', 'vn', 'v'))


# In[12]:


import jieba

seg_list = jieba.cut("一条大河波浪宽风吹稻花香两岸我家就在岸上住听惯了艄公的号子看惯了船上的白帆", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))


# In[13]:


seg_list = jieba.cut("一条大河波浪宽风吹稻花香两岸我家就在岸上住听惯了艄公的号子看惯了船上的白帆", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))


# In[5]:


test_sent = (
"一条大河波浪宽风吹稻花香两岸我家就在岸上住听惯了艄公的号子看惯了船上的白帆")

jieba.load_userdict("userdict.txt")
words = jieba.cut(test_sent)
print('/'.join(words))

