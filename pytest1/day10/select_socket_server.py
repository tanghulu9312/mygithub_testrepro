#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:select_socket_server.py
@time:2018-09-01 12:00
'''
import socket
import select
import queue

server=socket.socket()
server.bind(("localhost",9999))
server.listen(1000)

server.setblocking(False) #设置不阻塞
msg_dic = {}

inputs = [server,]

outputs = []

while True:
    readbale,writeable,exceptional=select.select(inputs,outputs,inputs)
    print(readbale,writeable,exceptional)
    for r in readbale:
        if r is server:#代表来了一个新连接
            conn,addr=server.accept()
            print("来了个新连接：",addr)
            inputs.append(conn)
            #要想实现这个客户端发来的数据时server端能知道，就需要让select再
            #监测这个conn
            msg_dic[conn]=queue.Queue()#初始化一个队列，存要返回给这个客户端的数据
        else:
            data=r.recv(1024)
            print("收到数据",data)
            msg_dic[r].put(data)

            outputs.append(r)#放入返回的连接队列里
    for w in writeable:
        data_to_client = msg_dic[w].get()
        w.send(data_to_client) #返回给客户端源数据
        outputs.remove(w) #确保下次循环的时候writeable,不返回这个已处理的连接了
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]