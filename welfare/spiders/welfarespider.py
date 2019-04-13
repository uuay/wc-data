# -*- coding: utf-8 -*-

__author__ = '2oosoo'

import scrapy

from welfare.items import WelfareItem

class welfarespider(scrapy.Spider):
    name = "welfareCrawler"
    start_urls = ["http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do"]

    def start_requests(self):
        for i in range(1, 4, 1):
            yield scrapy.Request(
                "http://bokjiro.go.kr/nwel/helpus/welsha/selectWelShaInfoBbrdMngList.do?searchCondition=&searchKeyword=&srchDuration=&stDate=&endDate=&pageUnit=10&endSvrEsc=0&intClIdStr=&orderCol=MODDATE&orderBy=DESC&recordCountPerPage=10&viewEndService=&pageIndex=%d" %i, 
                self.parse)

    def parse(self, response):
        for sel in response.xpath('//section[@id="contents"]/div[5]/table/tbody/tr'):
            request = scrapy.Request(
                "http://bokjiro.go.kr/" + sel.xpath('td[@class="txtL"]/a/@href').extract()[0], 
                callback=self.parse_bokjiro)
            yield request
    # name이 a태그일 경우의 xPath                    //*[@id="contents"]/div[2]/table/tbody/tr[2]/td/a[1]
    # name이 테이블의 td 태그일 경우의 xPath           //*[@id="contents"]/div[2]/table/tbody/tr[2]/td
    def parse_bokjiro(self, response):
        item = WelfareItem()
        service = response.xpath('//section[@id="contents"]/div[2]/table/tbody/tr[1]/td/strong/text()')
        if service:
            item['service'] = service.extract()

        name = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[2]/td/a[1]/text()')
        if name:
            item['name'] = name.extract()
        else:
            item['name'] = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[2]/td/text()').extract()
     
        val1 = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[1]/strong/text()')
        val2 = response.xpath('//section[@id="contents"]/div[2]/div/ul/li[1]/div/text()')
        if val1 == '사업목적':
            purpose = val2
            item['purpose'] = purpose.extract()
        elif val1 == '지원대상':
            target = val2
            item['target'] = target.extract()
        elif val1 == '지원내용':
            content = val2
            item['content'] = content.extract()
        elif val1 == '신청방법':
            howto = val2
            item['howto'] = howto.extract()
        elif val1 == '제출서류':
            docs = val2
            item['docs'] = docs.extract()
        elif val1 == '기타':
            etc = val2
            item['etc'] = etc.extract()

        # if purpose:
        #     item['purpose'] = purpose.extract()

        # if target:
        #     item['target'] = target.extract()

        # if content:
        #     item['content'] = content.extract()

        # if howto:
        #     item['howto'] = howto.extract()

        # if docs:
        #     item['docs'] = docs.extract()

        # if etc:
        #     item['etc'] = etc.extract()
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