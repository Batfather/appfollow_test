# -*- coding: utf-8 -*-
import os

# SCRAPY SETTINGS
BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'news.pipelines.MongoDBPipeline': 0,
}

# MONGODB SETTINGS
MONGO_URI = 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/' \
                                  + os.environ['MONGODB_DATABASE']
