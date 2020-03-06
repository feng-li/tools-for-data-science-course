# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:32:15 2019

@author: tutuxy
"""

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.bing.com/")
driver.find_element_by_id("sb_form_q").send_keys("feng li")
driver.find_element_by_id("sb_form_go").click()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("Firefox Headless Browser Invoked")

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("李丰 中央财经大学")

driver.find_element_by_id("su").click()
results = driver.find_elements_by_xpath('//div[@srcid="1599"]/h3/a')

for result in results:
    print(result.text)

driver.close()
