from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException


list3 = ['环保','污染','处罚','违规','处罚','债务','违约','纠纷','毁约','拖欠','安全性','质量','违规','造假']
for ii in list3:
    firefox = webdriver.Firefox()
    time.sleep(3)

    link = 'http://news-bos.cdn.bcebos.com/mvideo/pcnews_advanced.html?v=23'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0',
               'Host':'gss0.bdstatic.com'}

    firefox.get(link)
    firefox.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/input").send_keys('盾安MTN001')
    
    firefox.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[3]/input").send_keys(ii)
    firefox.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[2]/td[3]/input[1]").click()
    firefox.find_element_by_xpath('//*[@id="begin_date"]').clear()
    firefox.find_element_by_xpath('//*[@id="end_date"]').clear()
    firefox.find_element_by_xpath('//*[@id="begin_date"]').send_keys('2016-1-1')
    firefox.find_element_by_xpath('//*[@id="end_date"]').send_keys('2016-12-31')
    firefox.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(3)
    for i in range(20):
        try:
            a1 = firefox.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div['+str(i)+']/h3/a').text
            b1 = firefox.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div['+str(i)+']/div/p').text
            c1 = firefox.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div['+str(i)+']/div').text                                                     
            d1 = firefox.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div['+str(i)+']/h3/a').get_attribute('href')

        except NoSuchElementException:
            a1 = '-'
            b1 = '-'
            c1 = '-'
            d1 = '-'
        output_list = [(a1,b1,c1,d1)]        
        with open('盾安MTN0011.csv.csv','a+',encoding='utf_8_sig',newline='') as csvfile:
            w = csv.writer(csvfile)
            w.writerows(output_list)
    
