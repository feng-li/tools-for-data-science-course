import requests, logging, os, time
import pandas as pd
from lxml import etree


def crawl_full(url, old_url):
    response = requests.get(url, headers={
        'referer': old_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    })
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    content = ''.join(html.xpath('//div[@class="article"]//p//text()')).replace('\n', '')
    return content


def crawl(search_word, page):
    url = 'https://search.sina.com.cn/?q=%s&c=news&from=&col=&range=all&source=&country=&size=10&time=&dpc=0&a=&ps=0&pf=0&page=%s' % (
        search_word, page)
    response = requests.get(url, headers={
        'referer': 'https://search.sina.com.cn/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    })
    html = etree.HTML(response.text)
    items = html.xpath('//*[@id="result"]//div[@class="box-result clearfix"]')
    return save([parse(item, response.url) for item in items])


def parse(response, old_url):
    result = dict()
    result['title'] = response.xpath('.//h2/a/text()')[0]
    result['url'] = response.xpath('.//h2/a/@href')[0]
    temp = response.xpath('.//h2/span/text()')[0].split()
    result['source'] = temp[0]
    result['date'] = temp[1]
    result['time'] = temp[2]
    result['content'] = crawl_full(result['url'], old_url)
    return result


def save(result_list: list):
    target_file = '新冠文本.csv'
    mode = os.path.exists(os.path.join(target_file))
    df = pd.DataFrame(result_list)
    df.to_csv(target_file, encoding='utf-8', index=False,
              mode='a' if mode else 'w',
              header=not mode)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Initializing result.csv')
    if os.path.exists(os.path.join('result.csv')):
        os.remove(os.path.join('result.csv'))
    logging.info('Initialed result.csv')
    for page in range(0, 10):
        search_word = '新冠病毒'
        logging.info('Crawling 第%s页 %s' % (page, search_word))
        crawl(search_word, page)
        logging.info('Crawled 第%s页 %s' % (page, search_word))
        time.sleep(1)
