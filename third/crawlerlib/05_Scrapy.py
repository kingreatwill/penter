# https://github.com/scrapy/scrapy
# https://doc.scrapy.org/en/latest/intro/tutorial.html
# pip install scrapy
import scrapy
# scrapy startproject tutorial即可创建一个tutorial文件夹
# scrapy runspider 04_Scrapy.py

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)