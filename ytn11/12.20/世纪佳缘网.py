#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 世纪佳缘网.py
@time: 2018/12/23 10:56
@desc:
'''
import json

from lxml import etree


def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

import requests as r
url='http://search.jiayuan.com/v2/search_v2.php'
cookies={'COMMON_HASH':'f255a389f662408cbdda163e79a37369'}
data='''sex: f
key: 
stc: 
sn: default
sv: 1
p: 1
f: select
listStyle: bigPhoto
pri_uid: 187603231
jsversion: v5'''

data=get_data_from_params(data)
page=1
sv=1
while 1:
    print(page)
    data['p']=str(page)
    text=r.post(url=url,data=data,cookies=cookies).content[11:-13].decode()
    contents=json.loads(text)["userInfo"]

    for i in contents[1:]:
        id=i['realUid']
        url2='http://www.jiayuan.com/'+str(id)
        headers='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Host: www.jiayuan.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
        headers=get_data_from_params(headers)
        a=r.get(url=url2,headers=headers,cookies=cookies).content.decode()
        html=etree.HTML(a)
        list1 = html.xpath('//h4//text()')

        if list1:
            username=list1[0]
            userid=list1[1][2:]
            try:
                introduce_myself=''.join(html.xpath('//h6[@class="member_name"]//text()'))
            except:
                continue
            try:
                education=html.xpath('//div[@class="fl pr"]/em/text()')[0]
            except:
                continue
            try:
                high = html.xpath('//div[@class="fl pr"]/em/text()')[1]
            except:
                continue
            try:
                house = html.xpath('//div[@class="fl pr"]/em/text()')[0]
                if not house:
                    house='空'
            except:
                continue
            try:
                weight = html.xpath('//div[@class="fl pr"]/em/text()')[2]
            except:
                continue
            # try:
            #     fav=html.xpath('//h6[@class="yh"]//texy()')
            # except:
            #     continue
            print(username,userid,introduce_myself,education,high,weight)
    page+=1