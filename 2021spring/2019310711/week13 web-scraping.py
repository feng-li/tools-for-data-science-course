import scrapy

    class ArticleSpider(scrapy.Spider):
        name='article'

        def start_requests(self):
            urls = [
                'https://wiki.mbalib.com/wiki/%E5%B8%83%E6%9C%97%E8%BF%90%E5%8A%A8'
                ]
            return [scrapy.Request(url=url, callback=self.parse) for url in urls]

        def parse(self, response):
            url = response.url
            title = response.css('h1::text').extract_first()
            print('URL is: {}'.format(url))
            print('Title is: {}'.format(title))
