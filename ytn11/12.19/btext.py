#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: btext.py
@time: 2018/12/18 20:17
@desc: '''
from lxml import etree
import json
import urllib.request as req
from urllib.request import ProxyHandler
url=('http://www.httpbin.org/ip')
handler=ProxyHandler('http://61.176.223.7:58822')
opener=req.build_opener(handler)
html=json.loads(opener.open(url).read().decode())
print(html)