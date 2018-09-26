#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:socket_ssh_server.py
@time:2018-08-10 10:27
'''
import  socket
import os
import time
#生成一个socket实例
server=socket.socket()
#绑定IP和端口
server.bind(("localhost",8989))
#监听客户端
server.listen()

while True:
    #等待得到一个新的连接：
    conn,addr=server.accept()
    print("new conn:",addr)
    while True:
        #接收从客户端发来的指令
        client_cmd=conn.recv(1024)
        #执行命令
        cmd_res=os.popen(client_cmd.decode()).read()
        #判断执行命令的结果是否存在
        if len(cmd_res)==0:
            print("%s命令没有输出" %client_cmd)
        #现将命令结果的大小发给客户端
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
        time.sleep(0.5)
        # 将命令执行结果返回给客户端
        conn.send(cmd_res.encode("utf-8"))
        print("服务端发送数据完成。")
server.close()