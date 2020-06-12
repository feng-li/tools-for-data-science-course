from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumCrawl:
    def __init__(self, username, pw):
        self.options = Options()
        # self.options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)
        self.url = 'https://mail.qq.com/'
        self.username = username
        self.pw = pw

    def run(self):
        # 登录
        self.driver.get(self.url)
        self.driver.switch_to.frame(
            self.driver.find_element_by_id('login_frame')
        )
        bt_user_name = self.driver.find_element_by_xpath('//*[@id="u"]')
        bt_user_name.send_keys(self.username)
        bt_pw = self.driver.find_element_by_xpath('//*[@id="p"]')
        bt_pw.send_keys(self.pw)
        bt_login = self.driver.find_element_by_xpath('//*[@id="login_button"]')
        bt_login.click()
        # 进入收件箱
        time.sleep(5)  # 等待元素加载出来
        self.driver.switch_to.frame(
            self.driver.find_element_by_id('mainFrame')
        )
        self.driver.find_element_by_xpath('//*[@id="folder_1"]').click()


SeleniumCrawl('', '').run()
