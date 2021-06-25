import logging
import requests
import sys
import urllib
import re   
#利用
from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode

def get_list(topic,page):
    """Function to get  web list pages for a given topic and page number.

    Args:
        topic:The news topic
        page: The page number.

    Returns:
        newsData: A dictionary with news title as its key and other details as values.

    """
    newsData = OrderedDict()
    href = 'http://search.sina.com.cn/?%s&c=news&from=&col=&range=title&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=%s'% (topic, page) 
    html = requests.get(href)
    # Parsing html
    soup = BeautifulSoup(html.content, 'html.parser')
    divs = soup.findAll('div', {"class": "box-result clearfix"})
    for div in divs:
        head = div.findAll('h2')[0]
        # News title
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        a = re.compile(r'\u325b|\u2b07|\ufe0f|\ufffd|\u200b')
        title = a.sub('', title)
        # News url
        url = titleinfo['href']
        # Other info
        otherinfo = head.find('span', {"class": "fgray_time"}).get_text()
        otherinfo = a.sub('', otherinfo)
        source, date, time = otherinfo.split()
        # News abstract
        abstract = div.find('p', {"class": "content"}).get_text()
        abstract = a.sub('',abstract)
        newsData[title] = [date, source, abstract, url]
    return newsData



if __name__ == "__main__":
    topicRawStr = '新冠病毒'
    # Dealing with character encoding
    topic = topicRawStr.encode('gbk')
    d = {'q': topic}
    pname = urlencode(d)
    # Scraping and printing the first two pages
    newsDatas={}
    for page in range(10)[1:]:
        newsData=get_list(pname, page)
        newsDatas.update(newsData)
    for ky in newsDatas:
        print('\001'.join([ky] + newsDatas[ky])) # "\001" as separator
