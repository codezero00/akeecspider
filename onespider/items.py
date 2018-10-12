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

class BaiduTrashItem(scrapy.Item):
    __name__ = 'baidutrashitem'

    url = scrapy.Field()

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

class NSItem(scrapy.Item):
    name = 'NSItem'
    siteURL = scrapy.Field()  # sitemap url

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
    # xzimgs = scrapy.Field() # 写真图片list

class NSPhotoListItem(scrapy.Item):
    name = 'NSPhotoListItem'
    xzname =scrapy.Field()  # 写真集名称
    xzimgs = scrapy.Field()  # 写真图片list


class NSTableItem(scrapy.Item):
    name = 'NSTableItem'
    item_url = scrapy.Field()
    item_photourl = scrapy.Field()
    item_ms = scrapy.Field()

    item_name = scrapy.Field()
    item_bname = scrapy.Field()
    item_blood = scrapy.Field()
    item_height = scrapy.Field()
    item_weight = scrapy.Field()
    item_bwh = scrapy.Field()
    item_birthday = scrapy.Field()
    item_age = scrapy.Field()
    item_xz = scrapy.Field()
    item_birthaddr = scrapy.Field()
    item_job = scrapy.Field()
    item_hobby = scrapy.Field()