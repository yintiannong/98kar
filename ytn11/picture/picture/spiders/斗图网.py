#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 斗图网.py
@time: 2018/12/27 19:29
@desc:
'''
import scrapy

import picture.items as i
class Picture(scrapy.Spider):
    name = 'dt'
    page=1
    items=i.PictureItem()
    start_urls=['http://www.doutula.com/article/list/?page=1']
    def parse(self, response):
        urls=response.xpath('//div[@class="col-xs-6 col-sm-3"]/img/@data-original').extract()
        print(urls)
        fold_name='第'+str(self.page)+'页'
        self.items['image_urls']=urls
        self.items['fold_name']=fold_name
        yield self.items
