# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from onespider.db.models import *
import requests
import uuid

global autoid
autoid = (x for x in range(1000))


class OnespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MoviePipeline(object):
    def process_item(self, item, spider):
        # with open('my_meiju2.txt', 'a', encoding='utf8') as target:  # a表书append
        #     target.write(str(item['name']) + '@' +
        #                  str(item['url']) + '@' +
        #                  str(item['status']) + '@' +
        #                  str(item['tags']) + '@' +
        #                  str(item['tvstation']) + '@' +
        #                  str(item['updatetime']) + '\n')
        session = DBSession()
        newmovie = MovieList(mlid=next_id(),
                             name=item['name'],
                             url=item['url'],
                             status=item['status'],
                             tags=item['tags'],
                             tvstation=item['tvstation'],
                             updatetime=item['updatetime']
                             )
        session.add(newmovie)
        session.commit()
        session.close()


# 用requests的get方法获取图片并保存入文件
class XiaohuaPipeline(object):
    def process_item(self, item, spider):
        detailURL = item['detailURL']
        path = item['path']
        fileName = item['fileName']

        image = requests.get(detailURL)
        f = open(path, 'wb')
        f.write(image.content)
        f.close()
        print(u'正在保存图片：', detailURL)
        print(u'图片路径：', path)
        print(u'文件：', fileName)
        return item


# 用requests的get方法获取图片并保存入文件
class NSPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'ns':
            if item.name == 'NSGirlItem':
                print(item)
                print(item.name)
                print(spider)
            if item.name == 'NSPhotoListItem':
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Referer': 'https://www.nvshens.com',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
                print(item)
                print(item.name)
                print(spider)
                # path = r'D:/xh/'+item['xzname']+str(uuid.uuid1())+'.jpg'
                path = r'D:/xh/' + item['xzname'] + str(next(autoid)) + '.jpg'
                print(path)

                # image = requests.get(url=item['xzimgs'], headers=headers)
                # f = open(path, 'wb')
                # f.write(image.content)
                # f.close()

            if item.name == 'NSItem':
                siteURL = item['siteURL']

                print(u'正在保存URL：', siteURL)
                with open('nsurl.txt', 'a') as f:
                    f.write(siteURL + '\n')
                # return item
        elif spider.name == 'ns2':
            if item.name == 'NSTableItem':
                session = DBSession()
                newmovie = t_zngirls_info(id=next_id(),
                                          url=item['item_url'],
                                          photourl=item['item_photourl'],
                                          ms=item['item_ms'],
                                          name=item['item_name'],
                                          bname=item['item_bname'],
                                          blood=item['item_blood'],
                                          height=item['item_height'],
                                          weight=item['item_weight'],
                                          bwh=item['item_bwh'],
                                          birthday=item['item_birthday'],
                                          age=item['item_age'],
                                          xz=item['item_xz'],
                                          birthaddr=item['item_birthaddr'],
                                          job=item['item_job'],
                                          hobby=item['item_hobby']
                                          )
                session.add(newmovie)
                session.commit()
                session.close()


# 用requests的get方法获取图片并保存入文件
class baiduPipeline(object):
    """
    E:\downloaddata
    """

    def process_item(self, item, spider):
        if spider.name == 'baidu':
            if item.__name__ == 'baidutrashitem':
                print(item)
                print(item.__name__)
                print(spider)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Referer': 'https://www.nvshens.com',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
                # path = r'D:/xh/'+item['xzname']+str(uuid.uuid1())+'.jpg'
                path = r'E:/downloaddata/' + str(next(autoid)) + '.jpg'
                print(path)

                image = requests.get(url=item['url'], headers=headers)
                # f = open(path, 'wb')
                # f.write(image.content)
                # f.close()
                with open(path, 'wb') as f:
                    f.write(image.content)
