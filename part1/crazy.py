#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: crazy.py
@time: 2018/12/17 16:04
@desc:
'''
import copy
#自定义的deepcopy函数
def deepcopy(data):
    #新建的列表
    listdata = []
    if len(data)!=1:
        for i in data:
            #如果i是dict类型的数据，则调用字典处理函数copydict()
            if isinstance(i,dict):
                dictdata = copydict(i)
                listdata.append(dictdata)
            #如果是元组和列表则递归调用deepcopy()函数
            elif isinstance(i,list) or isinstance(i,tuple):
                listdata1 = deepcopy(i)
                listdata.append(listdata1)
            #其他不可变类型的数据就添加到列表listdata中
            else:
                listdata.append(i)
    else:
        return data
    return listdata

#字典类型的处理函数
def copydict(data): 
    dict1 = {}
    #遍历字典
    for keys,values in data.items():
        #以下的每一步的含义与deepcopy中的相似
        if isinstance(values,dict):
            numdict=copydict(values)
            dict1[keys]=numdict
        else:
            value = deepcopy(values)
            dict1[keys]=value
    return dict1
if __name__ == '__main__':
    print({'123':123})