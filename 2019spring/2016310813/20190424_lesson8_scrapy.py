
# coding: utf-8

# In[7]:

import csv
import os
import numpy as np
import random
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from random import randint
import seaborn
import requestsfrom bs4 import BeautifulSoup


# In[10]:

import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.sina.com.cn/world/')
# 请求获取链接返回的内容
res.encoding = 'utf-8'#设置编码格式为utf-8
soup = BeautifulSoup(res.text, 'html.parser')#前面已经介绍将html文档格式化为一个树形结构，每个节点都是一个对python对象，方便获取节点内容
for new in soup.select('.news-item'):#BeautifulSoup提供的方法通过select选择想要的html节点类名，标签等，获取到的内容会被放到列表中
    if len(new.select('h2')) > 0:
        #加[0]是因为select获取内容后是放在list列表中[内容,],text可以获取标签中的内容
        print( new.select('.time')[0].text+' '+new.select('h2')[0].text +' '+ new.select('a')[0]['href'] )


# In[ ]:

import time
import requests
from bs4 import BeautifulSoup 
info = requests.get('http://news.sina.com.cn/w/2018-09-04/doc-ihiixzkm4326136.shtml')
info.encoding = 'utf-8'
html = BeautifulSoup(info.text, 'html.parser')

print (html.select('.second-title')[0].text) #获取大标题
print (html.select('.date')[0].text) #获取发布时间
#dt = time.strptime(timesource, '%Y年%m月%d日 %H:%M') #用来格式化时间字符串为时间格式方便储存
#dt.strftime('%Y-%m-%d')
print (html.select('.source')[0].text + '  '+html.select('.source')[0]['href'])
article = []
for v in html.select('.article p')[:-1]:#获取article中被p包含的内容去除最后一个p标签即责任编辑
    article.append(v.text.strip())#将内容添加到列表中，并去除两边特殊字符
author_info = '\n'.join(article)#将列表中内容以换行连接
print( author_info)
print( html.select('.show_author')[0].text.lstrip(u'责任编辑：'))#输出编辑姓名

