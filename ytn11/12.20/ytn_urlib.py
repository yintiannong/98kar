# #!/usr/bin/env python
# # encoding: utf-8
# '''
# @author: 尹田农
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: ytn_urlib.py
# @time: 2018/12/18 17:37
# @desc:
# '''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 14:28
# @Author  : hbw
# @Site    :
# @File    : AI137Urllib.py
# @Software: PyCharm
# 封装urllib
from lxml import etree
import json
from urllib import request as req
from  urllib import parse
from http import cookiejar as cj
# 每次请求携带cookies  # 处理cookies
cookiejar = cj.CookieJar()
cookie_handler = req.HTTPCookieProcessor(cookiejar)
cookie_opener = req.build_opener(cookie_handler)
req.install_opener(cookie_opener)
class Request(object):
    def get_data_from_params(self,params):
        data = {}
        for line in params.split('\n'):
            data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
        return data
    def get(self,url,data={},headers={},proxy={},timeout=10):
        return self.__requset(url,'get',data,headers,proxy,timeout)
    def post(self,url,data={},headers={},proxy={},timeout=10):
        return self.__requset(url, 'post', data, headers, proxy, timeout)
    def __requset(self,url,method,data,headers,proxy,timeout):
        # 处理headers
        myrequest = req.Request(url, headers=headers)
        # 处理ip
        if proxy:
            proxy_handler = req.ProxyHandler(proxy)
            proxy_opener = req.build_opener(proxy_handler)
            req.install_opener(proxy_opener)
        # 处理请求方式
        if method == 'get':
            # 处理参数
            if data:
                url+='?'
                for key,value in data.items():
                    url+=key+'='+value+'&'
                url=url[0:-1]
                myrequest = req.Request(url, headers=headers)
            # 发请求 返回Response对象
            return Response(req.urlopen(myrequest,timeout=timeout).read())
        elif method=='post':
            if data:
                data=parse.urlencode(data).encode('utf-8')
            # 发请求 返回Response对象
            return Response(req.urlopen(myrequest,data=data,timeout=timeout).read())


class Response(object):
    def __init__(self, bytes):
        self.body=bytes
    @property
    def text(self):
        try:
            return self.body.decode('utf-8')
        except:
            try:
                return self.body.decode('gbk')
            except:
                raise ValueError('编码有问题,请用xpath方法直接解析html')
    def xpath(self,str):
        return etree.HTML(self.body).xpath(str)
    @property
    def json(self):
        return json.loads(self.text)