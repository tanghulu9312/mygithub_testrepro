#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_ssh_client.py
@time:2018-08-10 10:46
'''
import socket

client=socket.socket()

client.connect(("localhost",8989))

while True:
    #发送数据给服务端
    client_cmd=input(">>:").strip()
    if len(client_cmd)==0:
        continue
    client.send(client_cmd.encode("utf-8"))


    #接收从服务器端发来的命令结果大小
    cmd_recevide_size=client.recv(1024)
    print("cmd recevide total size:%s" %cmd_recevide_size)
    recevied_size = 0
    res_data = b""
    while recevied_size<int(cmd_recevide_size.decode()):
        data=client.recv(1024)
        recevied_size+=len(data)
        res_data+=data
    else:
        print("命令执行完成。",recevied_size)
        print(res_data.decode())
client.close()
