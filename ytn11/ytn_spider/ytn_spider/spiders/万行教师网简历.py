#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 万行教师网简历.py
@time: 2018/12/25 19:54
@desc:
'''
import scrapy


import ytn_spider.items as i
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisSpider


class Teacherspider(scrapy.Spider):
    name = 'js'
    start_urls=['http://www.job910.com/Company/resume/SearchList.aspx?NowAreaCode=&NowWork=&MinWorkYears=&MaxWorkYears=&UpdateDateScope=&Keyword=&HopeWorkArea=&HopeWork=&MinAge=&MaxAge=&MinDegree=-1&MaxDegree=-1&Marriage=&workMethod=&major=&TechnialPost=&entrytime=&resumeid=&IsHead=&Gender=&type=0&txtsearchName=']
    def parse(self, response):
        text=response.xpath('//td[@class="td_l"]/a[1]/@href').extract()
        for i in text:
            url2='http://www.job910.com/company/resumeview.aspx?userId='+i[32:-21]
            re=scrapy.Request(url=url2,callback=self.parse2)
            yield re
        url3 = response.xpath('//div[@class="pagination"]/div[1]/a[last()]/@href')[0].extract()
        re2 = scrapy.Request(url=url3)
        yield re2
    # rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="pagination"]/div')), follow=True),)  # 多个的
    def parse2(self,response):
        name=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[1]/span[1]/text()').extract()).strip()
        sex=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/text()').extract()).strip()
        age=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/span[3]/text()').extract()).strip()
        now_address=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/span[5]/text()').extract()).strip()
        exe=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/text()').extract()).strip()
        education=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[3]/text()').extract()).strip()
        postion=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[5]/text()').extract()).strip()
        postion_name=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/span[3]/text()').extract()).strip()
        job_intention_city=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/span[2]/text()').extract()).strip()
        job_intention_postion=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/span[2]/text()').extract()).strip()
        job_intention_salary=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[3]/label[1]/text()').extract()).strip()
        job_intention_nature=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[3]/label[2]/text()').extract()).strip()
        job_intention_work_time=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[3]/label[3]/text()').extract()).strip()
        education_exe_school_name=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[@class="unit-item"]/div[@class="unit-item-title m-tb-10"]/span[@class="gray-dark bold"]/text()').extract()
        education_exe_school_zy=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[1]/text()').extract()
        education_exe_school_time =response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[2]/text()').extract()
        education_exe_school_desc =response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[3]/text()').extract()
        address=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/span[9]/text()').extract()).strip()
        work_exe_conpany=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[4]/div[2]/div[@class="unit-item"]/div[@class="unit-item-title m-tb-10"]/span/text()').extract()
        work_exe_postion=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[4]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[1]/text()').extract()
        work_exe_time=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[4]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[2]/text()').extract()
        work_exe_desc=response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[4]/div[2]/div[@class="unit-item"]/div[@class="unit-item-content gray"]/div[3]/text()').extract()
        zhengshu=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div[2]//text()').extract()).strip()
        self_ev=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[6]/div[2]//text()').extract()).strip()
        id=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/text()').extract()).strip()[4:-1]
        p_out=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/span[1]/text()').extract()).strip()
        marryage=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/span[7]/text()').extract()).strip()
        peixun=''.join(response.xpath('//*[@id="container"]/div/div/div/div[1]/div[2]/div[6]/div[2]/div//text()').extract()).strip()

        item=i.YtnSpiderItem()
        item['id']=id
        item['name']=name
        item['sex']=sex
        item['age']=age
        item['now_address']=now_address
        item['exe']=exe
        item['education']=education
        item['postion']=postion
        item['postion_name']=postion_name
        item['job_intention_city']=job_intention_city
        item['job_intention_postion']=job_intention_postion
        item['job_intention_salary']=job_intention_salary
        item['job_intention_nature']=job_intention_nature
        item['job_intention_work_time']=job_intention_work_time
        item['education_exe_school_zy']=education_exe_school_zy
        item['education_exe_school_name']=education_exe_school_name
        item['education_exe_school_time']=education_exe_school_time
        item['education_exe_school_desc']=education_exe_school_desc
        item['work_exe_conpany']=work_exe_conpany
        item['work_exe_postion']=work_exe_postion
        item['work_exe_time']=work_exe_time
        item['work_exe_desc']=work_exe_desc
        item['zhengshu']=zhengshu
        item['self_ev']=self_ev
        item['p_out']=p_out
        item['marryage']=marryage
        item['address']=address
        item['peixun']=peixun
        yield item

