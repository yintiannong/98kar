#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: zhaopin.py
@time: 2019/1/3 9:19
@desc:
'''
import json
import math
import ssc.items as items
def dict_coookies(cookies):
    cookies=cookies[7:-1]
    a=cookies.replace('=',':')
    b=a.replace(';','\n')
    data = {}
    for line in b.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data
import scrapy
class zhaopin_dog(scrapy.Spider):
    cookies='Cookie:Hm_lvt_b025367b7ecea68f5a43655f7540e177=1546478192; user_account_session=a6ddb32e-5945-498c-bcb0-505dbfa0d206AAA4; zhaopingou_select_city=1; hrkeepToken=F6B8FA3F3804915A92B184F7B2673A88; zhaopingou_account=19862705822; zhaopingou_zengsong_cookie_newDay=2019-01-03%3D1; zhaopingou_htm_cookie_register_userName=; zhaopingou_htm_cookie_newDay=2019-01-03; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1546501042; JSESSIONID=A49A61DFCE302C66F8E6F9B5859003B4'
    cookies=dict_coookies(cookies)
    name = 'lsz'
    headers='''User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'''
    formdata='''cityId:-1
addressQu:
strKey:
workYears:
degreesTypes:
positionNature:
companyNature:
companyScaleId:
companySeedtime:
monthType:
monthStr:
sPayMonth:
ePayMonth:
pageSize:0
pageNo:25
clientNo:
userToken:
clientType:2'''
    headers=get_data_from_params(headers)
    formdata=get_data_from_params(formdata)
    def start_requests(self):
        url='http://www.zhaopingou.com/zhaopingou_interface/c_search_find_position?timestamp=1546478211050'
        yield scrapy.FormRequest(url=url,formdata=self.formdata,cookies=self.cookies)
    def parse(self, response):
        dict1=json.loads(response.text)
        list1=dict1['positionReleaseList']
        for i in list1:
            #http://www.zhaopingou.com/jobs/709607.html
            print(i['id'])
            yield scrapy.Request(url='http://www.zhaopingou.com/jobs/'+str(i['id'])+'.html',headers=self.headers,cookies=self.cookies, callback=self.parse2)
        for j in range(1,math.ceil(int(dict1['total'])/25)-1):
            self.formdata['pageSize']=str(j)
            yield scrapy.FormRequest(cookies=self.cookies,url='http://www.zhaopingou.com/zhaopingou_interface/c_search_find_position?timestamp=1546478211050',headers=self.headers,formdata=self.formdata,callback=self.parse3,)
    def parse3(self,response):
        # print(response.text,response.url)
        dict1 = json.loads(response.text)
        list1 = dict1['positionReleaseList']
        for i in list1:
            # http://www.zhaopingou.com/jobs/709607.html
            yield scrapy.Request(url='http://www.zhaopingou.com/jobs/'+str(i['id'])+'.html',headers=self.headers,callback=self.parse2)
    def parse2(self,response):
        # print(response.xpath('//title[1]//text()').extract(),response.url)
        company=''.join(response.xpath('//h2[@id="position_detail_id"]/text()').extract())
        postion=''.join(response.xpath('//p[@class="le public-howa760 position_name"]/text()').extract())
        salary=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/span/text()').extract())
        address=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/ul/li[1]/text()').extract())
        work_type=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/ul/li[2]/text()').extract())
        work=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/ul/li[3]/text()').extract())
        education=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/ul/li[4]/text()').extract())
        exe=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/h2[2]/ul/li[5]/text()').extract())
        data_from=''.join(response.xpath('//*[@id="wrapDiv"]/div[1]/div/div[2]/h2/text()').extract())
        job_des=''.join(response.xpath('//*[@id="wrapDiv"]/div[2]/div/div/div[1]/div[1]/div/div[2]//text()').extract())
        work_address=''.join(response.xpath('//*[@id="wrapDiv"]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/p/text()').extract())
        url=''.join(response.xpath('//*[@id="wrapDiv"]/div[2]/div/div/div[2]/div[1]/div[2]/p[1]/a/span/text()').extract())
        company_type=''.join(response.xpath('//*[@id="wrapDiv"]/div[2]/div/div/div[2]/div[1]/div[2]/p[2]/span/text()').extract())
        company_address=''.join(response.xpath('//*[@id="wrapDiv"]/div[2]/div/div/div[2]/div[1]/div[2]/p[3]/span/text()').extract())
        ite=items.SscItem()
        ite['company']=company
        ite['postion']=postion
        ite['salary']=salary
        ite['address']=address
        ite['work_type']=work_type
        ite['work']=work
        ite['education']=education
        ite['exe']=exe
        ite['data_from']=data_from
        ite['job_des']=job_des
        ite['work_address']=work_address
        ite['url']=url
        ite['company_type']=company_type
        ite['company_address']=company_address
        yield ite


