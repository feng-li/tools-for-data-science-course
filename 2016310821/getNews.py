from urllib import request
import requests
from bs4 import BeautifulSoup
import logging
import sys
from collections import OrderedDict
from urllib.parse import urlencode


def getNews(comp):
    '''
    Function to get news about given company.
    
    Args:
        comp: Company name
    
    Returns:
        newsData: A dictionary with news title as its keys and details as its values.
    '''
    
    NewsData = OrderedDict()
    cpname = comp.encode('gbk')
    d = {'q': cpname}
    comp = urlencode(d)
    cookie = 'SINAGLOBAL=106.38.124.44_1539233363.37888; UOR=www.baidu.com,finance.sina.com.cn,; U_TRS1=000000b1.3c22739c.5bc5e985.f9ab378b; mYSeArcH=%u767E%u5EA6; U_TRS2=0000001b.cc365f.5cdbda7c.e49e5184; Apache=106.121.8.27_1557912189.95496; ULV=1557912195534:11:3:2:106.121.8.27_1557912189.95496:1557912189376; lxlrttp=1556243090'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
              'Connection': 'keep-alive',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Cookie': cookie}
        
    for page in range(11)[1: ]:
        link = 'http://search.sina.com.cn/?q=%s&c=news&from=index&col=&range=&source=&country=&size=&time=&a=&page=%s&pf=0&ps=0&dpc=1' % (comp, page)
        html = requests.get(link, headers = header).text
        
        bs = BeautifulSoup(html, "html.parser")
        namelist = bs.findAll('div', {'class': 'box-result clearfix'})
        for name in namelist:
            head = name.find('h2')
            titleInfo = head.find('a')
            title = titleInfo.get_text()
            url = titleInfo['href']
            otherInfo = head.find('span', {'class': 'fgray_time'}).get_text()
            source, date, time = otherInfo.split(' ')
            abstract = name.find('div', {'class': 'r-info'}).find('p', {'class': 'content'}).get_text()
            NewsData[title] = [date, source, abstract, url]
    return(NewsData)





if __name__ == "__main__":

    NewsData = getNews('新浪')
    for ky in NewsData:
        print('\001'.join([ky] + NewsData[ky]))
