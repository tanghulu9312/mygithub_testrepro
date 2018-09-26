#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_server.py
@time:2018-08-07 15:48
'''
import socket

server=socket.socket()
server.bind(('localhost',8000))
server.listen()
server.accept()

data=server.recv(1024)

print("recv:",data)

server.send(data.upper())
server.close()