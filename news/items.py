# -*- coding: utf-8 -*-

import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    created_at = scrapy.Field()
