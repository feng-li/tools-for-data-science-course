from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://mail.qq.com/")

driver.switch_to.frame("login_frame") 
# 用户名 密码
elem_user = driver.find_element_by_name("u")
elem_user.send_keys("xxxxxxxxxx@qq.com")   
elem_pwd = driver.find_element_by_name("p")
elem_pwd.send_keys("xxxxxxxxxxx")            
elem_but = driver.find_element_by_id("login_button")
elem_but.click()

