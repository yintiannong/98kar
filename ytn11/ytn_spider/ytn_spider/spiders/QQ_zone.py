#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: QQ_zone.py
@time: 2018/12/24 19:08
@desc:
'''
#cookie={'skey':'@1aFT2FfMw'}
#蛇市厂qq：1061022597
import json
import math
import scrapy
class ZoneSpider(scrapy.Spider):
    cookie = {'p_skey': 'bKMZzykbN9LSSh7MwcpdzYs9KOXsGseoxiAu9Y5uYgo_','uin': 'o1375020135'}
    name = 'qq'
    pos=20
    qq_num='1375020135'
    def start_requests(self):
        url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin='+self.qq_num+'&ftype=0&sort=0&pos=0&num=20&replynum=100&g_tk=414890102&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken=b21383d3db28f15137849017cb216a4fe69dca3b645bd682382ff27ead1b7a53630eb03eff3641a3&g_tk=414890102'
        re = scrapy.Request(url=url, cookies=self.cookie)
        yield re

    def parse(self, response):
        text = response.text[17:-2]
        dict1 = json.loads(text)
        count=dict1['usrinfo']['msgnum']
        for i in dict1['msglist']:
            print(i['content'])
        for j in range(math.ceil(int(count)/20)):
            url2 = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin='+self.qq_num+'&ftype=0&sort=0&pos=' + str(self.pos) + '&num=20&replynum=100&g_tk=414890102&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken=b21383d3db28f15137849017cb216a4fe69dca3b645bd682382ff27ead1b7a53630eb03eff3641a3&g_tk=414890102'
            self.pos+=20
            re2 = scrapy.Request(url=url2, cookies=self.cookie, callback=self.parse1)
            yield re2

    def parse1(self, response):
        text = response.text[17:-2]
        dict1 = json.loads(text)
        for i in dict1['msglist']:
            print(i['content'])

