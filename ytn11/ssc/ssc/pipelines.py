# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class SscPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            db='mysql_db',
            user='root',
            password='123456',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
    def save(self, item):
        sql = 'insert into conpany_base(company_name,company_type,url,address)VALUES (%s,%s,%s,%s)'
        self.cursor.execute(sql,[item['company'], item['company_type'], item['url'],item['address']])
        self.conn.commit()
    def process_item(self, item, spider):
        self.save(item)
        return item
