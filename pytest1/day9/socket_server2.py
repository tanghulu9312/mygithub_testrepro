#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_server2.py
@time:2018-08-09 17:01
'''
import socket


server = socket.socket()
#
server.bind(("localhost", 9000))
# 监听客户端
server.listen()
while True:
    # 等待客户端连接
    conn, addr = server.accept()
    print(conn, addr)
    while True:

        #接收从客户端发来的请求
        data=conn.recv(2048)
        print(data)
        print(("请求收到，等待发送数据"))
        #响应客户端的请求
        conn.send(b"from the server....")
server.close()
