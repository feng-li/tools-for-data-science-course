from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
sleep(5)
#打开网页
driver.get("https://login.nipic.com/login?backurl=http://user.nipic.com/?xinshou=1")
sleep(5)

#输入用户名
driver.find_element_by_id("UserName").send_keys("ann3333")
sleep(10)
#输入密码
driver.find_element_by_id("PassWord").send_keys("20000303")
sleep(5)
#登入

driver.find_element_by_class_name("new-login-btn").click()
