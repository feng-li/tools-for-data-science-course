from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.ilovepdf.com/login")
#找了很久才找到全是inputid引导的
driver.find_element_by_id("loginEmail").send_keys("2017310901@email.cufe.edu.cn")
driver.find_element_by_id("inputPasswordAuth").send_keys("d20000601")
driver.find_element_by_id("loginBtn").click()
#如果不是inputid而是class类driver.find_element_by_class_name("login-btn").click()
