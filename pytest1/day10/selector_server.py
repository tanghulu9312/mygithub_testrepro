#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:selector_server.py
@time:2018-09-02 11:08
'''
import selectors
import socket
import types

sel=selectors.DefaultSelector()
lsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind(('localhost',9999))

lsock.listen(5)
print('listen on',('localhost',9999))
lsock.setblocking(False)

sel.register(lsock,selectors.EVENT_READ,data=None)
'''
sel.register()sel.select()为您感兴趣的事件注册要监视的套接字。
对于侦听套接字，我们需要读取事件：selectors.EVENT_READ。

data用于存储您想要的任何数据以及套接字。
它返回时select()返回。我们将用它data来跟踪套接字上发送和接收的内容。
'''
def accept_wrapper(sock):
    conn,addr=sock.accept()
    print('accepted connection from',addr)
    conn.setblocking(False)
    data=types.SimpleNamespace(addr=addr,inb=b'',outb=b'')
    events=selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn,events,data=data)

def service_connection(key,mask):
    sock=key.fileobj
    data=key.data
    if mask & selectors.EVENT_READ:
        recv_data=sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to',data.addr)
            sel.unregister(sock)
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print('echoing',repr(data.outb),'to',data.addr)
                sent=sock.send(data.outb)
                data.outb=data.outb[sent:]
#接下来是事件循环
while True:
    events=sel.select(timeout=None)
    for key,mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key,mask)









