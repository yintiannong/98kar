#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: baidu.py
@time: 2018/12/19 13:59
@desc:
'''
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data
data='''resource_id: 6899
query: '失信人'
pn: 10
rn: 10
ie: utf-8
oe: utf-8
format: json
'''
print(get_data_from_params(data))