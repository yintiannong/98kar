#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: no_trust.py
@time: 2018/12/19 11:19
@desc:
'''

import requests as r
import json
from lxml import etree


url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'


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
format: json'''
data=get_data_from_params(data)
pn=0
while 1:
    data['pn']=str(pn)
    textz=r.get(url,params=data,proxies={'http': '219.238.186.188:8118'}).text
    a=json.loads(textz)
    # print(a['data'][0]['result'])

    for i in a['data'][0]['result']:
        name=i['iname']
        sexy=i['sexy']
        idcard=i['cardNum']

        print(name,sexy,idcard)
    pn+=10
