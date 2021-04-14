from selenium import webdriver
import csv
import time
driver = webdriver.Firefox()
url="https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&sf=0&st=0"
driver.get(url)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(1)
for i in range(50):
    sal = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[3]/div[2]/div/div[i]/div/a/div[2]/div[1]/p").text
    loc = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[3]/div[2]/div/div[i]/div/a/div[2]/div[1]/ul/li[1]").text
    exp = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[3]/div[2]/div/div[i]/div/a/div[2]/div[1]/ul/li[2]").text
    edu = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[3]/div[2]/div/div[i]/div/a/div[2]/div[1]/ul/li[3]").text
    output_list = [(sal,loc,exp,edu)]    
    with open('C:\\Users\\Administrator\\Desktop\\salarydata.csv','a+',encoding='utf_8_sig',newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(output_list)
driver.close()
