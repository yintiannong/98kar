#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: model.py
@time: 2018/12/18 22:51
@desc:
'''
from urllib import parse
import urllib.request as req

class Request(object):
    def get(self,url,data={},header={},cookie={},proxy={},timeout=10):
        print(123)
        return self.__request(url,'get',data,header,cookie,proxy,timeout)
    def post(self,url,data,header=None,cookie=None,proxy=None,timeout=10):
        pass
    def __request(self,url,method,data,header={},cookie={},proxy={},timeout=10):
        #处理header


        #处理请求参数和请求方式
        if method=='get':
            print(456)
            if data:
                print(789)
                url+='?'
                for k,v in data.items():
                    url+=(str(k)+'='+str(v)+'&')
                url=url[0,-1]


        if method=='post':
            data = parse.urlencode(data).encode('utf-8')
        myrequest = req.Request(url, headers=header)
        return Response(req.urlopen(myrequest).read())


class Response(object):
    def __init__(self,content):
        self.content=content
    @property
    def text(self): #属性
        try:
            text=self.content.decode('utf-8')
            return text
        except:
            try:
                text = self.content.decode('gbk')
            except:
                return '自己解决'
    @property
    def xpath(self):
        pass