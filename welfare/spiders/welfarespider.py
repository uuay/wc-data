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
     
        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[1]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[1]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[2]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[2]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[3]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[3]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[4]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[4]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[5]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[5]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        val1 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[6]/strong)')
        val2 = response.xpath('string(//section[@id="contents"]/div[2]/div/ul/li[6]/div)')

        if val1.get('data') == '사업목적':
            item['purpose'] = val2.get('data')
        elif val1.get('data') == '지원대상':
            item['target'] = val2.get('data')
        elif val1.get('data') == '지원내용':
            item['content'] = val2.get('data')
        elif val1.get('data') == '신청방법':
            item['howto'] = val2.get('data')
        elif val1.get('data') == '제출서류':
            item['docs'] = val2.get('data')
        elif val1.get('data') == '기타':
            item['etc'] = val2.get('data')

        yield item