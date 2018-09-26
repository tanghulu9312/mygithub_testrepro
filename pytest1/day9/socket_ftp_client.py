#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_ftp_client.py
@time:2018-08-10 16:39
'''
import socket
import hashlib
client=socket.socket()

client.connect(('localhost',9090))
while True:
    cmd=input(">>:").strip()
    if len(cmd)==0:continue
    if cmd.startswith("get"):
        #向服务端发送请求
        client.send(cmd.encode())
        #接收从服务端的响应结果
        file_size=client.recv(1024)
        print("server response:" ,file_size)
        client.send(b"ready to recv file")
        file_total_size=int(file_size.decode())
        recevied_size=0
        filename=cmd.split()[1]

        f=open(filename+'.new',"wb")
        m=hashlib.md5()
        while recevied_size < file_total_size:
            if file_total_size-recevied_size>1024:
                size=1024
            else:
                size=file_total_size-recevied_size
            #接收从服务端发过来的数据
            data=client.recv(size)
            recevied_size+=len(data)
            m.update(data)
            f.write(data)
        else:
            new_flie_md5=m.hexdigest()
            print("file recv done",recevied_size,file_total_size)
            f.close()
        client_file_md5=client.recv(1024)
        print("client file md5:",client_file_md5)
        print("server file md5:",new_flie_md5)
client.close()