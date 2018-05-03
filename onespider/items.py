# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OnespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

class MovieItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    tags = scrapy.Field()
    tvstation = scrapy.Field()
    updatetime = scrapy.Field()


class XhItem(scrapy.Item):
    addr = scrapy.Field()
    name = scrapy.Field()