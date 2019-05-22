#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: sports.py
@time: 2019/1/25 14:52
@desc:
'''
import json

import scrapy
import time

from lxml import etree


def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

class Sport_spiders(scrapy.Spider):
    name = 'ty'
    headers='''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
    headers=get_data_from_params(headers)
    def start_requests(self):
        url='https://www.huodongjia.com/business/page-1/'
        yield scrapy.Request(url=url,headers=self.headers)
    def parse(self,response):
        url=response.xpath('//h3/a/@href').extract()
        for i in url:
            url='https://www.huodongjia.com'+i
            yield scrapy.Request(url,headers=self.headers,callback=self.parse1)
        next_page=response.xpath('//a[text()="下一页"]/@href').extract()[0]
        if next_page:
            with open('duandian.log','w') as a:
                a.write(next_page)
        if next_page:
            next_page_url='https://www.huodongjia.com'+next_page
            yield scrapy.Request(next_page_url,headers=self.headers,callback=self.parse)
    def parse1(self,response):
        name=''.join(response.xpath('//h1[@class="event_name"]/a/text()').extract()).strip()
        times=''.join(response.xpath('//h1[@class="event_name"]/following-sibling::p[1]//text()').extract()).strip()[5:]
        address=response.xpath('//h1[@class="event_name"]/following-sibling::p[2]//text()').extract()
        address1=''
        for i in address[1:]:
            address1+=i.strip()
        size=''.join(response.xpath('//h1[@class="event_name"]/following-sibling::p[3]//text()').extract()).strip()[5:]
        owner=''.join(response.xpath('//h1[@class="event_name"]/following-sibling::p[4]//text()').extract()[1:]).strip()
        line=name+'     '+times+'      '+address1+'     '+size+'        '+owner
        # with open('informatios.doc','a') as w:
        #     w.write(line+'\n')
        # print(name,times,address,size,owner)
        dict1={'name':name,'time':times,'address':address1,'owner':owner,'size':size}
        str1=str(dict1)
        print(str1)
        # with open('info.txt','a') as w:
        #     w.write(str1+'\n')
        # print(name,times,address,size,owner)



