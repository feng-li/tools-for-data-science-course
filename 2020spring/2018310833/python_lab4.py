import logging
import requests
import sys
import urllib

from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode


def get_list(words, page):
    
    newsData = OrderedDict()
    href = 'http://search.sina.com.cn/?%s&c=news&from=&col=&range=all&source=&country=&size=10&time=&dpc=0&a=&ps=0&pf=0&page=%s' % (words, page) # words -> first %s; page -> 2nd %s; col=1_7 -> financial news in sina
    html = requests.get(href)
    soup = BeautifulSoup(html.content, 'html.parser')
    divs = soup.findAll('div', {"class": "r-info r-info2"})
    for div in divs:
        head = div.findAll('h2')[0]
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        url = titleinfo['href']
        otherinfo = head.find('span', {"class": "fgray_time"}).get_text()
        source, date, time = otherinfo.split()
        abstract = div.find('p', {"class": "content"}).get_text()
        newsData[title] = [source, date,time, abstract, url]
    return newsData


   
if __name__ == "__main__":
    wordsRawStr = '新冠病毒'
    words = wordsRawStr.encode('gbk')
    d = {'q': words}
    pname = urlencode(d)
    virus = []
    for page in range(1,10):
        newsData = get_list(pname, page)
        for ky in newsData:
            a = '\001'.join([ky] + newsData[ky])
            virus.append(a)
    

import pandas as pd
news = pd.DataFrame(data = virus)
news.to_csv("C:/Users/Jellysillyfish/Desktop/news.txt")
with open("C:/Users/Jellysillyfish/Desktop/news.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
with open("C:/Users/Jellysillyfish/Desktop/news.txt","w",encoding="utf-8") as f_w:
    for line in lines:
        if ",0" in line:
            continue
        f_w.write(line)


def get_body(href):
    html = requests.get(href)
    soup = BeautifulSoup(html.content, 'html.parser')
    try:
        div = soup.find('div',{"id":"artibody"})
        paras = div.find_all("p")
        content = ''
        for p in paras:
            ptext = p.get_text().strip().replace("\n","")
            content += ptext
        
    except:
        pass
    return content

        


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    virus_news = []
    with open("C:/Users/Jellysillyfish/Desktop/news.txt",encoding="utf-8") as f:
        for line in f:
            try:
                label,title, source, date, abstract, href = line.strip().split('\001')
                logging.info('Scraping ' + href)
                content = get_body(href)
                b='\001'.join([label,title, source, date, abstract, href, content])
                virus_news.append(b)
            except:
                pass
            continue
        

import pandas as pd
news1 = pd.DataFrame(data = virus_news)
news1.to_csv("C:/Users/Jellysillyfish/Desktop/virus_news.txt")


            
        



            
   
        
