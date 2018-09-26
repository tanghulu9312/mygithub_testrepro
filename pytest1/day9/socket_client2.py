#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_client2.py
@time:2018-08-09 16:57
'''
import socket

#生成一个socket实例
client=socket.socket()
#连接服务端
client.connect(("localhost",9000))
#向服务端发送请求
while True:
    chioce=input("input your chioce>>:").strip()
    if len(chioce)==0:
        continue
    client.send(chioce.encode("utf-8"))
    #接收服务器的响应
    data=client.recv(2048)
    print(data)
client.close()
