#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: test.py
@time: 2019/1/3 14:59
@desc:
'''
import requests
url='http://www.zhaopingou.com/jobs/800271.html'
print(requests.get(url).text)