#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_client.py


@time:2018-08-07 15:14
'''

import socket
client=socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))
while True:
    cli_input=input(">>:").strip()
    if not cli_input:
        continue
    client.send(cli_input.encode("utf-8"))
    data=client.recv(1024)
    print("recv:",data)
client.close()