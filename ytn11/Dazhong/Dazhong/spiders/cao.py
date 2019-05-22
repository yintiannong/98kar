#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: cao.py
@time: 2018/12/28 20:45
@desc:
'''
import scrapy
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

class Ru(scrapy.Spider):
    name = 'oo'
    def start_requests(self):
        headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Cache-Control: max-age=0
        Connection: keep-alive
        Cookie: navCtgScroll=100; navCtgScroll=100; _hc.v=09d606a7-d8b8-da5a-0811-89eb8026f43f.1545988489; _lxsdk_cuid=167f4286401c8-0128e72c26344-5701732-1fa400-167f4286401c8; _lxsdk=167f4286401c8-0128e72c26344-5701732-1fa400-167f4286401c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1545993996; wed_user_path=163|0; cy=2; cityid=2; cye=beijing; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1545996173; cy=2; cye=beijing; _lxsdk_s=167f4286402-bcd-ece-8a6%7C%7C3599
        Host: www.dianping.com
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
        headers = get_data_from_params(headers)
        url='http://www.dianping.com/anxian/ch10'
        yield  scrapy.Request(url=url,headers=headers)
    def parse(self, response):
        print(response.text)