#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: spiders.py
@time: 2018/12/28 17:48
@desc:
'''
import re
import requests
def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

import scrapy
class Spiders_dazhong(scrapy.Spider):
    name = 'dz'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

    def start_requests(self): #
        url1='http://www.dianping.com/citylist'
        request=scrapy.Request(url=url1,headers=self.headers)
        request.meta['proxy'] = 'http://101.4.136.34:80'
        yield request
    def parse(self, response): #拿到所有城市
        urls=response.xpath('//div[@class="findHeight"]/a/@href').extract()
        cookies='''navCtgScroll:0
_hc.v:2d9ff4c9-c328-8d78-9f6f-dad4f49e7bb9.1527647254
_lxsdk_cuid:163aedf40b1bb-0feb67110a6e9c-7c117d7e-1fa400-163aedf40b2c8
_lxsdk:163aedf40b1bb-0feb67110a6e9c-7c117d7e-1fa400-163aedf40b2c8
_lx_utm:utm_source%3DBaidu%26utm_medium%3Dorganic
s_ViewType:10 
aburl:1
Hm_lvt_dbeeb675516927da776beeb1d9802bd4:1545993996
wed_user_path:163|0
cy:2
cityid:2
cye:beijing
Hm_lpvt_dbeeb675516927da776beeb1d9802bd4:1545996173
cy:2 
cye:beijing
_lxsdk_s:167f509ed62-20-6a-c0%7C%7C102'''
        cookies=get_data_from_params(cookies)
        headers = '''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding:gzip, deflate
        Accept-Language:zh-CN,zh;q=0.9
        Cache-Control:max-age=0
        Connection:keep-alive
        Host:www.dianping.com
        Upgrade-Insecure-Requests: 1
        User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'''
        headers=get_data_from_params(headers)
        for i in urls:
            url2='http:'+i+'/ch10'
            yield scrapy.Request(url=url2,headers=headers,cookies=cookies,callback=self.parse1)
    def parse1(self,response):
        urls=response.xpath('//div[@id="classfy"]/a/@href').extract()
        for i in urls:
            # print(i)
            rea=scrapy.Request(url=i,headers=self.headers,callback=self.parse3)
            yield rea
    def parse3(self,response):
        city=response.xpath('//div[@id="region-nav"]/a/@href').extract()
        for i in city:
            # print(i)
            yield scrapy.Request(url=i,headers=self.headers,callback=self.parse4)
    def parse4(self,response):
        urls=response.xpath('//div[@class="tit"]/a/@href').extract()
        for i in urls:
            pp=scrapy.Request(url=i,headers=self.headers,callback=self.parse5)
            pp.meta['proxy'] = 'http://101.4.136.34:80'
            yield pp
        try:
            next_page=response.xpath('//div[@class="page"]/a[last()]/@title')[0].extract()

            if next_page=='下一页':
                    url6=response.xpath('//div[@class="page"]/a[last()]/@href')[0].extract()
                    yield scrapy.Request(url6,headers=self.headers,callback=self.parse4)
        except:
            pass
    def parse5(self,response):
        css_html=get_css_html(response.text)
        # numcb = re.search(r'id="reviewCount".*?>[\s\S]*?class="(\w\w)-\w{4}"', response.text).group(1)
        # b=get_kjs(a,numcb)

        shop_name=response.xpath('//h1[@class="shop-name"]/text()').extract()[0]
        print(css_html)
        num=response.xpath('//span[@id="address"]/text()|//span[@id="address"]/span/@class').extract()


def get_css_html(html):
    '''
    获取css文件的内容
    '''
    # 从html中提取css文件的url
    regex = re.compile(r'(s3plus\.meituan\.net.*?)\"')
    css_url = re.search(regex, html).group(1)
    css_url = 'http://' + css_url
    # 得到css文件的内容
    resp = requests.get(css_url)
    css_html = resp.content.decode('utf-8')
    return css_html

def get_kjs(css_html, numcb):
    '''
    获取kj开头的class属性对应显示的文字字典
    '''
    # 从css_html中提取kj的svg文件url
    regex = re.compile(r'\[class\^="%s-"\][\s\S]*?url\((.*?)\)' % numcb)
    svg_url = re.search(regex, css_html).group(1)
    if svg_url.startswith('//'):
        svg_url = 'http:' + svg_url
    # 得到svg文件内容
    resp = requests.get(svg_url)
    svg_html = resp.text
    # 从svg内容中提取10位数字
    number = re.search(r'\d{10}', svg_html).group()
    # 匹配出以kj-开头的class属性中的偏移量
    regex_kj = re.compile(r'\.(%s-\w{4})[\s\S]*?-(\d+)' % numcb)
    kjs = re.findall(regex_kj, css_html)
    # 根据偏移量排序
    kjs.sort(key=lambda x: int(x[1]))
    # 将class属性其真正显示的数字组成字典
    kjs = {i[0]: number[n] for n, i in enumerate(kjs)}

    return kjs

