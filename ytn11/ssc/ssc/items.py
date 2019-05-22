# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SscItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    postion = scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    work_type = scrapy.Field()
    work = scrapy.Field()
    education= scrapy.Field()
    exe= scrapy.Field()
    data_from= scrapy.Field()
    job_des= scrapy.Field()
    work_address= scrapy.Field()
    url= scrapy.Field()
    company_type= scrapy.Field()
    company_address= scrapy.Field()
