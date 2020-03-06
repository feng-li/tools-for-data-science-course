from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=options)
driver.get("http://172.1.52.1/index.php")

f = open("CVE.txt", 'r')
fw = open("result.txt", 'w')

lines = f.readlines()
for hint in lines:
    driver.find_element_by_xpath("//input[@name='id']").send_keys(hint.strip())
    driver.find_element_by_xpath("//input[@type='submit']").click()

    result = driver.find_element_by_xpath("//body")
    fw.write(hint.strip()+"\n")
    fw.write(result.text+"\n")

fw.close()
f.close()
