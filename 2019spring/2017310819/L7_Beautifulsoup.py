# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
res = urllib.urlopen("http://www.baidu.com")
print res.read()

url = "http://www.baidu.com"
page = urllib.urlopen(url)
soup = BeautifulSoup(page，"html.parser")
print soup


res = urllib.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res,"html.parser")
book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print book.string
