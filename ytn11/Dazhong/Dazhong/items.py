# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DazhongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    business=scrapy.Field()
    per_money=scrapy.Field()
    taste=scrapy.Field()
    env=scrapy.Field()
    server=scrapy.Field()
    address=scrapy.Field()
    phone=scrapy.Field()
    open_time=scrapy.Field()
    introduce=scrapy.Field()


