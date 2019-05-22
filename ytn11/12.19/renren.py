#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: renren.py
@time: 2018/12/19 18:45
@desc:
'''
import random
import requests as r
import chaojiying as cj
from lxml import etree
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		  # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="baizhi_db",          # 要使用的库名
    charset="utf8")      # 连接中使用的字符集

cursor = conn.cursor()

cookies={
    't':'f6b69528b436b5394d41b44c98c27ad59'
}

url = 'http://www.renren.com/259598622/profile'
session = r.Session()
session.cookies.update(cookies)
i='259598622'
while 1:
    try:
        title = etree.HTML(session.get(url).text).xpath('//title/text()')[0]
        print(title)
        if '验证码' in title:
            print('sss')
            getcode_url = 'http://icode.renren.com/getcode.do?t=ninki&rnd=1545312152636'
            print(456)
            code = cj.getcode(session.get(getcode_url).content)  # 获取验证码二进制流，并且识别验证码
            check_code_url = 'http://www.renren.com/validateuser.do?'
            print(789)
            data = {
                'id': i,
                'icode': code,
                'submit': '继续浏览',
                'requestToken': '303803715',
                '_rtk': 'dddcab9d'
            }
            # 验证验证码
            a=session.post(check_code_url, data)
    except:
        continue
    else:
        text = session.get(url=url).text
        html = etree.HTML(text)
        nameid = html.xpath('//a/@namecard')
        for i in nameid:
            # sql='insert into userid (userid) values('+i+')'
            # cursor.execute(sql)
            # conn.commit()
            print(i)
        print(nameid)
        if not nameid:
            print(656)
            url = 'http://www.renren.com/1/profile'
        else:
            num = random.randint(0, len(nameid) - 1)
            i = nameid[num]
            print(i)
            url = 'http://www.renren.com/' + i + '/profile'


