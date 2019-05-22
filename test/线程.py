#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 线程.py
@time: 2019/2/13 17:55
@desc:
'''
# import webbrowser
# with open(r'C:\Users\尹田农\Desktop\尹田农.txt','r') as q :
#     print(q.readline())
#     print(q.readline())
#     q.seek(0)
#     print(q.readline())
#     print(q.readlines())




#
# import copy
# l1 = [1,2,3,[11,22,33]]
# l2 = copy.deepcopy(l1)
# l1[3][0]=5
# print(l2)


#
# print('{0} 呵呵'.format('python','566456'))


# import re
# print(re.search("func", "f6unction")) match 和seacher的区别



# import random
# a=random.random()
# print(a)

# import sys
# import time
# import poplib
# import smtplib
# from email.mime.text import MIMEText
# #邮件发送函数
# from email.utils import formataddr
#
#
# def send_mail():
#
#     handle = smtplib.SMTP('smtp.163.com', 25)
#     handle.login('yintiannong@163.com','1314lsz')
#     msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
#     msg['From'] = formataddr(["发件人邮箱昵称", 'yintiannong@163.com'])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#     msg['To'] = formataddr(["收件人邮箱昵称", '1532295578@qq.com'])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#     msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题
#     print(msg)
#     a=handle.sendmail('yintiannong@163.com', '1532295578@qq.com',msg.as_string())
#     print(a)
#     handle.close()
#     print(4556)
#
# if __name__ == '__main__':
#     send_mail()
#
#

# import os.path
# def jun(*args,**kwargs):
#     print(args,kwargs)
#
# import socket
# if __name__ == '__main__':
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('localhost', 8001))
#     sock.listen(5)
#
#     while True:
#         connection,address = sock.accept()
#         try:
#             connection.settimeout(5)
#             buf = connection.recv(1024)
#             if buf == '1':
#                 connection.send('welcome to server!')
#             else:
#                 connection.send('please go out!')
#         except socket.timeout:
#             print ('time out')
# import psutil
# import socket
# import os, datetime, time
# a=socket.socket.bind()
# print(a)
# def getIp():
#     print(socket.getaddrinfo(socket.gethostname(),None))
# def getMemCpu():
#     data = psutil.virtual_memory()
#     total = data.total  # 总内存,单位为byte
#     free = data.available  # 可以内存
#     print(free)
#     memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + " "
#     cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
#     return memory + cpu
#
#
# def main():
#     while True:
#         info = getMemCpu()
#         time.sleep(0.2)
#         print(info)


import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, World")


def main1():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 80))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main1()