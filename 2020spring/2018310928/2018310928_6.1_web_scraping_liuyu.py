#标题
import logging
import requests
import sys
import urllib

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
    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page) # comp -> first %s; page -> 2nd %s; col=1_7 -> financial news in sina
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
    compRawStr = '新冠病毒'
    # Dealing with character encoding
    comp = compRawStr.encode('gbk')
    d = {'q': comp}
    pname = urlencode(d)
    # Scraping and printing the first two pages
    for page in range(4)[1:]:
        newsData = get_list(pname, page)
        for ky in newsData:
            print('\001'.join([ky] + newsData[ky])) # "\001" as separator
   
        

#正文
import logging
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
    content = ''
    for p in paras:
        ptext = p.get_text().strip().replace("\n", "")
        content += ptext
    return content



if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    # Getting and printing content for each url in the crawled web list pages
    with open("ccc.txt",encoding="utf-8") as f:
        for line in f:
            title, date, source, abstract, href = line.strip().split('\001')
            # Printing progress onto console
            logging.info('Scraping ' + href)
            content = get_body(href)
            print('\001'.join([title, date, source, abstract, href, content]))
