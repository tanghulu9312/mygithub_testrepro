#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_client1.py
@time:2018-08-07 17:24
'''
import socket
client=socket.socket()
#1.建立连接
client.connect(("localhost",8000))
#2.发送数据
client.send(b"hello world this is socket client...")
#3.接收数据
data=client.recv(2048)
print(data)
#4.关闭连接
client.close()