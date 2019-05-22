#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 百度图片.py
@time: 2018/12/26 18:44
@desc:
'''
import json
import tp.items as i
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class Pict(scrapy.Spider):
    items=i.TpItem()
    name = 'tp'
    start_urls=['http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E6%96%97%E5%9B%BE&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=3c&1545818030329=']
    def parse(self, response):
        dict=json.loads(response.text)
        list1=[]
        for url in dict['data']:
            try:
                list1.append(url['thumbURL'])
            except:
                continue

        self.items['image_urls']=list1
        yield self.items
