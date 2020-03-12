# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:57:02 2019

@author: tutuxy
"""

from urllib.request import urlopen
html = urlopen('https://feng.li/python/')
print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://feng.li/python/')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://feng.li/python/')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('div', {'class':'entry-content'})
for name in nameList:
    print(name.get_text())
    
import logging
import requests
import sys
import urllib

from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode



import logging
#作为分隔，单独存在另一个文件中 
import requests
import sys

from bs4 import BeautifulSoup




def get_body(href):
    """Function to retrieve news content given its url.

    Args:
        href: url of the news to be crawled.

    Returns:
        content: the crawled news content.

    """
    html = requests.get(href)
    soup = BeautifulSoup(html.content, 'html.parser')
    div = soup.find('div', {"id": "artibody"})
    paras = div.findAll('p')
    #段落
    content = ''
    for p in paras:
        ptext = p.get_text().strip().replace("\n", "")
        content += ptext
    return content



if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    # Getting and printing content for each url in the crawled web list pages
    with open("data/baidu_list") as f:
        for line in f:
            title, date, source, abstract, href = line.strip().split('\001')
            # Printing progress onto console
            logging.info('Scraping ' + href)
            content = get_body(href)
            print('\001'.join([title, date, source, abstract, href, content]))