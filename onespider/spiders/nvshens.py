# -*- coding: utf-8 -*-
import scrapy
from onespider.items import NSItem
from scrapy.http import Request
import re

class MeijuSpider(scrapy.Spider):
    name = 'ns'
    allowed_domains = ['nvshens.com']
    start_urls = ['https://www.nvshens.com/sitemap.xml']

    # def parse(self, response):
    #     print(response)
    #     pattern = re.compile(r'<loc>(.*?)</loc>', re.S)
    #     girls = re.findall(pattern, response.text)
    #     # girls = response.xpath('1/2/3')
    #     for each_girl in girls:
    #         item = NSItem()
    #         item['siteURL'] = each_girl
    #         yield item

    # def parse(self, response):
    #     pattern = re.compile(r'<loc>(.*?)</loc>', re.S)
    #     girls = re.findall(pattern, response.text)
    #     # girls = response.xpath('1/2/3')
    #     for each_girl in girls:
    #         item = NSItem()
    #         item['siteURL'] = each_girl
    #         yield Request(each_girl, callback=self.parse_2)

    def start_requests(self):
        siteurls = []
        with open('nsurl.txt','r') as f:
            siteurls = f.read().split('\n')
        for i in siteurls:
            url = i
            yield Request(url, callback=self.parse_2)

    def parse_2(self, response):
        items=[]
        item = NSItem()
        item["girlname"] = response.xpath('//*[@id="post"]/div[2]/div/div[1]/h1/text()').extract()[0]
        item["girlimgurl"] = response.xpath('//*[@id="post"]/div[2]/div/div[3]/a/img/@src').extract()[0]
        item["girltable"] = response.xpath('//*[@id="post"]/div[2]/div/div[4]/table').extract()[0]
        item["girldetail"] = response.xpath('//*[@id="post"]/div[5]/div/div[1]/div[2]/text()').extract()
        items.append(item)
        xzurls = response.xpath('//*[@id="post"]/div[8]/div/div[3]/ul/li/div[1]/a/@href').extract()
        for item in items:
            yield item
        for url in xzurls:
            yield Request(url, callback=self.parse_3)

    def parse_3(self, response):
        print(response)
        # item = NSItem()
        # item[""] = response.xpath()
