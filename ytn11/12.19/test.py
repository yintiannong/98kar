#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: test.py
@time: 2018/12/19 20:22
@desc:
'''
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		  # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="baizhi_db",          # 要使用的库名
    charset="utf8")      # 连接中使用的字符集
cursor = conn.cursor()
sql="insert into userid(userid) values (456)"
print(123)
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()