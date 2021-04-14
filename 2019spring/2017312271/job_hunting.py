import logging
import requests
import sys
import urllib
import scrapy

from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode


def get_list(comp, page):
    """Function to get  web list pages for a given company and page number.

    Args:
        comp: Company name.
        page: The page number.

    Returns:
        newsData: A dictionary with news title as its key and other details as values.

    """
    newsData = OrderedDict()
    # comp -> first %s; page -> 2nd %s; col=1_7 -> financial news in sina
    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page)
    html = requests.get(href)
    # Parsing html
    soup = BeautifulSoup(html.content, 'html.parser')
    divs = soup.findAll('div', {"class": "r-info r-info2"})
    for div in divs:
        head = div.findAll('h2')[0]
        # News title
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        # News url
        url = titleinfo['href']
        # Other info
        otherinfo = head.find('span', {"class": "fgray_time"}).get_text()
        source, date, time = otherinfo.split()
        # News abstract
        abstract = div.find('p', {"class": "content"}).get_text()
        newsData[title] = [date, source, abstract, url]
    return newsData


if __name__ == "__main__":
    compRawStr = '百度'
    # Dealing with character encoding
    comp = compRawStr.encode('gbk')
    d = {'q': comp}
    pname = urlencode(d)
    # Scraping and printing the first two pages
    for page in range(3)[1:]:
        newsData = get_list(pname, page)
        for ky in newsData:
            print('\001'.join([ky] + newsData[ky]))  # "\001" as separator
