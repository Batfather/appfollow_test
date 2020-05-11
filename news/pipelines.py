import pymongo
import logging
from datetime import datetime
from scrapy.exceptions import DropItem

logger = logging.getLogger("scrapy")


class MongoDBPipeline:

    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client.appfollow
        self.collection = self.db.news

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            item['created_at'] = datetime.utcnow()
            self.collection.update({'title': item['title']}, {'$setOnInsert': dict(item)}, upsert=True)
            logger.info("News added to MongoDB database!")
        return item


