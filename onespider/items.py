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
    siteURL = scrapy.Field()  # 首页中各MM的URL
    pageURL = scrapy.Field()  # 每一张图片入口URL
    detailURL = scrapy.Field()  # 图片原图地址
    title = scrapy.Field()  # MM标题
    fileName = scrapy.Field()  # 文件夹名，每一个MM一个文件夹
    path = scrapy.Field()  # 图片存储路径（绝对路径）

class NSGirlItem(scrapy.Item):
    name = 'NSGirlItem'
    siteURL = scrapy.Field()  # MM的url
    girlname = scrapy.Field()  # 姓名
    girlimgurl = scrapy.Field()  # 图片url
    girltable = scrapy.Field()  # table
    girldetail = scrapy.Field()  #描述
    # xzurl =scrapy.Field()  # 写真url
    # xzname = scrapy.Field()
    # xzdesc = scrapy.Field()

class NSAlbumsItem(scrapy.Item):
    name = 'NSAlbumsItem'
    xzurl =scrapy.Field()  # 写真集url
    xzname = scrapy.Field()  # 写真集名称
    xzdesc = scrapy.Field()  # 写真集描述
    xzimgurl = scrapy.Field()  # 写真集图片url
    xztags = scrapy.Field()  # 写真tag
    xzimgs = scrapy.Field() # 写真图片list