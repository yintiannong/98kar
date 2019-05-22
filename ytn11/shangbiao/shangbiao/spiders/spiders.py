#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: spiders.py
@time: 2018/12/29 14:13
@desc:
'''
import  scrapy
class Sb(scrapy.Spider):
    name = 'sb'
    def start_requests(self):
        url='http://wsjs.saic.gov.cn/txnRead02.ajax?MmEwMD=3.wgi7xrHHHZcbOtYyoXEdoR_jhkFQPC6xlHwcZYCFPUdY09AhcQYKJgVtCV_j12G19eRv_mEU_tXcqvj94FsTf06NgXhBGbSztewt0qc4.cdV.cVHcyNuIyO4OfVB5PIrYtYvGBPlX5kKM0.7pwaqrLf9N6m8X.0ZSAdFVmEpJKjR1F_0Jw3tUdpgzPwRheMZssG0yizipg8X7cVsPD1x73gvBxUOeAU3fH8E5B5mUfHTHIY0rx8h5p45ddXQvsj3aYNLv6E.sPFHrgfL8E55CeoNS4VHE0D4sRclNYCSGzi7SVaunO_uUeZ_usVtLcfAK_rebnh25iQk5EkUPlUMMRLPPl5kcZw28HmNJR8slYfjtMiVBGixr.T.9OBSFYqaY7La5afoaEGoTbCPsvO86er6m_YTzrebaNohAcVOICZxtSq.o7ToxpjhLELMwG_lAmoXOLu5rkiI1Y073wtsdD2'
        yield scrapy.Request(url=url)
    def parse(self, response):
        print(response.text)