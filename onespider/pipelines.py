# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from onespider.db.models import *


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