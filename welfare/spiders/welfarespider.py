# -*- coding: utf-8 -*-

__author__ = '2oosoo'

import scrapy

from welfare.items import WelfareItem

class welfarespider(scrapy.Spider):
    name = "welfareCrawler"
    start_urls = ["http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do"]

    def start_requests(self):
        for i in range(1, 100, 1) :
            yield scrapy.Request("http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do?searchCondition=&searchKeyword=&srchDuration=&stDate=&endDate=&pageUnit=10&endSvrEsc=0&intClIdStr=&orderCol=MODDATE&orderBy=DESC&recordCountPerPage=10&viewEndService=&pageIndex=%d" %i, self.parse_bokjiro)

    def parse_bokjiro(self, response):
        for sel in response.xpath('//section[@id="contents"]/div[5]/table/tbody/tr'):
            item = WelfareItem()

            item['servicename'] = sel.xpath('td[@class="txtL"]/a/text()').extract()[0]
            item['link'] = "http://bokjiro.go.kr/" + sel.xpath('td[@class="txtL"]/a/@href').extract()[0]
            item['institution'] = sel.xpath('td[3]/text()').extract()[0]
            
            yield item