#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: wh.py
@time: 2019/1/3 16:55
@desc:
'''
import json
import wh.items as items
import scrapy
class wh(scrapy.Spider):
    name = 'wh'
    items=items.WhItem()
    start_urls=['http://zhejiang.job910.com/']
    def parse(self, response):
        hrefs=response.xpath('//div[@class="content"]/ul[@class="area-list"]/li/a/@href').extract()
        for i in hrefs:
            url='http:'+i+'/'
            yield scrapy.Request(url=url,callback=self.parse2)
    def parse2(self,response):
        hrefs=response.xpath('//div[@class="area-entry area-entry-province pull-left"]/div/a/@href').extract()
        for i in hrefs:
            yield scrapy.Request(url='http:'+i,callback=self.parse3)
    def parse3(self,response):
        href=response.xpath('//a[@class="show-more"]/@href').extract()[0]
        print(href)
        yield scrapy.Request(url=href,callback=self.parse4)
    def parse4(self,response):
        hrefs=response.xpath('//div[@class="position title"]/a/@href').extract()
        for i in hrefs:
            yield scrapy.Request(url='http://www.job910.com'+i,callback=self.parse5)
        href=''.join(response.xpath('//div[@class="inner"]/a[last()]/@href').extract())
        try:
            yield scrapy.Request(url=href,callback=self.parse4)
        except:
            pass
    def parse5(self,response):
        pass
        company=''.join(response.xpath('//div[@class="company"]/a/text()').extract())
        postion_id=response.url[32:-5]
        company_id=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[1]/div/a/@href').extract()).strip()[13:-5]
        company_type=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[2]/div/p[1]/text()').extract()).strip()
        company_size=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[2]/div/p[3]/text()').extract()).strip()
        url=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[2]/div/p[4]/a/@href').extract()).strip()
        postion=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[1]/span/text()').extract()).strip()
        salary=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[1]/text()').extract())
        education=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[4]/text()').extract()).strip()
        address=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[2]/text()').extract())
        exe=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[3]/text()').extract()).strip()
        job_type=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[5]/text()').extract()).strip()
        update_time=''.join(response.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[2]/text()').extract())
        data_from='来源于万行教师网'
        desc_job=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[1]/text()').extract()).strip()
        salary2=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[2]//text()').extract()).strip()
        conpany_address=''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[3]/div[2]/text()').extract()).strip()
        hr_name =''.join(response.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[3]/div[1]/text()').extract()).strip()
        self.items['company']=company
        self.items['company_id']=company_id
        self.items['postion_id']=postion_id
        self.items['company_type']=company_type
        self.items['company_size']=company_size
        self.items['url']=url
        self.items['postion']=postion
        self.items['salary']=salary
        self.items['education']=education
        self.items['address']=address
        self.items['exe']=exe
        self.items['job_type']=job_type
        self.items['update_time']=update_time
        self.items['data_from']=data_from
        self.items['desc_job']=desc_job
        self.items['salary2']=salary2
        self.items['conpany_address']=conpany_address
        self.items['hr_name']=hr_name
        yield self.items
        jobid=response.url
        url='http://www.job910.com/api/job/index.ashx?jobid='+jobid[32:-5]+'&d_type=phone'
        yield scrapy.Request(url=url,callback=self.parse6)
    def parse6(self,response):
        phone_num=json.loads(response.text)['Data']['Phone']
        self.items['phone_num']=phone_num
        yield self.items