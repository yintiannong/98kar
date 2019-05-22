#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: list_pachong.py
@time: 2018/12/20 19:21
@desc:
'''
#管理urls
from lxml import etree
import requests

class DFS(object):
    def __init__(self):
        self.unvisited=[]
        self.visited=[]
    #存储未访问url
    def save_unvisted(self,url):
        if url not in self.unvisited and url not  in self.visited and url.startswith('http'):
            self.unvisited.append()
    #调取未访问的url
    def put_unvisted(self):
        return self.unvisited.pop()
    #存储已访问的url
    def save_visited(self,url):
        self.visited.append(url)
    def stop(self):
        return self.unvisited


#管理爬虫c
class Crawer(object):
    #准备好容器
    def __init__(self):
        self.dfs=DFS()
    #处理我们的信息
    def crawers(self,host):
        #把首页存进容器
        self.dfs.save_unvisted(host)
        while 1:
            #取出未访问的url
            url=self.dfs.put_unvisted()
            html=etree.HTML(requests.get(url=url))
            self.dfs.save_visited(url)
            urls = html.xpath('//a/@href')
            for i in urls:
                self.dfs.save_unvisted(i)
                #把界面爬出的http开头的链接加入到容器中