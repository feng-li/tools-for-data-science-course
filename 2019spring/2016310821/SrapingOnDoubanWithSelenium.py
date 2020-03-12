#! /usr/bin python3


from selenium import webdriver
from collections import OrderedDict
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("Firefox Headless Browser Invoked")

driver = webdriver.Firefox()
driver.get('https://movie.douban.com')
wait = WebDriverWait(driver, 10)
inp = wait.until(EC.presence_of_element_located((By.ID, 'inp-query')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.inp-btn > input:nth-child(1)')))

driver.find_element_by_id('inp-query').send_keys("周星驰")
driver.find_elements_by_xpath('//div[@class = "inp-btn"]/input')[0].click()

personalInf = driver.find_elements_by_xpath('//div[@class = "sc-bxivhb hRIaFd"]/div[@class = "item-root"]/div[@class = "detail"]')[0]
name, collect, tags = personalInf.text.split('\n')


works = OrderedDict()

while(True):
    worklist = driver.find_elements_by_xpath('//div[@class = "sc-bZQynM fYArNj sc-bxivhb hRIaFd"]/div[@class = "item-root"]/div[@class = "detail"]')
    for item in worklist:
        title = item.find_elements_by_xpath('div[@class = "title"]/a')[0].text
        rating_nums = item.find_elements_by_xpath('div[@class = "rating sc-bwzfXH hxNRHc"]/span[@class = "rating_nums"]')[0].text
        rating_people = item.find_elements_by_xpath('div[@class = "rating sc-bwzfXH hxNRHc"]/span[@class = "pl"]')[0].text
        tags = item.find_elements_by_xpath('div[@class = "meta abstract"]')[0].text
        actors = item.find_elements_by_xpath('div[@class = "meta abstract_2"]')[0].text
        works[title] = [title, rating_nums, rating_people, tags, actors]

    next_button = driver.find_elements_by_xpath('//a[@class = "next"]')
    next_button[0].click()
    if len(next_button)>0:
        next_button[0].click()
    else:
        break
    print('on')
    
works_StephenChow = pd.DataFrame(works, columns = ['title', 'rating_nums', 'rating_people', 'tags', 'actors'])
works_StephenChow.to_csv('/home/luo/Desktop/works_StephenChow.csv', index = True, sep = '\001')

driver.close()
