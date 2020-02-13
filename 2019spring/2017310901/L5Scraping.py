#!/usr/bin/env python
# coding: utf-8

# In[75]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
html = urlopen('https://search.sina.com.cn/?q=%E7%99%BE%E5%BA%A6&c=news&from=channel&ie=utf-8')
bs = BeautifulSoup(html.read(), 'html.parser')
heads=bs.findAll('h2')
newsData = OrderedDict()
for head in heads:
    titleinfo=head.find('a')
    title=titleinfo.get_text()
    url=titleinfo['href']
    otherinfo=head.find('span',{'class':'fgray_time'}).get_text()
    source,date,time=otherinfo.split()
    newsData[title] = [date, source, url]
for ky in newsData:
    print('\001'.join([ky] + newsData[ky])) # "\001" as separator
    


# In[ ]:





# In[64]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://search.sina.com.cn/?q=%E7%99%BE%E5%BA%A6&c=news&from=channel&ie=utf-8')
bs = BeautifulSoup(html.read(), 'html.parser')
divs = bs.findAll('h2')
for div in divs:
    titleinfo =div.find('a')
    title = titleinfo.get_text()
    print(title)
    url = titleinfo['href']
    print(url)


# In[86]:


import logging
import requests
import sys
import urllib

from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode
def get_list(comp, page):
    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page)
    html = requests.get(href)
    bs = BeautifulSoup(html.content, 'html.parser')
    heads=bs.findAll('h2')
    newsData = OrderedDict()
    for head in heads:
        titleinfo=head.find('a')
        title=titleinfo.get_text()
        url=titleinfo['href']
        otherinfo=head.find('span',{'class':'fgray_time'}).get_text()
        source,date,time=otherinfo.split()
        newsData[title] = [date, source, url]
    return newsData
compRawStr = '沃尔玛'
comp = compRawStr.encode('gbk')
d = {'q': comp}
pname = urlencode(d)
for page in range(5)[1:]:
    newsData = get_list(pname, page)
for ky in newsData:
    print('\001'.join([ky] + newsData[ky])) # "\001" as separator

