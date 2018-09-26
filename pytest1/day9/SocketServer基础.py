#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:SocketServer基础.py
@time:2018-08-16 08:31
'''
import socketserver

class MySocketServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data.decode())
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("error",e)
                break
if __name__ == "__main__":
    HOST,PORT = "localhost",8000
    server = socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer)
    server.serve_forever()

