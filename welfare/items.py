# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WelfareItem(scrapy.Item):
    service = scrapy.Field() 
    name = scrapy.Field()
    purpose = scrapy.Field()
    target = scrapy.Field()
    content = scrapy.Field()
    howto = scrapy.Field()
    docs = scrapy.Field()
    etc = scrapy.Field()