#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import csv
def save_csv(data):
    with open('news.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

if __name__ == '__main__':
    save_csv(['新闻标题','新闻内容'])
    url = 'https://cj.sina.com.cn/articles/view/2375086267/8d90f0bb02000zgh8?from=finance'
    response = requests.get(url=url).text
    #response = response.encode("latin-1")
    #response = response.decode("utf-8")
    dom = etree.HTML(response)
    article_list = dom.xpath("//div[@id='artibody']//text()")
    name=article_list[5]
    content=''
    for item in article_list[5:-2]:
        content=content+item+'\n'
        print(item)
    save_csv([name,content])
   
