from scrapy import Spider
from scrapy.selector import Selector

from news.items import NewsItem


class NewsSpider(Spider):
    name = 'news'
    allowed_domains = ['news.ycombinator.com']
    start_urls = [
        'https://news.ycombinator.com/'
    ]

    def parse(self, response):
        news = Selector(response).xpath('//tr[@class="athing"]/td/a')
        for news_item in news:
            item = NewsItem()
            item['title'] = news_item.xpath('text()').extract()[0]
            item['url'] = news_item.xpath('@href').extract()[0]
            yield item

