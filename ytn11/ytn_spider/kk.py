#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: kk.py
@time: 2019/1/2 8:59
@desc:
'''
def dict_coookies(cookies):
    cookies=cookies[7:-1]
    a=cookies.replace('=',':')
    b=a.replace(';','\n')
    print(b)
    data = {}
    for line in b.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data



