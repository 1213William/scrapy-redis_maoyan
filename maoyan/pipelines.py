# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MaoyanPipeline(object):
    container = []
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            db='spider',
            autocommit=True
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        # print(item['link'])
        self.container.append([item['title'], item['link']])
        if len(self.container) == 1:
            self.insert_sql(self.container)
            self.container.clear()
        return item

    def insert_sql(self, data):
        try:
            sql = 'insert into maoyan (title, link) values (%s, %s);'
            self.cursor.execute(sql, data[0])
        except:
            print('插入数据发生了错误...')
            self.conn.rollback()


