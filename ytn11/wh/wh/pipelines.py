# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import uuid
class WhPipeline(object):
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
        sql = 'insert into conpany_base(id,company_name,company_type,company_size,url,address,hr_name,hr_phone,data_from)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        sql2='insert into t_postion(id,postion_name,salary,address,exe,education,job_type,introduce_job,salary2,postion_type,company_id)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, [item['company_id'],item['company'], item['company_type'],item['company_size'], item['url'], item['address'],item['hr_name'],item['phone_num'],item['data_from']])
        except:
            pass
        try:
            self.cursor.execute(sql2,[item['postion_id'],item['postion'],item['salary'],item['address'],item['exe'],item['education'],item['job_type'],item['desc_job'],item['salary2'],'老师',item['company_id']])
        except:
            pass
        self.conn.commit()

    def process_item(self, item, spider):
        self.save(item)
        return item