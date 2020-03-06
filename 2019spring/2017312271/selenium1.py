from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


driver = webdriver.Firefox()
driver.get("http://xuanke.cufe.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t=1558620354349")
driver.find_element_by_id("yhm").send_keys("2017312271")
driver.find_element_by_id("mm").send_keys("yangyiyi3247")
driver.find_element_by_id("dl").click()

WebDriverWait(driver, 20, 0.5).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn_yd']")))
driver.find_element_by_id("btn_yd").click()
driver.find_element_by_xpath("//li[@class='dropdown'][3]/a[@id='drop1']").click()
time.sleep(3)
driver.find_element_by_xpath("//li[@class='dropdown'][3]/ul/li").click()


'''
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("Firefox Headless Browser Invoked")

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("李丰 中央财经大学")'''
