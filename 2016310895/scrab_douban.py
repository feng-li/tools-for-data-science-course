# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:10:28 2019

@author: Lee Oscar
"""

from bs4 import BeautifulSoup
import requests

url = "https://movie.douban.com/top250"
f = requests.get(url)       #Get该网页从而获取该html内容
soup = BeautifulSoup(f.content,'lxml')      #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
print(f.content.decode())
#content = soup.find_all('div',class_="info" )   #因为calss和关键字冲突，所以改名class_

name = []
for k in soup.find_all('div',class_ = 'info'):
    a = k.find_all('span',class_ ='title')
    print(a[0].string)
    name.append(a[0].string)

score = []
for k in soup.find_all('div',class_ = 'info'):
    a = k.find_all('span',class_ ='rating_num')
    print(a[0].string)
    score.append(a[0].string)
    
quote = []
for k in soup.find_all('div',class_ = 'info'):
    a = k.find_all('span',class_='inq')
    print(a[0].string)
    quote.append(a[0].string)
    
info = []
for k in soup.find_all('div',class_ = 'info'):
    a = k.find_all('p',class_='')
    print(a)
    info.append(a)
 

scrapy = {'name':name,'info':info,'quote':quote,'score':score}
print(scrapy)