# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:44:48 2021

@author: Always
"""

import jieba
sentence = '我爱自然语言处理'
# 创建【Tokenizer.cut 生成器】对象
generator = jieba.cut(sentence)
# 遍历生成器，打印分词结果
words = '/'.join(generator)
print(words)

我/爱/自然语言/处理

