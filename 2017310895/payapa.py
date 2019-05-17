import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import pandas
from time import sleep
from urllib.parse import urlencode
import ssl
import random

pro = ['1.119.129.2:8080', '115.174.66.148', '113.200.214.164'] 
header={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}


title=[]
source_time=[]
article=[]

def getweb(word,page):
    compRawStr = word
    comp = compRawStr.encode('gbk')
    d = {'q': comp}
    keyword=urlencode(d)
    webpart1="http://search.sina.com.cn/?"
    webpart2=keyword
    webpart3="&c=news&from=index&col=&range=&source=&country=&size=&time=&a=&page="
    webpart4=str(page)
    webpart5="&pf=0&ps=0&dpc=1"

    print(webpart1+webpart2+webpart3+webpart4+webpart5)
    return webpart1+webpart2+webpart3+webpart4+webpart5

def get_allcontent(web):
    #先解析网页
    response = requests.get(web,proxies={'http': random.choice(pro)},headers=header)
    bs = BeautifulSoup(response.txt , 'html.parser') 
    #获取标题
    for t in bs.select("h2 a"):
        if t.text.strip() !="":
            t=t.text.strip()
            title.append(t)
            sleep(1)
            print(t)
            
    #获取时间和来源
    
    for s in bs.select(".fgray_time"):
        if s.text.strip() !="":
            s=s.text.strip()
            source_time.append(s)
            sleep(1)
            print(s)
    #获取摘要
    
    for p in bs.select(".r-info"):
        if p.text.strip() !="":
            p=p.text.strip()
            article.append(p.replace(" ",""))
            sleep(1)
            print(p)
    #return title,source_time,article

word="刘强东"
page=3
for i in range(3):
    print(i)
    web=getweb(word,i+1)
    print(web)
    get_allcontent(web)
"""
   #total={"Title":title,"Article":article,"SourceandTime":source_time}
   #df=pandas.DataFrame(total)
   #df.to_excel('news.xlsx')"""
import logging  # 引入logging模块
logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
logging.debug(u"如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")
