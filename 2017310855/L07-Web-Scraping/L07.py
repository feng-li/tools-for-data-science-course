# !/usr/bin/env python

import logging
import requests
import sys
import urllib
from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode

def get_list(comp, page): 
    
    """
    Goal：Scrap web info
    Data：Return summary dic
    """
    
    # Set emp dic
    Data = OrderedDict()
    
    # Set object
    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page)
    html = requests.get(href)
    
    # Parsing html
    s = BeautifulSoup(html.content, 'html.parser')
    heads = s.findAll('h2')
    
    # Loop
    for head in heads:
        # Topic
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        
        # url
        url = titleinfo['href']
        
        # Others
        otherinfo= head.find('span', {'class':'fgray_time'}).get_text()
        source, date, time = otherinfo.split()
        
        # Organize
        Data[title] = [date, source, url]
        
    return Data
    
# Set search content
compRawStr = '苏见信'
comp = compRawStr.encode('gbk')
d = {'q': comp}
pname = urlencode(d)

# Print
for page in range(3)[1:]:
    Data = get_list(pname, page)
    
for ky in Data:
    print('\001'.join([ky] + Data[ky]))
    
