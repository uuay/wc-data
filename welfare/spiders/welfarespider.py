# -*- coding: utf-8 -*-

__author__ = '2oosoo'

import scrapy

from welfare.items import WelfareItem

class welfarespider(scrapy.Spider):
    name = "welfareCrawler"
    start_urls = ["http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do"]

    def start_requests(self):
        for i in range(1, 43, 1):
            yield scrapy.Request(
                "http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do?searchCondition=&searchKeyword=&srchDuration=&stDate=&endDate=&pageUnit=10&endSvrEsc=0&intClIdStr=&orderCol=MODDATE&orderBy=DESC&recordCountPerPage=10&viewEndService=&pageIndex=%d" %i, 
                self.parse)

    def parse(self, response):
        for sel in response.xpath('//section[@id="contents"]/div[5]/table/tbody/tr'):
            request = scrapy.Request(
                "http://bokjiro.go.kr/" + sel.xpath('td[@class="txtL"]/a/@href').extract()[0], 
                callback=self.parse_bokjiro)
            yield request

    def parse_bokjiro(self, response):
        item = WelfareItem()
        service = response.xpath('//section[@id="contents"]/div[2]/table/tbody/tr[1]/td/strong/text()')
        if service:
            item['service'] = service.extract()
        purpose = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[1]/div/text()')
        if purpose:
            item['purpose'] = purpose.extract()
        target = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[2]/div/text()')
        if target:
            item['target'] = target.extract()
        content = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[3]/div/text()')
        if content:
            item['content'] = content.extract()
        howto = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[4]/div/text()')
        if howto:
            item['howto'] = howto.extract()
        docs = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[5]/div/text()')
        if docs:
            item['docs'] = docs.extract()
        etc = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[6]/div/text()')
        if etc:
            item['etc'] = etc.extract()
        # if response.xpath('//section[@id="contents"]/div[2]/table/tbody/tr[1]/td/strong/text()').extract()[0] is not None:
        #     item['service'] = response.xpath('//section[@id="contents"]/div[2]/table/tbody/tr[1]/td/strong/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[1]/div/text()').extract()[0] is not None:
        #     item['purpose'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[1]/div/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[2]/div/text()').extract()[0] is not None:
        #     item['target'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[2]/div/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[3]/div/text()').extract()[0] is not None:
        #     item['content'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[3]/div/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[4]/div/text()').extract()[0] is not None:
        #     item['howto'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[4]/div/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[5]/div/text()').extract()[0] is not None:
        #     item['docs'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[5]/div/text()').extract()[0]
        # if response.xpath('//section[@id="contents"]/div[2]/div/ul/li[6]/div/text()').extract()[0] is not None:
        #     item['etc'] = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[6]/div/text()').extract()[0]
        yield item