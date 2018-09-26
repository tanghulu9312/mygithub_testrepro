#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_ftp_server.py
@time:2018-08-10 16:21
'''
import socket
import os,hashlib,time
server=socket.socket()

server.bind(('localhost',9090))
server.listen()

while True:
    conn,addr=server.accept()
    print("new conn",addr)
    while True:
        #服务端收到客户端发过来的命令
        cmd_data=conn.recv(1024)
        if not cmd_data:
            print("客户端已断开。")
            break
        #判断是收到的是否是一个文件
        cmd,filename = cmd_data.decode().split()
        print(filename)

        if os.path.isfile(filename):

            f=open(filename,'rb')
            m=hashlib.md5()
            file_size=os.stat(filename).st_size
            #向客户端发送文件大小
            conn.send(str(file_size).encode())

            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print("send done")
server.close()