#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: pa.py
@time: 2018/12/17 16:11
@desc:
'''
import re
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		  # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="mysql_db",          # 要使用的库名
    charset="utf8")      # 连接中使用的字符集
cursor = conn.cursor()

from urllib.parse import quote
import string
import urllib.request as req
import json
from lxml import etree
# 确定需求
citys=['530', '538', '763', '765']  #四个城市的代号
kws=['python+web','爬虫','python 大数据','AI'] # 搜索词
# 标示爬虫采集的进度
city_index=0
kw_index=0
start=0
while 1:
    url='https://fe-api.zhaopin.com/c/i/sou?start='+str(start)+'&pageSize=90&cityId='+citys[city_index]+'&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw='+kws[kw_index]+'&kt=3&_v=0.49512205&x-zp-page-request-id=c7e19a85faaa4eeaa56b759ef311fea2-1545047419388-203372'
    url=quote(url,safe=string.printable)
    req2 = req.urlopen(url=url).read().decode('utf-8')
    datas=json.loads(req2)
    for i in datas['data']['results']:
        try:
            req1=req.urlopen(i['positionURL']).read().decode('utf-8')
            html=etree.HTML(req1)
            postion=html.xpath('//h1/text()')[0]
        except:
            continue
        try:
           company=html.xpath('//div[@class="company l"]/a/text()')[0]
        except:
            continue
        try:
            salary=html.xpath('//div[@class="l info-money"]/strong/text()')[0]
        except:
            continue
        try:
            duty=''.join(html.xpath('//div[@class="pos-ul"]/p/text()'))
            if not  duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/p/span/text()'))
            if not duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/span/text()')[0])
            if not duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/div/span/text()')[0])
            if not duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/div/text()')[0])
            if not duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/text()')[0])
            if not duty:
                duty = ''.join(html.xpath('//div[@class="pos-ul"]/pre/text()')[0])

        except:
            continue
        try:
            education=html.xpath('//div[@class="info-three l"]/span[3]/text()')[0]
        except:
            continue
        try:
            zp_num=html.xpath('//div[@class="info-three l"]/span[4]/text()')[0]
        except:
            continue
        try:
            yw=html.xpath('//span[@class="iconfont icon-promulgator-person"]/following-sibling::strong/a/text()')[0]
        except:
            continue
        try:
            gs_num=html.xpath('//span[@class="iconfont icon-promulgator-link"]/following-sibling::strong/text()')[0]
        except:
            continue
        try:
            gs_xz=html.xpath('//span[@class="iconfont icon-promulgator-type"]/following-sibling::strong/text()')[0]
        except:
            continue
        try:
            gs_url=html.xpath('//span[@class="iconfont icon-promulgator-url"]/following-sibling::strong/a/text()')[0]
        except:
            continue
        try:
            gs_introduce=''.join(html.xpath('//div[@class="intro-content"]/p/span/text()'))
        except:
            continue
        try:
            welfare = re.findall(r"JobWelfareTab = '(.+?)';", req1)[0]
        except:
            continue
        # gs_introduce=html.xpath()
        # gs_num=html.xpath('//ul[@class="promulgator-ul cl"]/li/strong/a[3]/text()')[0]
        # print(duty)

        # print(postion,company,salary,duty,gs_introduce,welfare,gs_url,gs_xz,gs_num,yw,zp_num)
        #
        # sql = "insert into t_zl (conpany,salary,duty,education,zp_num,zy_job,gs_xz,url,gs_fl,gs_introduce,gs_num,postion) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # row_count = cursor.execute(sql,[str(company),str(salary),str(duty),education,zp_num,str(yw),str(gs_xz),str(gs_url),welfare,str(gs_introduce),gs_num,postion])
        # conn.commit()

    num_found=int(datas['data']['numFound'])
    print(num_found)

    start=start+90
    if start>=num_found:
        city_index+=1
        start=0
    if city_index>=len(citys):
        kw_index+=1
        city_index=0
        start=0
    # 当所有条件满足 结束采集
    if kw_index>=len(kws):
        break

