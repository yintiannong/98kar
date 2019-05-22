#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 脚本.py
@time: 2019/5/16 17:08
@desc:
'''
import os
import sys
import re
def get_dir_name(path):
    return os.listdir(path)
def get_start_shell(path):
    rule='csc_admin_start.sh'
    for i in get_dir_name(path):
        if re.match(rule,i):
            print(i)
            return i
def get_stop_shell(path):
    rule = 'csc-admin-stop.sh'
    for i in get_dir_name(path):
        if re.match(rule, i):
            return i
def start(path):
    os.chdir(path)
    os.popen('su kds'+'&&sh'+get_start_shell(path))
def stop(path):
    os.chdir(path)
    os.system('su kds'+path+'&&sh'+get_stop_shell(path))

if __name__ == '__main__':
    start(r'/opt/kds/mobile-stock/bin')