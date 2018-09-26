#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:select_socket_ftp.py
@time:2018-09-03 19:01
'''
import socket
import select
import os
import sys
import queue
import json

#创建一个TCP/IP实例
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置不阻塞
server.setblocking(False)
#绑定连接
server_address=('localhost',9999)
server.bind(server_address)
#设置监听
server.listen(5)

inputs=[server]
outputs=[]
message_queue={}

while inputs:
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)
    for s in readable:
        if s is server:
            client_conn,client_addr=s.accept()
            #设置不阻塞
            s.setblocking(False)
            print("新进入一个链接:{}，连接地址是：{}".format(client_conn,client_addr))
            #放入inputs
            inputs.append(client_conn)
            message_queue[client_conn]=queue.Queue()  #初始化一个队列存要返回给客户端的数据
        else:
            data=s.recv(1024)
            if data:
                print("从{}连接接收到客户端命令：{}".format(client_conn,data))
                message_queue[s].put(data)
                if s not in writeable:
                    outputs.append(s)
            else:
                print("连接断开了")
                if s in writeable:
                    outputs.remove(s)
                inputs.remove(s)

                s.close()
                del message_queue[s]

    for s in writeable:

        try:
            next_data = message_queue[s].get_nowait()
            mesage=json.loads(next_data.decode())
        except queue.Empty:
            print("队列里的数据为空。。。")
            outputs.remove(s)
        else:
            if next_data.decode().startswith('get'):
                # 判断客户端发来的是否是一个文件/文件是否存在
                cmd,filename = data.decode().split()
                if os.path.isfile(filename):
                    f = open(filename, 'rb')
                    # 向客户端发送文件大小
                    file_size = os.stat(filename).st_size
                    s.send(str(file_size).encode())
                    for line in f:
                        s.send(line)
                    else:
                        print("下载成功！")

            elif mesage['action'].startswith('put'):

                '''接收客户端文件'''

                filename = next_data["filename"]
                filesize = next_data["size"]
                if os.path.isfile(filename):
                    f = open(filename + ".new", "wb")
                else:
                    f = open(filename, "wb")
                s.send(b"200 ok")
                received_size = 0
                while received_size < filesize:
                    data = s.request.recv(1024)
                    f.write(data)
                    received_size += len(data)
                else:
                    print("file [%s] has uploaded..." % filename)
    #最后如果socket出错则关闭。
    for s in exceptional:
        print('连接{}异常'.format(s.getpeername()))
        if s in writeable:
            outputs.remove(s)
        inputs.remove(s)
        s.close()
        del message_queue[s]
"fsd".s




