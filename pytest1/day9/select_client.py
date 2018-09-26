#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:select_client.py
@time:2018-09-01 15:33
'''
import socket
import sys

messages=[
    'This is the message',
    'It will be sent',
    'in parts',
]
server_address=('localhost',9999)

#创建一个TCP/IP socket
sockets=[
    socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(400)

]
print('连接到：{} 端口：{}'.format(*server_address),file=sys.stderr)

for s in sockets:
    s.connect(server_address)
#然后它通过每个套接字一次发送一条消息，并在写入新数据后读取所有可用的响应
for message in messages:
    outgoing_data=message.encode()

    #在socket之间发送消息
    for s in sockets:
        print('{}:正在发送 {!r}'.format(s.getsockname(),outgoing_data),file=sys.stderr)
        s.send(outgoing_data)
    for s in sockets:
        data=s.recv(1024)
        print('{}:接收到了 {!r}'.format(s.getsockname(),data),file=sys.stderr)
        if not data:
            print('准备关闭socket',s.getsockname(),file=sys.stderr)

            s.close()
