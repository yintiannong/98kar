# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YtnSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 字典
    sex = scrapy.Field()  # 字典
    age = scrapy.Field()  # 字典
    now_address = scrapy.Field()  # 字典
    exe = scrapy.Field()  # 字典
    education = scrapy.Field()  # 字典
    address=scrapy.Field()
    postion = scrapy.Field()  # 字典
    postion_name = scrapy.Field()  # 字典
    job_intention_city = scrapy.Field()  # 字典
    job_intention_postion = scrapy.Field()  # 字典
    job_intention_salary = scrapy.Field()  # 字典
    job_intention_nature = scrapy.Field()  # 字典
    job_intention_work_time = scrapy.Field()  # 字典
    education2 = scrapy.Field()  # 字典
    education_exe_dec = scrapy.Field()  # 字典
    work_exe_conpany = scrapy.Field()  # 字典
    work_exe_postion = scrapy.Field()
    work_exe_desc = scrapy.Field()# 字典
    work_exe_time = scrapy.Field()  # 字典
    zhengshu = scrapy.Field()  # 字典
    self_ev = scrapy.Field()  # 字典
    id=scrapy.Field()
    peixun=scrapy.Field()
    education_exe_school_name=scrapy.Field()
    education_exe_school_zy=scrapy.Field()
    education_exe_school_time=scrapy.Field()
    education_exe_school_desc=scrapy.Field()
    p_out=scrapy.Field()
    marryage=scrapy.Field()








