#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:select_test_server.py
@time:2018-09-03 14:16
'''
import select
import socket
import queue

#创建一个TCP/IPsocket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
#绑定连接
server_addr=('localhost',9999)
server.bind(server_addr)
#监听
server.listen(5)

inputs=[server]
outputs=[]
msg={}

while inputs:
    readable,writable,exceptional=select.select(inputs,outputs,inputs)

    for s in readable:
        if s is server:

            conn, addr = s.accept()
            print('进来一个新连接：%s' %conn)
            conn.setblocking(False)
            inputs.append(conn)
            msg[conn]=queue.Queue()
        else:
            data=s.recv(1024)
            if data:
                print('从%s接收到数据：%s' % (s.getpeername(),data))
                msg[s].put(data)

                if s not in outputs:
                    outputs.append(s)
            else:
                print('客户端关闭了，从%s读完之后没有数据接收'%conn)

                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del msg[s]

    for s in writable:
        try:
            next_msg=msg[s].get_nowait()
        except queue.Empty:
            print('from {} send data is empty'.format(s.getpeername()))
            outputs.remove(s)
        else:
            print('start send message {} to {}'.format(next_msg,s.getpeername()))
            s.send(next_msg)

    for s in exceptional:
        print('处理异常情况 {}'.format(s.getpeername()))
        inputs.remove(s)

        if s in outputs:
            outputs.remove(s)
        s.close()
        del msg[s]
