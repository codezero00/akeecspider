# -*- coding: utf-8 -*-
import scrapy
from onespider.items import NSGirlItem, NSAlbumsItem, NSPhotoListItem, NSItem
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
    #
    #     # girls = response.xpath('1/2/3')
    #     for each_girl in girls:
    #         item = NSItem()
    #         item['siteURL'] = each_girl
    #         yield Request(each_girl, callback=self.parse_2)




    def start_requests(self):
        """
        start capture from nsurl
        :return:
        """
        siteurls = []
        with open('nsurl.txt', 'r') as f:
            siteurls = f.read().split('\n')
        for i in siteurls:
            url = i
            yield Request(url, callback=self.parse_1)

    def parse_1(self, response):
        """
        page person
        :param response:
        :return:
        """
        # items=[]
        item = NSGirlItem()
        item["girlname"] = response.xpath('//*[@id="post"]/div[2]/div/div[1]/h1/text()').extract()[0]
        item["girlimgurl"] = response.xpath('//*[@id="post"]/div[2]/div/div[3]/a/img/@src').extract()[0]
        item["girltable"] = response.xpath('//*[@id="post"]/div[2]/div/div[4]/table').extract()[0]
        item["girldetail"] = response.xpath('//*[@id="post"]/div[5]/div/div[1]/div[2]/text()').extract()
        # items.append(item)
        # xzurls = response.xpath('//*[@id="post"]/div[8]/div/div[3]/ul/li/div[1]/a/@href').extract()
        elements = response.xpath('//*[@class="igalleryli"]')
        yield item
        for element in elements:
            xzitem = NSAlbumsItem()
            url = element.xpath('./div[1]/a/@href').extract()[0]
            xzurl = 'https://www.nvshens.com' + url
            xztitle = element.xpath('//img/@title').extract()[0]
            xzimgurl = element.xpath('//img/@data-original').extract()[0]
            xzitem['xzurl'] = xzurl
            xzitem['xzname'] = xztitle
            xzitem['xzimgurl'] = xzimgurl
            yield Request(xzurl, meta={'xzitem': xzitem}, callback=self.parse_2)

    def parse_2(self, response):
        """
        title: <h1 id="htilte">营养过剩！巴西女孩「Jordana Lopes Vucetic」发育超前</h1>
        desc: <div id="ddesc" class="albumInfo">這位有著傲人身材的妹子叫做《Jordana Lopes Vucetic》，「未熟女孩」……沒错！就是「未熟女孩」。你们猜猜眼前的這位妹子，实际年龄是多少吧！...........................只有14岁！</div>
        :param response:
        :return:
        """
        print(response)
        print(response.meta['xzitem'].name)
        # xzitem = NSAlbumsItem()
        xzitem = response.meta['xzitem']
        xzitem['xzdesc'] = response.xpath('//*[@id="ddesc"]/text()').extract()[0]
        xzitem['xztags'] = response.xpath('//*[@id="utag"]/li/a/text()').extract()
        print(xzitem)
        for i in range(1, 15):
            photourl = xzitem['xzurl']+str(i)+'.html'
            yield Request(photourl, meta={'xzitem': xzitem}, callback=self.parse_3)

    def parse_3(self, response):
        photoimgurllist = response.xpath('//*[@id="hgallery"]/img/@src').extract()
        print(photoimgurllist)
        xzitem = response.meta['xzitem']
        imgitem = NSPhotoListItem()
        for i in photoimgurllist:
            imgitem['xzname'] = xzitem['xzname']
            imgitem['xzimgs'] = i
            yield  imgitem

