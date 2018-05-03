# -*- coding: utf-8 -*-
import scrapy
from onespider.items import OnespiderItem, MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        print(response)
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:

            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            item['url'] = each_movie.xpath('./h5/a/@href').extract()[0]
            item['status'] = each_movie.xpath('./span[1]/font/text()').extract()[0] if len(each_movie.xpath('./span[1]/font/text()').extract()) >= 1 else each_movie.xpath('./span[1]/text()').extract()[0]
            item['tags'] = each_movie.xpath('./span[2]/text()').extract()[0]
            item['tvstation'] = each_movie.xpath('./span[3]/text()').extract()[0]
            # item['updatetime'] = len(each_movie.xpath('./div[2]/font/text()').extract()) # each_movie.xpath('./div[2]/font/text()').extract()[0] if len(each_movie.xpath('./div[2]/font/text()').extract()) >= 1 else each_movie.xpath('./div[2]/text()').extract()[0]
            item['updatetime'] = each_movie.xpath('./div[2]/font/text()').extract()[0] if len(each_movie.xpath('./div[2]/font/text()').extract()) >= 1 else each_movie.xpath('./div[2]/text()').extract()[0]
            yield item
