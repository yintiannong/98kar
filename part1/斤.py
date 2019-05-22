#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 斤.py
@time: 2019/2/16 10:03
@desc:
'''
# dict1={'niubi':123}
# a=dict1.items()#返回的是个列表 列表镶嵌着元祖
# print(a)



# def yileds():
#     for i in range(10):
#         yield i
#
# if __name__ == '__main__':
#     y=yileds()
#     next(y)
#     next(y)
#     next(y)
#     next(y)
#     next(y)
#     print(next(y))



# list1=[1,2,3,4,5]
# def sss(n):
#     return n*n
# list2=map(sss,list1)
# for i in list2:
#     print(i)



# def multipliers():
#    yield [lambda x : i * x for i in range(4)]
#
# print ([m(2) for m in multipliers()])
#二叉树：

# class Node(object):
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value
# class Tree(object):
#     def __init__(self):
#         self.root=None
#     def add(self,item):
#         if not self.root:
#             self.root=Node(item)
#冒泡：
# string='123 456'
# print(string.split()[2:])

#通过爬虫获取到docx的文件 然后经过docx模块进行处理
# import docx
# cc=docx.Document('G:\\python后续阶段\\第三阶段\\项目\\库表设计.docx')
# list1=cc.paragraphs
# for i in list1:
#     print(i.text)


#图像识别

# def ytn(a):
#     print('修饰一下')
#     return a
#
#
#
# @ytn #ytn(fun)()
# def fun():
#     print(789)
#
#
# fun()
# m=[1,2,3,4,5]
# def fun(m):
#     m2=[]
#     for i in m:
#         m2.append((i-1,i+1))
#     return m2
# if __name__ == '__main__':
#     print(fun(m))


# def fun():
# #     yield 'niubi'
# #
# # print(fun())

# with open(r'G:\学生成绩.doc','r',) as docc:
#     content=docc.readlines()
#     for i in content:
#         print()
#满二叉树的实现：
# class Note:
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value
# class Tree:
#     tree_list=[]
#     def __init__(self):
#         self.root=None
#     def add_node(self,value):
#         node=Note(value)
#         if self.root==None:
#             self.root=node
#             self.tree_list.append(self.root)
#             while True:
#                 if self.tree_list.pop(0).left==None:


#冒泡排序
# a=[5,4,3,2,1]
#
#
def maopao(a):
    length=len(a)
    for i in range(1,length):   #轮次 1 2 3 4
        for j in range(length-i):#次数 4,3,2,1
            if a[j]['age']>a[j+1]['age']:
                a[j],a[j+1]=a[j+1],a[j]
    return a

# if __name__ == '__main__':
#     print(maopao(a))

#选择排序
# def xuanze(a):
#     length=len(a)
#     for i in range(length-1):  #1,2,3,4
#         for j in range(i+1,length):#4 3 2 1
#             if a[i]>a[j]:
#                 a[i],a[j]=a[j],a[i]
#
#     return a
#
# if __name__ == '__main__':
#     print(xuanze(a))



# s='a3i2'
#
# def fun(s):
#     list1=[]
#     for i in s:
#         if i.isalpha():
#             for i in range(2):
#                 list1.append(i)


# def fun(num):
# # #     for i in range(1,num):
# # #         print(' '*(num-i),'*'*i)
# # #
# # # if __name__ == '__main__':
# # #     fun(4)

# a=[1,2,3,4,5,6,7,8,9,10,12,13]
# #
# # def fun(a):
# #     n=0
# #     list1=[]
# #     length=len(a)
# #     while 1:
# #         if n>length-1:
# #             break
# #         list1.append(tuple(a[n:n+3]))
# #         n+=3
# #     return list1
# #
# # if __name__ == '__main__':
# #     print(fun(a))

#通过排序得到
# list1=[{'name':'xiaoming','age':20},{'name':'xiaoming','age':18},{'name':'xiaoming','age':11},{'name':'xiaoming','age':180},{'name':'xiaoming','age':33},{'name':'xiaoming','age':6}]
# print(maopao(list1))
# a=[1,2,3,4,5]
# # # b=sum(map(lambda x:x+3,a))
# # # print(b)
# print([i for i in range(10)])

# list1=[{'name':'xiaoming','age':20},{'name':'xiaoming','age':18},{'name':'xiaoming','age':11},{'name':'xiaoming','age':180},{'name':'xiaoming','age':33},{'name':'xiaoming','age':6}]
# # for k,v in list1[0]:
# #     print(k,v)
#
# def maopao(a):
#     length=len(a)
#     for i in range(1,length):   #轮次 1 2 3 4
#         for j in range(length-i):#次数 4,3,2,1
#             if a[j][2]<a[j+1][2]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a


# with open(r'G:\成绩.doc',encoding='utf-8') as strings:
#    list1=strings.readlines()
#    print(list1)
#    a=maopao(list1)
#    print(''.join(a))
#

# def re(list1):
#     dict1={}
#     for i in list1:
#         k=list1.splite('.')[1]
#         if dict1.get(k):
#             dict1['k']+=1
#         else:
#             dict1['k']=1
#
# dict2={'in':123}
# a=dict2.get('on')
# print(a)
# import os
# import time
# import socket
# content=os.open(r'G:\一天你呢.doc','wr')
# print(content)
