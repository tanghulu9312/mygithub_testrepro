#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_server1.py
@time:2018-08-07 17:20
'''
import socket
#1.获得一个socket
server=socket.socket()
#2.建立和服务端的连接
server.bind(("localhost",8000))
#3.监听从客户端发来的请求
server.listen()
#4.等待连接
conn,addr=server.accept()
print(conn,addr)
#5.获取从客户端发来的数据
data=conn.recv(2048)
print("recv:",data)
#6返回客户端数据
conn.send(b"hello world this is socket server...")
#6.关闭连接
server.close()