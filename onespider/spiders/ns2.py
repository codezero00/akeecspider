# -*- coding: utf-8 -*-
import scrapy
from onespider.items import NSGirlItem, NSAlbumsItem, NSPhotoListItem, NSItem, NSTableItem
from scrapy.http import Request
import re


class MeijuSpider(scrapy.Spider):
    name = 'ns2'
    allowed_domains = ['nvshens.com']
    start_urls = []


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
        photourl = re.compile(r"<a target='_blank' class='imglink' href='(.*?)'>", re.S)
        ms = re.compile(r"<div class=\"infocontent\"><p>(.*?)</p>", re.S)
        name = re.compile(r"<div class=\"div_h1\"><h1 style=\"font-size: 15px\">(.*?)</h1>", re.S)
        bname = re.compile(r"<td class='info_td'>别 名：</td><td class='info_td_r'>(.*?)</td>", re.S)
        blood = re.compile(r"<td class='info_td'>血 型：</td><td>(.*?)</td>", re.S)
        height = re.compile(r"<td class='info_td'>身 高：</td><td>(.*?)</td>", re.S)
        weight = re.compile(r"<td class='info_td'>体 重：</td><td>(.*?)</td>", re.S)
        bwh = re.compile(r"<td class='info_td'>三 围：</td><td>(.*?)</td>", re.S)
        birthday = re.compile(r"<td class='info_td'>生 日：</td><td>(.*?)</td>", re.S)
        age = re.compile(r"<td class='info_td'>年 龄：</td><td>.*? \((.*?)\)</td>", re.S)
        xz = re.compile(r"<td class='info_td'>星 座：</td><td>(.*?)</td>", re.S)
        birthaddr = re.compile(r"<td class='info_td'>出 生：</td><td>(.*?)</td>", re.S)
        job = re.compile(r"<td class='info_td'>职 业：</td><td>(.*?)</td>", re.S)
        hobby = re.compile(r"<td class='info_td'>兴 趣：</td><td class='info_td_r'>(.*?)</td>", re.S)
        """
        """
        item_photourl = re.findall(photourl, response.text)
        item_ms = re.findall(ms, response.text)

        item_name = re.findall(name, response.text)
        item_bname = re.findall(bname, response.text)
        item_blood = re.findall(blood, response.text)
        item_height = re.findall(height, response.text)
        item_weight = re.findall(weight, response.text)
        item_bwh = re.findall(bwh, response.text)
        item_birthday = re.findall(birthday, response.text)
        item_age = re.findall(age, response.text)
        item_xz = re.findall(xz, response.text)
        item_birthaddr = re.findall(birthaddr, response.text)
        item_job = re.findall(job, response.text)
        item_hobby = re.findall(hobby, response.text)
        item = NSTableItem()

        item['item_url'] = response.url
        item['item_photourl'] = dict(enumerate(item_photourl)).get(0)
        item['item_ms'] = dict(enumerate(item_ms)).get(0)

        item['item_name'] = dict(enumerate(item_name)).get(0)
        item['item_bname'] = dict(enumerate(item_bname)).get(0)
        item['item_blood'] = dict(enumerate(item_blood)).get(0)
        item['item_height'] = dict(enumerate(item_height)).get(0)
        item['item_weight'] = dict(enumerate(item_weight)).get(0)
        item['item_bwh'] = dict(enumerate(item_bwh)).get(0)
        item['item_birthday'] = dict(enumerate(item_birthday)).get(0)
        item['item_age'] = dict(enumerate(item_age)).get(0)
        item['item_xz'] = dict(enumerate(item_xz)).get(0)
        item['item_birthaddr'] = dict(enumerate(item_birthaddr)).get(0)
        item['item_job'] = dict(enumerate(item_job)).get(0)
        item['item_hobby'] = dict(enumerate(item_hobby)).get(0)
        yield item