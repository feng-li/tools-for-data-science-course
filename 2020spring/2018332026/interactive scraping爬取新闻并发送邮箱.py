import requests, json
from bs4 import BeautifulSoup
import yagmail
import schedule,time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

def get_page_url(num):  # 定义一个处理url的函数，用于存储各页的url列表
    url_list = []
    url_list.append('https://temp.163.com/special/00804KVA/cm_guonei.js?callback=data_callback')    # 第一页地址
    for page in range(2, num + 1):
        url = 'https://temp.163.com/special/00804KVA/cm_guonei_0{}.js?callback=data_callback'.format(page)
        url_list.append(url)
    return url_list

def get_data(url):  # 定义一个函数,用JSON方法解析url列表，获得标题新闻的源地址url
    html = requests.get(url)
    start = html.text.index('[')  # 通过索引方法，获取有效字段开始位置
    end = html.text.index('])') + 1
    html_json = html.text[start:end]  # 通过字符串切片方法，获取符合JSON语法的html数据
    news_count = 0       # 定义一个记录新闻条数的变量
    for data in json.loads(html_json):  # 用JSON方法解析获取的接口数据
        dic = {}  # 定义一个空字典，用于存储逐条新闻数据
        dic['title'] = data['title']    # 获取新闻标题并给字典中关键字赋值
        dic['docurl'] = data['docurl']  # 获取新闻并链接地址url并给字典中关键字赋值
        dic['source'] = data['source']  # 获取新闻来源并给字典中关键字赋值
        dic['time'] = data['time'].split(' ')[0]  # 获取新闻日期并赋值，这里去掉时间信息'05/15/2020 16:35:01'
        str = ''  # 定义一个空字符串，用于存储新闻标签字符
        for key in data['keywords']:    # 逐一获取新闻关键字信息内容
            str = str + ' ' + key['keyname']  # 组合新闻关键字字符串
        dic['keyword'] = str  # 获取新闻关键字并给字典中关键字赋值
        if dic['keyword'] == '':   # 如果keyword数据为空，则字典中删除该关键字
            del dic['keyword']
        if dic['docurl'] != '':
            dic['content'] = get_content(data['docurl'])[1]    # 调用get_content()函数获取新闻正文内容，传入新闻地址参数
            dic['author'] = get_content(data['docurl'])[0]    # 调用get_content()函数获取新闻正文内容，传入新闻地址参数
            if dic['author'] == '':   # 如果Author数据为空，则字典中删除该关键字
                del dic['author']
        save_to_file(dic)   # 调用函数将该条新闻写入文件
        news_count += 1     # 爬取新闻条数计数
        if news_count <= 30:        # 设置爬取新闻的条数
            print(f'存储第{news_count}条新闻到text文件成功！')  # 实时显示爬取新闻进程
        else:
            break

def get_content(url):   # 函数用于获取单条新闻相关数据
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    if html.url.find('news') > 0:  # 区分url为"https://news.163.com/......"进行处理
        author = soup.select('.ep-source.cDGray span')[1].get_text()    # 获取新闻编辑及作者信息
        content = soup.select('div .post_text')[0].get_text()   # 获取新闻正文
        content = ''.join(content.split())   # 对数据进行消空、去换行等，再组合成文本字符串
        return author,content    # 返回函数结果，元组数据
    elif html.url.find('dy') > 0:   # 区分url为"https://dy.163.com/......"进行处理
        author = ""  # 此类新闻页无责任编辑和作者信息
        content = soup.select('div.content')[0].get_text()  # 获取新闻正文
        content = ''.join(content.split())  # 对数据进行消空、去换行等，再组合成文本字符串
        return author,content    # 返回函数结果，元组数据
    elif html.url.find('v') > 0:   # 区分url为"https://v.163.com/......"进行处理
        author = ""     # 此类新闻页无责任编辑和作者信息
        content = ""    # 此类新闻页无责任编辑和作者信息
        return author, content  # 返回函数结果，元组数据
    else:
        return

def save_to_file(result):  # 函数用于存储新闻到txt文件
        with open('./News163-top30.txt', 'a+', encoding='utf-8') as f:   # 打开文件，命名为“网易新闻.txt”
            f.write(json.dumps(result, ensure_ascii=False) + '\n')  # 逐条写入数据


def sent_news():    # 定义一个给邮箱发新闻的函数
    yag = yagmail.SMTP(user='ylq_bk@163.com', host='smtp.163.com')
    contents = ['News163-top30.txt']
    yag.send('ylq_bk@qq.com', '每日新闻', contents)       # 附件发送
    print('新闻发送成功')

def main_news():
    url_list = get_page_url(1)  # 设置爬取的页数为2页，并调用页面处理函数
    page_num = 1
    for url in url_list:
        print(f"正在爬取第 {page_num} 页新闻......")
        get_data(url)
        page_num += 1
    print('-'*20 + ' 今日新闻30条已爬取完毕，自动发送到您的邮箱中 '+'-'*20)
    sent_news()

schedule.every().day.at('08:00').do(main_news)       # 每天上午08:00启动发送新闻任务

while True:     # 通过无限循环语句，确保程序始终处于运行状态
    schedule.run_pending()
    time.sleep(1)
