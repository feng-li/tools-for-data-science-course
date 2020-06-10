# coding: utf-8
import requests
from bs4 import BeautifulSoup
import re
from __future__ import unicode_literals
from wxpy import *
from threading import Timer

bot = Bot()
def sendWea(Wea):

    myFriend=bot.friends().search(u'数据科学工具')[0])
    myFriend.send(Wea)
    t=Timer(86400,sendWea)
    t.start()

def getWeather():
    url = 'http://www.weather.com.cn/weather1d/101070901.shtml'
    ret = requests.get(url)
    ret.encoding = 'utf-8'
    soup = BeautifulSoup(ret.text, 'html.parser')
    tagToday = soup.find('p', class_ = "tem") 
    try:  
        highTemperature = tagToday.span.string  
    except AttributeError:
        highTemperature ='未显示最高气温'
    lowTemperature = tagToday.i.string  
    weather = soup.find('p', class_ = "wea").string
    wind = soup.find('p', class_ = "win") 
    return {'最高温度':highTemperature
            ,'最低温度':lowTemperature
            , '天气':weather
            , '风力':wind.i.string}

def wea(wea):
    weather = ''
    for m in wea:
       weather += m + ':' + wea[m]+'/n'       
    return weather
if __name__ == "__main__":
    Wea = wea(getWeather())
    sengWea(Wea)
