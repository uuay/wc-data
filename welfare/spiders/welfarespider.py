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

    def parse(self, response):
        for href in response.css("contents > div.listTbl > table > tbody > tr:nth-child > td.txtL > a::attr('href)"):
            #contents > div.listTbl > table > tbody > tr:nth-child(1) > td.txtL > a
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_bokjiro)
            
    def parse_bokjiro(self, response):
        for sel in response.xpath('//section[@id="contents"]/div[2]'):
            item = WelfareItem()

            item['service'] = sel.xpath('/table/tbody/tr[1]/td/strong/text()').get()
            #contents > div.viewTbl.shareViewTbl > table > tbody > tr:nth-child(1) > td > strong
            item['name'] = sel.xpath('/table/tbody/tr[2]/td/a[1]/text()').get()
            item['serviceCont'] = sel.xpath('/div/ul/li[1]/div/text()').get()
            yield item