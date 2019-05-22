#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 万行教师网.py
@time: 2018/12/23 16:22
@desc:
'''
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		  # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="mysql_db",          # 要使用的库名
    charset="utf8")      # 连接中使用的字符集

cursor = conn.cursor()
import requests as r
from lxml import etree
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

url='http://www.job910.com/search.aspx'
data='''funtype: 
salary: 
maxSalary: 
minSalary: 
workMethod: 
sortField: 1
education: 
experience: 
uptime: 0
area: 370100,370300
keyword: 
sort: 0
pageSize: 20
pageIndex: 1'''
data=get_data_from_params(data)
page=1
while 1:
    data['pageIndex']=str(page)
    text=r.get(url=url,params=data).content.decode()
    html=etree.HTML(text)
    content=html.xpath('//div[@class="position title"]/a/@rel')
    headers='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Host: www.job910.com
    Referer: http://www.job910.com/search.aspx?funtype=&sortField=1&sort=1&pageSize=20&pageIndex=2&salary=&maxSalary=&minSalary=&workMethod=&education=&experience=&uptime=0&keyword=%E5%B1%B1%E4%B8%9C&area=
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
    headers=get_data_from_params(headers)
    for i in content:

        url2='http://www.job910.com/jobs_view_'+str(i)+'.html'
        text=r.get(url=url2,headers=headers).content.decode()
        html=etree.HTML(text)
        school=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[1]/div/a/text()')[0]
        postion=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[1]/span/text()')[0].strip()
        salary=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[1]/text()')[0]
        address=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[2]/text()')[0]
        exper=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[3]/text()')[0].strip()
        education=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[4]/text()')[0].strip()
        xizhi=html.xpath('//*[@id="jobs-page"]/div[1]/div/div[1]/div[2]/p[1]/span[5]/text()')[0].strip()
        in_postion=''.join(html.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[1]//text()')).strip()[34:]
        fldy=''.join(html.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[2]//text()')).strip()[34:]
        address1=html.xpath('//*[@id="jobs-page"]/div[3]/div/div[1]/div[1]/div[3]/div[2]/text()')[0].strip()
        sql='insert into t_wh(school,postion,salary,address,exper,education,xizhi,in_postion,fldy,address1) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,[school,postion,salary,address,exper,education,xizhi,in_postion,fldy,address1])
        conn.commit()
    page+=1