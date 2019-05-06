# !/usr/bin/env python
# 将拓展包导入备用
import logging
import requests
import sys
import urllib
from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urlencode

def get_list(comp, page): 
    
    """
    Goal：捕捉网页信息
    Data：返回摘要字典
    
    """
# 设置空字典
    Data = OrderedDict()
# 设定新浪新闻为抓取对象
    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page)
    html = requests.get(href)
    # Parsing html
    s = BeautifulSoup(html.content, 'html.parser')
    heads = s.findAll('h2')
# 循环遍历，返回结果
    for head in heads:
        # 标题
        titleinfo = head.find('a')
        title = titleinfo.get_text()
        # url
        url = titleinfo['href']
        # 其他
        otherinfo= head.find('span', {'class':'fgray_time'}).get_text()
        source, date, time = otherinfo.split()
        # 整合字典
        Data[title] = [date, source, url]
    return Data
# 设定搜索对象为“摇滚巨人”苏见信
compRawStr = '苏见信'
comp = compRawStr.encode('gbk')
d = {'q': comp}
pname = urlencode(d)
# 输出第1、2页的数据
for page in range(3)[1:]:
    Data = get_list(pname, page)
for ky in Data:
    print('\001'.join([ky] + Data[ky]))