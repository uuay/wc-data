# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WelfareItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    servicename = scrapy.Field() #혜택명
    link = scrapy.Field()
    institution = scrapy.Field() #기관명
    pass
