# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import uuid
class YtnSpiderPipeline(object):

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
        try:
            sql = 'insert user_base(country,id,name,age,sex,education,birth,political_outlook,now_address,address)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, ['中国',item['id'], item['name'], item['age'],item['sex'],item['education'],item['age'],item['p_out'],item['now_address'],item['address']])

            for i in range(len(item['education_exe_school_name'])):
                start1=item['education_exe_school_time'][i].split('-')[0]
                stop1=item['education_exe_school_time'][i].split('-')[1]
                profession=item['education_exe_school_zy'][i].split('·')[1]
                education_type=item['education_exe_school_zy'][i].split('·')[0]
                sql2 = 'insert education_base(id,user_id,school,admission_time,graduate_time,professional,education_type,school_desc) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(sql2,[uuid.uuid4(),item['id'],item['education_exe_school_name'][i],start1,stop1,profession,education_type,item['education_exe_school_desc'][i]])
            for j in range(len(item['work_exe_conpany'])):
                in_time=item['work_exe_time'][j].split('-')[0]
                out_time=item['work_exe_time'][j].split('-')[1]
                sql3='insert job_exe(id,user_id,company_name,pos_name,in_time,out_time,job_introduce)values(%s,%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(sql3,[uuid.uuid4(),item['id'],item['work_exe_conpany'][j],item['work_exe_postion'][j],in_time,out_time,item['work_exe_desc'][j]])
            sql4='insert job_wanted(id,user_id,want_city,want_salary,postion_name,postion_time) values (%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql4,[uuid.uuid4(),item['id'],item['job_intention_city'],item['job_intention_salary'],item['job_intention_nature'],item['job_intention_work_time']])
            sql5='insert vip_info(id,user_id,zhengshu,introduce_myself,train_exe) values(%s,%s,%s,%s,%s)'
            self.cursor.execute(sql5,[uuid.uuid4(),item['id'],item['zhengshu'],item['self_ev'],item['peixun']])
        except:
            pass
        self.conn.commit()
    def process_item(self, item, spider):
        self.save(item)
        return item


