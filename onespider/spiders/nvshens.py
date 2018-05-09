# -*- coding: utf-8 -*-
import scrapy
from onespider.items import NSItem
import re

class MeijuSpider(scrapy.Spider):
    name = 'ns'
    allowed_domains = ['nvshens.com']
    start_urls = ['https://www.nvshens.com/sitemap.xml']

    def parse(self, response):
        print(response)
        pattern = re.compile(r'<loc>(.*?)</loc>', re.S)
        girls = re.findall(pattern, response.text)
        # girls = response.xpath('1/2/3')
        for each_girl in girls:
            item = NSItem()
            item['siteURL'] = each_girl
            yield item
