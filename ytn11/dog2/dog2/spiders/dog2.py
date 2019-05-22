#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: dog2.py
@time: 2019/1/3 22:36
@desc:
'''
import scrapy
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data
class Dog2(scrapy.Spider):
    name = 'dog2'
    formdata='''pageSize: 0
pageNo: 25
keyStr: 
companyName: 
schoolName: 
keyStrPostion: 
postionStr: 
startDegrees: -1
endDegress: -1
startAge: 0
endAge: 0
gender: -1
region: 
timeType: -1
startWorkYear: -1
endWorkYear: -1
beginTime: 
endTime: 
isMember: -1
hopeAdressStr: 
cityId: -1
updateTime: 
tradeId: 
startDegreesName: 
endDegreesName: 
tradeNameStr: 
regionName: 
isC: 0
is211_985_school: 0
clientNo: 
userToken: 84DA14F87C3A99FECE624DA6F466C6B0
clientType: 2'''
    formdata=get_data_from_params(formdata)
    def start_requests(self):
        url='http://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new?timestamp=1546526342455'
        yield scrapy.FormRequest(url=url,formdata=self.formdata)
    def parse(self, response):
        print(response.text)
