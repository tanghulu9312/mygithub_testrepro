#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:main.py
@time:2018-08-18 11:58
'''
import socketserver
import json
import os
class FtpServer(socketserver.BaseRequestHandler):
    def put(self,*args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f=open(filename+".new","wb")
        else:
            f=open(filename,"wb")
        self.request.send(b"200 ok")
        received_size=0
        while received_size < filesize:
            data=self.request.recv(1024)
            f.write(data)
            received_size+=len(data)
        else:
            print("file [%s] has uploaded..." %filename)

    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic=json.loads(self.data.decode())
                action=cmd_dic["action"]
                if hasattr(self,action):
                    func=getattr(self,action)
                    func(cmd_dic)
            except ConnectionResetError as e :
                print("error",e)
                break
if __name__ == "__main__":
    HOST,PORT = "localhost",8000
    server=socketserver.ThreadingTCPServer((HOST,PORT),FtpServer)
    server.serve_forever()