#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: wb.py
@time: 2018/12/19 22:21
@desc:
'''
import json

from lxml import etree


def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data
def loading(a):

    for i in range(0,2):
        a['pagebar']=str(i)
        text1 = r.get(url=url2, params=data2, cookies=cookies,headers=header).content.decode()
        content2 = json.loads(text1)
        dict1 = content2['data']
        op = etree.HTML(dict1)
        text2 = op.xpath('//div[@class="WB_text W_f14"]//text()')
        j=''.join(text2)
        print(j)
        # for j in text2:
        #     print(j.strip())
        with open('luhanhan.txt', 'a', encoding='utf-8') as w:
            w.write(j+'\n')

    return 123

import requests as r
url='https://weibo.com/p/1004061537790411/home'
cookies={'SUB':'_2A25xGDBrDeRhGeNJ61MW8inOzz2IHXVSbCajrDV8PUNbmtAKLRihkW9NSB4Mp4hCwtKCch8JSAFXYtD-sVDgKSU6'}
data='''pids: Pl_Official_MyProfileFeed__23
is_search: 0
visible: 0
is_all: 1
is_tag: 0
profile_ftype: 1
page: 1
ajaxpagelet: 1
ajaxpagelet_v6: 1'''
header='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive'''
header2='''X-Requested-With: XMLHttpRequest'''
data = get_data_from_params(data)
header=get_data_from_params(header)
header2=get_data_from_params(header2)
url2='https://weibo.com/p/aj/v6/mblog/mbloglist'
data2='''ajwvr: 6
domain: 100406
is_search: 0
visible: 0
is_all: 1
is_tag: 0
profile_ftype: 1
page: 1
pagebar: 0
pl_name: Pl_Official_MyProfileFeed__23
id: 1004061537790411
script_uri: /p/1004061537790411/home
feed_type: 0
pre_page: 1'''
data2=get_data_from_params(data2)
o=1
while 1:
    data['page']=str(o)
    data2['page']=str(o)
    data2['pre_page']=str(o)
    text=r.get(url=url,params=data,headers=header,cookies=cookies).content
    a=text.decode()[23:-11]
    content=json.loads(a)
    html=content['html']
    op=etree.HTML(html)
    lll=op.xpath('//div[@class="WB_text W_f14"]//text()')
    p=''.join(lll).strip('')
    print(p)
    # for i in lll:
    #
    #     print(i.strip())
    with open('luhanhan.txt', 'a', encoding='utf-8') as w:
        w.write(p+'\n')
    loading(data2)
    #
    #
    o+=1