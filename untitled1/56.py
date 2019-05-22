#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 56.py
@time: 2019/5/17 9:32
@desc:
'''
import subprocess
import os
import pwd
import sys
def check_status_test(path):
    os.chdir(path)
    a=os.popen('')
    print(a.read())
if __name__ == '__main__':
    check_status_test(r'G:\测试')