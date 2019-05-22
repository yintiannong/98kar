#!/usr/bin/ python
#
import os
import sys
import re
def get_pwd(part):
    a=os.walk(part)
    return list(a)
def next(part):
    pwd=get_pwd(part)
    dirs_list=pwd[0][2]
    return dirs_list
def runing(path):
    a=os.chdir(path)
    b=os.getcwd()
    starts=[]
    stops=[]
    rule_start='(start)'
    rule_stop='(stop)'
    for i in next(path):
        p1=re.findall(rule_start,i)
        p2=re.findall(rule_stop,i)
        if p1:
            starts.append(i)
        if p2:
            stops.append(i)
    print(starts)
    print(stops)


if __name__ == '__main__':
    # next(r'/opt/kds/mobile-stock/bin')
    runing(r'/opt/kds/mobile-stock/bin')
