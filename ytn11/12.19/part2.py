#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: part2.py
@time: 2018/12/18 15:39
@desc:
'''
from lxml import etree
import urllib.request as req
index=0
while 1:
    check_url='http://httpbin.org/ip'
    url='https://www.xicidaili.com/nn'
    req_obj=req.Request(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    })
    html=etree.HTML(req.urlopen(req_obj).read())
    result=html.xpath('//tr/td[2]/text()')
    print(html)
