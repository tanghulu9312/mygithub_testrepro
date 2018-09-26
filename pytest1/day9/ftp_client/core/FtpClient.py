#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:FtpClient.py
@time:2018-08-18 12:02
'''
import socket
import os
import json
class FtpClient(object):
    def __init__(self):
        self.client=socket.socket()

    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)

    def connector(self,ip,port):
        self.client.connect((ip,port))

    def interactive(self):
        while True:
            cmd=input(">>:").strip()
            if len(cmd)==0:continue
            cmd_str=cmd.split()[0]
            if hasattr(self,"cmd_%s" %cmd_str):
                func=getattr(self,"cmd_%s" %cmd_str)
                func(cmd)
            else:self.help()

    def cmd_put(self,*args):
        #把文件名和文件大小发送给服务端
        cmd_args=args[0].split()
        if len(cmd_args)>1:
            filename=cmd_args[1]
            if os.path.isfile(filename):
                file_size=os.stat(filename).st_size
                meg_dic={
                    "action":"put",
                    "filename":filename,
                    "size":file_size,
                    "overridden":True
                }
                self.client.send(json.dumps(meg_dic).encode("utf-8"))
                #防止粘包
                server_response=self.client.recv(1024)
                f=open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success...")
            else:
                print(filename,"file not exist")
    def cmd_get(self,*args):
        cmd_args=args[0].split()
        if len(cmd_args)>1:

            self.client.send(args[0].encode())
            #防止粘包
            # 接收从服务端的响应结果
            file_size = self.client.recv(1024)
            print("server response:", file_size)
            self.client.send(b"ready to recv file")
            file_total_size = int(file_size.decode())
            recevied_size = 0


            f = open(cmd_args[1] + '.new', "wb")

            while recevied_size < file_total_size:
                if file_total_size - recevied_size > 1024:
                    size = 1024
                else:
                    size = file_total_size - recevied_size
                # 接收从服务端发过来的数据
                data = self.client.recv(size)
                recevied_size += len(data)

                f.write(data)
            else:

                print("file recv done", recevied_size, file_total_size)
                f.close()





















cli=FtpClient()
cli.connector("localhost",9999)
cli.interactive()