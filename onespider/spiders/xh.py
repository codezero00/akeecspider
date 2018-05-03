# -*- coding: utf-8 -*-
import scrapy
from onespider.items import OnespiderItem, MovieItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        print(response)
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            item['name']=each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
