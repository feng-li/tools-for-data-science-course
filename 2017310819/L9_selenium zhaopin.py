# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
import time
#from bs4 import BeautifulSoup
#import csv

#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC 
#from selenium.common.exceptions import NoSuchElementException

firefox = webdriver.Firefox()
time.sleep(3)
link = 'https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3&sf=0&st=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0',
           'Host':'desktop-bucket.zhaopin.cn'}
firefox.get(link)
firefox.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(5)
list1 = []
for i in range(1,3):
    a = firefox.find_element_by_xpath("/html/body/div/div/div[4]/div[3]/div[2]/div/div["+"i"+"]/div/a/div[1]/div[1]/span")
    list1.append(a.text)
    a.click()
    time.sleep(3)
    handles = firefox.window_handles
    firefox.switch_to.window(handles[1])
    b1 = firefox.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[2]').text
    print(b1)
    firefox.close()
    firefox.switch_to.window(handles[0])
    output_list = [(a.text,b1)]      
    with open('zhaopin.csv.csv','a+',encoding='utf_8_sig',newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(output_list)
