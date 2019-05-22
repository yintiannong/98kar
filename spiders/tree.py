#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: tree.py
@time: 2019/1/15 21:55
@desc:
'''
# 节点 存的值；左节点；有节点
class Node(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
#根节点 添加节点 属性
class tree(object):
    def __init__(self):
        self.root=None   #开始 是可以 什么都没有的 包括根节点
    def add_node(self,item):
        node=Node(item)
        if not self.root:
            self.root=node
            return
        else:
            duilie=[self.root]
        #从队列中拿出 未访问的 节点
        while 1:
            node1=duilie.pop(0)
        #判断左节点是否为空
            if not node1.left:
                node1.left=node
                return
            elif not node1.right:
                node1.right=node
                return
            else:
                duilie.append(node1.left)
                duilie.append(node1.right)
        #没有 添加

        #有 判断右节点是否为空
        #空 添加 不空 就将左右节点加入队列
    #根 左 右
    def xianxu(self,node):
        if not node:
            return []
        gen=[node]
        left=self.xianxu(node.left)
        right=self.xianxu(node.right)
        return gen+left+right

    # 左 根 右
    def zhongxu(self,node):
        if  not node:
            return []
        gen = [node]
        left = self.zhongxu(node.left)
        right = self.zhongxu(node.right)
        return left+gen+right

import random
array=list(range(10))
random.shuffle(array)

def faster(list1):
    if len(list1)<=1:
        return list1
    
if __name__ == '__main__':
    a=tree()
    for i in range(1,8):
        a.add_node(i)

    for i in a.zhongxu(a.root):
        print(i.item,end=' ')