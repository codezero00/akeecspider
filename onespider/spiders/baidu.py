"""
百度爬取垃圾桶
"""

import scrapy
from onespider.items import NSGirlItem, NSAlbumsItem, NSPhotoListItem, BaiduTrashItem
from scrapy.http import Request
import re

class baiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']

    def start_requests(self):
        for n in range(10):
            n = n*100
            start_url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%9E%83%E5%9C%BE%E6%A1%B6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%9E%83%E5%9C%BE%E6%A1%B6&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={n}&rn=100&gsm=258&1533722301876='
            yield Request(start_url, callback=self.parse1)

    def parse1(self, response):
        print(response)
        # elements = response.xpath('//img')
        # print(elements)
        pattern = re.compile(r'"ObjURL":"(.*?)",', re.S)
        imglist = re.findall(pattern, response.text)
        print(imglist)
        item = BaiduTrashItem()
        for i in imglist:
            item['url'] = i.replace('\\','')
            yield item

