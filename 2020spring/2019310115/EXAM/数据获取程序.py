import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
rank=input("输入数字货币的排名：")
coinData = OrderedDict()
href = 'https://www.hqz.com/exchange/huobipro/'
html = requests.get(href)
soup = BeautifulSoup(html.content, 'html.parser')
divs = soup.findAll('tbody')
for div in divs:
   head = div.findA"class": "volume"}).get_text()
coinData[name] = [name, price,ll('tr')[int(rank)-1]
        # 名称
   name = head.find('td', {"class": "w-120px ellipsis"}).get_text()
        # 价格
   price = head.find('td', {"class": "price"}).get_text()
        # 24小时成交额
   volume = head.find('td', { volume]
print (coinData)
