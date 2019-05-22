#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: exe.py
@time: 2019/1/7 17:46
@desc:
'''
import os
from openpyxl import load_workbook
paths='G:\python后续阶段\第三阶段\项目\数据清洗\excel'
path_name=os.listdir(paths)
for i in path_name[2:]:
    print(i)
    workbook = load_workbook(u'G:\python后续阶段\第三阶段\项目\数据清洗\excel\\'+i)
    booksheet = workbook.active
    # 获取sheet页的行数据
    rows = booksheet.rows
    # 获取sheet页的列数据
    columns = booksheet.columns
    for j in rows:
        list1=[]
        for k in j:
            list1.append(k.value)
        print(list1)
