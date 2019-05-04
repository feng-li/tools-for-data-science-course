import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas

title=[]
source_time=[]
article=[]

word="刘强东"
page=6

def getweb(word,page):
    keyword=urllib.parse.quote(word)
    webpart1="https://search.sina.com.cn/?c=news&ie=utf-8&q="
    webpart2=keyword
    webpart3="&col=&range=&source=&from=&country=&size=&time=&a=&page="
    webpart4=str(page)
    webpart5="&pf=0&ps=0&dpc=1"
    return webpart1+webpart2+webpart3+webpart4+webpart5

def get_allcontent(web):
    #先解析网页
    html=urlopen(web)
    bs = BeautifulSoup(html.read(), 'html.parser') 
    #获取标题
    for t in bs.select("h2 a"):
        if t.text.strip() !="":
            t=t.text.strip()
            title.append(t)
            print("0")
    #获取时间和来源
    
    for s in bs.select(".fgray_time"):
        if s.text.strip() !="":
            s=s.text.strip()
            source_time.append(s)
            print("0")
    #获取摘要
    
    for p in bs.select(".r-info"):
        if p.text.strip() !="":
            p=p.text.strip()
            article.append(p.replace(" ",""))
            print("0")
    return title,source_time,article
for i in range(page):
    web=getweb(word,page+1)
    get_allcontent(web)
total={"Title":title,"Article":article,"SourceandTime":source_time}
df=pandas.DataFrame(total)
df.to_excel('news.xlsx')    
