#!/usr/bin/env python
# coding: utf-8

# In[19]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.cctv.com/')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('div', {'class':'wrapper_1200'})
for name in nameList:
    print(name.get_text())


# In[55]:


import logging
import requests
import sys
import urllib

from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode

def get_list(comp, page):
    newsData = OrderedDict()
    href = 'https://www.sogou.com/sogou?query=%s&pid=sogou-wsse-f880d0d6a01ba52f-&page=%s&ie=utf8' % (comp, page) # comp -> first %s; page -> 2nd %s; col=1_7 -> financial news in sina
    html = requests.get(href)
    # Parsing html
    soup = BeautifulSoup(html.content, 'html.parser')
    divs = soup.findAll('div', {"class": "rb"})
    for div in divs:
        head = div.find('h3',{"class":"pt"})
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        # News url
        url = titleinfo['href']
        # Other info
        source=div.find('div',{"class":"fb"}).get_text()
        # News abstract
        abstract = div.find('div',{"class":"ft"}).get_text()
        newsData[title] = [source,abstract, url]
    return newsData



if __name__ == "__main__":
    compRawStr = '新冠肺炎'
    # Dealing with character encoding
    comp = compRawStr.encode('utf-8')
    d = {'q': comp}
    pname = urlencode(d)
    # Scraping and printing the first two pages
    for page in range(10)[1:]:
        newsData = get_list(pname, page)
        for ky in newsData:
            print('\001'.join([ky] + newsData[ky])) # "\001" as separator
        


# In[58]:


import csv
csv_file = open("c:/dell/爬虫.csv",'w+')
csv_writer = csv.writer(csv_file)
for ky in newsData:
    csv_writer.writerow([ky])


# In[ ]:





# In[ ]:




