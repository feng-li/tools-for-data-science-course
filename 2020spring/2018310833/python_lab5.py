from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.switch_to.frame("login_frame")
driver.find_element_by_xpath('//*[@id="u"]').send_keys("账号")
driver.find_element_by_xpath('//*[@id="p"]').send_keys("密码")
driver.find_element_by_xpath('//*[@id="login_button"]').click()