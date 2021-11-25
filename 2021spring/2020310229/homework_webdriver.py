# 这个程序用来登录中央财经大学门户网站

from selenium import webdriver
def get_info():
    username = input("请输入用户名： ")
    password = input("请输入密码： ")
    return [username, password]

def log_in(info):
    username = info[0]
    password = info[1]
    url = "https://authserver.cufe.edu.cn/authserver/login?service=https%3A%2F%2Fi.cufe.edu.cn%3A443%2Flogin"

    driver = webdriver.Firefox()
    driver.get(url=url)
    driver.find_element_by_id("username").send_keys("2020310229")
    driver.find_element_by_id("password").send_keys("Ljc020515")
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[4]/div/form/p/button").click()
    return 0


if __name__ == '__main__':
    info = get_info()
    log_in(info)

