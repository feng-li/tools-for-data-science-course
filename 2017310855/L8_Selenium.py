# sudo pip3 install selenium
from selenium import webdriver
d = webdriver.Safari()
# dir(driver)
d.maximize_window()
d.get("https://www.baidu.com/")
# Auto func def
# import time
# time.sleep(2)
d.find_element_by_id("kw").send_keys("foxmail")
d.find_element_by_id("su").click()
d.find_element_by_xpath('//div[@id="1"]/h3/a').click()
# d.switch_to.default_content()
d.switch_to.frame("login_frame")
d.find_element_by_xpath('//div[@id="switch"]/a').click()
# d.find_element_by_id("u").clear()
d.find_element_by_id("u").send_keys("764211922")
# d.find_element_by_id("p").clear()
d.find_element_by_id("p").send_keys("*********")
d.find_element_by_id("login_button").click()
# d.close()
