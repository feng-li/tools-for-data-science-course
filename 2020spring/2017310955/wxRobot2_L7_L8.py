# -*- coding: utf-8 -*-
"""
"""

import itchat
import datetime
import os
import matplotlib
import requests
from skimage import io
from bs4 import BeautifulSoup


def get_HTML(url):
    '''获取一个网页，headers模拟浏览器的报头，注意是字典形式和键的名称；response是
    服务器发到客户端上完整的报表，谷歌浏览器看到的网页源码是其中的一部分；raise_for_status()
    如果没有获取成功会返回连接状态；编码方式用响应的apparent_encoding；在查找资源中我们只需要
    在网页源码中找即可，所以返回响应的文本'''
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    return response.text

def get_weather(province, cityIndex, countryIndex=1):
    '''通过观察网页结构，得到不同天气城市url之间的规律;将html源码解析成DOM树soup，不同的节点开始建立联系；
    利用CSS选择器找到相应的节点提取出标签，get('href')，get_text()得到文本，注意这两个函数都是标签的函数，不是
    列表'''
    url = 'http://www.weather.com.cn/textFC/' + province + '.shtml'
    web = get_HTML(url)
    soup = BeautifulSoup(web, 'html.parser')
    
    weather_day = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(3)')
    weather_day = weather_day[0].get_text()
    weather_night = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(6)')
    weather_night = weather_night[0].get_text()
    if weather_day == weather_night:
        weather = weather_day
    else:
        weather = weather_day + '转' + weather_night
    
    temperature_max = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(5)')
    temperature_max = temperature_max[0].get_text()
    temperature_min = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(8)')
    temperature_min = temperature_min[0].get_text()
    temperature = temperature_min + '°C' + '/' + temperature_max + '°C'
    
    wind_direction = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(4) span:nth-of-type(1)')
    wind_direction = wind_direction[0].get_text()
    wind_force = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(4) span:nth-of-type(2)')
    wind_force = wind_force[0].get_text()
    wind = {'wind_direction': wind_direction, 'wind_force': wind_force}
    
    w = {'weather':weather, 'temperature':temperature, 'wind':wind}
    
    return w

def get_weather_country(province, cityIndex, countryIndex):
    '''通过观察网页结构，得到不同天气城市url之间的规律;将html源码解析成DOM树soup，不同的节点开始建立联系；
    利用CSS选择器找到相应的节点提取出标签，get('href')，get_text()得到文本，注意这两个函数都是标签的函数，不是
    列表'''
    url = 'http://www.weather.com.cn/textFC/' + province + '.shtml'
    web = get_HTML(url)
    soup = BeautifulSoup(web, 'html.parser')
    
    weather_day = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(2)')
    weather_day = weather_day[0].get_text()
    weather_night = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(5)')
    weather_night = weather_night[0].get_text()
    if weather_day == weather_night:
        weather = weather_day
    else:
        weather = weather_day + '转' + weather_night
    
    temperature_max = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(4)')
    temperature_max = temperature_max[0].get_text()
    temperature_min = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(7)')
    temperature_min = temperature_min[0].get_text()
    temperature = temperature_min + '°C' + '/' + temperature_max + '°C'
    
    wind_direction = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(3) span:nth-of-type(1)')
    wind_direction = wind_direction[0].get_text()
    wind_force = soup.select('.conMidtab div:nth-of-type(' + str(cityIndex+1) + ') table tr:nth-of-type(' + str(countryIndex) +') td:nth-of-type(3) span:nth-of-type(2)')
    wind_force = wind_force[0].get_text()
    wind = {'wind_direction': wind_direction, 'wind_force': wind_force}
    
    w = {'weather':weather, 'temperature':temperature, 'wind':wind}
    
    return w

def get_datetime():
    '''日期有date和datetime两种格式，datetime格式精确到小时分钟秒，date年月日；两个datetime对象可以做加减运算；
    得到timedelta对象，它的属性days可返回int格式的天数'''
    begin_time = datetime.date(2018, 5, 20)
    now = datetime.date.today()
    delta = now - begin_time
    days = delta.days
    return days

def get_earthyLove(delta):
    '''在不同的delta下打开不同的txt文件；将txt文本进行处理：去掉读入列表里的\n，去除序号和顿号；在这里去除顿号
    的方法使用的是每一行前几位是数字，事实上用split函数以顿号为分隔符能达到同样的效果'''
    if delta <= 25:
        index = 0
        numbers = 26
        delta_new = delta
    elif delta <= 125:
        index = 1
        numbers = 100
        delta_new = delta-26
    elif delta <= 154:
        index = 2
        numbers = 29
        delta_new = delta-126
    elif delta <= 174:
        index = 3
        numbers = 20
        delta_new = delta-155
    elif delta <= 324:
        index = 4
        numbers = 150
        delta_new = delta-175
    elif delta <= 427:
        index = 5
        numbers = 103
        delta_new = delta-325
    else:
        index = 6
        numbers = 50
        delta_new = delta - 428
    filename = 'earthyLove' + str(index) + '(' + str(numbers) + ').txt'
    with open(filename, 'r') as f:
        lines = []
        org_lines = f.readlines()
        for ln in org_lines:
            if len(ln) != 2:
                lines.append(ln)
        line = lines[delta_new]
# =============================================================================
# 第一次写的比较麻烦，试图识别字符串前多少位是序号，然后用序号+1索引出顿号，从而得到字符串
#         try:
#             headers = int(line[0:3])
#             line = line[4:]
#             line.strip()
#         except ValueError:
#             try:
#                 headers = int(line[0:2])
#                 line = line[3:]
#                 line.strip()
#             except ValueError:
#                 headers = int(line[0])
#                 line = line[2:]
#                 line.strip()
# =============================================================================
    return line.split('、')[1]

def get_jpg(url):
    '''从网页源码上获得jpg的url，可以使用CSS选择器（如果找得到），或者使用正则表达式匹配'''
    html = get_HTML(url)   
# html解析
    soup = BeautifulSoup(html, 'html.parser')
    #jpg_url = soup.select('#preloadBg')[0].get('href')
    jpg_url = soup.select('#bgLink')[0].get('href')
    img_url = url + jpg_url
    return img_url
# =============================================================================
# 正则表达式匹配
#     re_jpg = re.compile(r'url:.{10,90}jpg')
#     jpglist = re.findall(re_jpg, html)
#     if jpglist:
#         jpg_url = jpglist[1].split('/')[1]
#         image_url = url + jpg_url
#         return image_url
#     else:
#         print('failed')
# =============================================================================

def get_img():
    '''这里用到skimage里的io.imread读取来自网页的jpg图片，尝试用pyplot.imread貌似只能读取png格式的文件'''
    url = 'https://cn.bing.com'
    img_url = get_jpg(url)
    img = io.imread(img_url)
    return img
        
def send_to_girlfriend(name, province, city, country):
    '''将所有函数打包，修改工作路径到earthy.txt所在路径, province用来打开url，city用来发该城市的天气，
    country用来发所在区的天气'''
    os.chdir('C:\\Users\\mac\\Desktop\\cufe\\self\\program_learning\wxRobot')

# 搭建城市天气url时需要拼音，而在发消息的时候需要用中文，利用字典实现
    city_name = {'hongkong':'香港', 'beijing':'北京', 'guangzhou':'广州', 'chongqing':'重庆',
            'zhangjiakou':'张家口', 'jinan':'济南'}
    city_index = {'zhangjiakou':3, 'jinan':1, 'beijing':1}
    country_name = {'xuanhua':'宣化区', 'lixia':'历下区', 'haidian':'海淀区', 'changping':'昌平区'}
    country_index = {'xuanhua':2, 'lixia':7, 'haidian':2, 'changping':7}
    cityIndex = city_index[city]
    countryIndex = country_index[country]
    cityName = city_name[city]
    countryName = country_name[country]
    
# 以2018.05.20为第一天，
    datetime = get_datetime() + 1
    delta = datetime - 445
    earthyLove = get_earthyLove(delta)
    # 省会天气
    w = get_weather(province, cityIndex)
    weather = w['weather']
    tem = w['temperature']
    wind_force = w['wind']['wind_force']
    wind_direction = w['wind']['wind_direction']
    # 县区天气
    w_country = get_weather_country(province, cityIndex, countryIndex)
    weather_country = w_country['weather']
    tem_country = w_country['temperature']
    wind_force_country = w_country['wind']['wind_force']
    wind_direction_country = w_country['wind']['wind_direction']
    

# 构建f-string，格式化字符串   
    msg_org = f'First Day, First Message'
    msg_org_datetime= f'你知道嘛，我们已经在一起{datetime}天啦！'
    msg_datetime = f'今天是在一起的第{datetime}天！'
    if wind_direction == wind_force:
        msg_weather_city = f'下面是今天的天气预报：\n今天{cityName}{weather}\n气温:{tem}\n{wind_direction}'
        msg_weather_country = f'下面是今天的天气预报：\n今天{countryName}{weather_country}\n气温:{tem_country}\n{wind_direction_country}'
    else:
        msg_weather_city = f'下面是今天的天气预报：\n今天{cityName}{weather}\n气温:{tem}\n{wind_direction}:{wind_force}\n今天{countryName}{weather_country}\n气温:{tem_country}\n{wind_direction_country}:{wind_force_country}'
#        msg_weather_country = f'今天{countryName}{weather_country}\n气温:{tem_country}\n{wind_direction_country}:{wind_force_country}'
    
    msg_earthyLove = f'{earthyLove}'
    
# itchat只能发送本地图片，无法将数组形式的图片发送，故先用matplotlib.image.imsave储存到本地，这个函数的
# 优点在于可以通过定义存储路径的后缀改变图片格式，同时可以将数组形式的图片保存成图像格式
    wallpaper_index = delta + 20
    image = get_img()
    file_path = 'C:\\Users\\mac\\Desktop\\wallpaper\\th(' + str(wallpaper_index) + ').png'
    matplotlib.image.imsave(file_path, image)

# 模拟登陆网页微信，nickName是昵称，remarkName是备注，每次登陆网页微信的每个好友的UserName是随机分配的，
# 而itchat发送的target需要Username定位，所以先通过备注或昵称得到Username。
    itchat.auto_login(hotReload=True)
    whom = itchat.search_friends(nickName=name)[0]['UserName']
    
    msg_t = 'The first message'

    if delta == 0:
        itchat.send_msg(msg_org, whom)
        itchat.send_msg(msg_org_datetime, whom)
        itchat.send_msg(msg_weather_city, whom)
#        itchat.send_msg(msg_weather_country, whom)
        itchat.send_msg(msg_earthyLove, whom)
    else:
        itchat.send_msg(msg_t, whom)
        itchat.send_msg(msg_datetime, whom) 
        itchat.send_msg(msg_weather_city, whom)
#        itchat.send_msg(msg_weather_country, whom)
        itchat.send_msg(msg_earthyLove, whom)
        itchat.send_image(file_path, whom)

if __name__ == '__main__':
    send_to_girlfriend('J', 'beijing', 'beijing', 'changping')

