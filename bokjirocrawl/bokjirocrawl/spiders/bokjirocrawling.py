# -*- coding: utf-8 -*-
import scrapy


class BokjirocrawlingSpider(scrapy.Spider):
    name = 'bokjirocrawling'
    start_urls = ['http://http://www.bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do/']

    def parse(self, response):
        pass
