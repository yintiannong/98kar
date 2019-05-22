# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    company_id = scrapy.Field()
    postion_id = scrapy.Field()
    company_type = scrapy.Field()
    company_size = scrapy.Field()
    url = scrapy.Field()
    postion = scrapy.Field()
    salary = scrapy.Field()
    education=scrapy.Field()
    address = scrapy.Field()
    exe = scrapy.Field()
    job_type = scrapy.Field()
    update_time = scrapy.Field()
    data_from = scrapy.Field()
    desc_job = scrapy.Field()
    salary2 = scrapy.Field()
    conpany_address = scrapy.Field()
    phone_num = scrapy.Field()
    hr_name = scrapy.Field()
