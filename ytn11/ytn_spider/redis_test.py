#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: redis_test.py
@time: 2019/1/2 11:20
@desc:
'''
import redis
r=redis.Redis(host='192.168.31.97',port=6379)
r.set(456,123)