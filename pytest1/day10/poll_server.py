#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:poll_server.py
@time:2018-09-01 16:05
'''
import select
import socket
import queue
import sys

#创建一个TCP/IPsocke
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定连接
server_address=("localhost",9999)
server.bind(server_address)
#监听
server.listen(5)

#与即将发出的消息保持一致
message_queues={}
#传递给的超时值以poll()毫秒而不是秒表示，因此为了暂停一整秒，必须将超时设置为1000。
TIMEOUT=1000
#Python poll()使用一个类来实现，该类管理被监视的已注册数据通道。
# 通过register()使用标志调用来添加通道，该标志指示哪个事件对该通道感兴趣。下表列出了完整的标志集。
#echo服务器将设置一些仅用于读取的套接字，以及其他用于读取或写入的套接字。适当的标志组合保存到局部变量READ_ONLY和 READ_WRITE。
#print(select.POLLIN)
#常用的标记设置
READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE=READ_ONLY | select.POLLOUT
#该server socket被注册，以便任何传入的连接或数据触发一个事件
#设置轮询器
poller=select.poll()
poller.register(server,READ_ONLY)
#由于poll()返回包含套接字文件描述符和事件标志的元组列表，因此需要从文件描述符编号到对象的映射来检索 socket从中读取或写入的内容。

# 将文件描述符映射到socket对象
fd_to_socket = {
    server.fileno(): server,
}
#服务端的循环调用poll()然后通过查找socket并根据事件中的标志采取操作来处理返回的事件。
while True:
    #至少要等一个socket
    #准备处理
    print("等待下一个事件",file=sys.stderr)
    events= poller.poll(TIMEOUT)

    for fd,flag in events:
        #从其文件描述符中检索实际socket
        s=fd_to_socket[fd]
    #与select()主服务器套接字“可读”时一样，这实际上意味着客户端存在挂起的连接。
    # 新连接在READ_ONLY标志中注册，以监视通过它的新数据。
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                #一个可读socket准备好嘞
                #接受一个连接
                connection,client_address=s.accept()
                print('连接',client_address,file=sys.stderr)
                connection.setblocking(0)

                fd_to_socket[connection.fileno()]=connection
                poller.register(connection,READ_ONLY)

                #给连接一个队列以供数据发送
                message_queues[connection]=queue.Queue()
                #服务器以外的套接字是现有客户端，recv()用于访问等待读取的数据。
            else:
                data=s.recv(1024)
            #如果recv()返回任何数据，它将被放入套接字的传出队列中，并且使用modify()
            # 更改该套接字的标志， 因此poll()将监视套接字是否准备好接收数据。
                if data:
                    #一个可读的客户端套接字有数据
                    print('接收到：{!r} 从 {}'.format(data,s.getsockname()),file=sys.stderr)

                    message_queues[s].put(data)
                    #添加响应输出通道
                    poller.modify(s,READ_WRITE)
                else:
                    #将空结果解释为闭合连接
                    print('关闭：',client_address,file=sys.stderr)
                    #停止监听连接上的输入
                    poller.unregister(s)
                    s.close()
                    #移除消息队列
                    del message_queues[s]
        elif flag & select.POLLHUP:
            #客户端挂了
            print('closing',client_address,'HUP',file=sys.stderr)
            #停止监听
            poller.unregister(s)
            s.close()
        #可写套接字的处理类似于示例中使用的版本select()，
        # 除了modify()用于更改轮询器中套接字的标志，而不是从输出列表中删除它。
        elif flag & select.POLLOUT:
            #socket 准备发送数据
            #如果有什么要发送的。
            try:
                next_msg=message_queues[s].get_nowait()
            except queue.Empty:
                print(s.getsockname(),'queue empty',file=sys.stderr)
                poller.modify(s,READ_ONLY)
            else:
                print('sending {!r} to {}'.format(next_msg,s.getsockname()),file=sys.stderr)
                s.send(next_msg)
            #最后，任何POLLERR导致服务端关闭socket的事件
        elif flag & select.POLLERR:
            print('exception on',s.getsockname(),file=sys.stderr)
            #停止监听
            poller.unregister(s)
            s.close()
            #移除消息队列
            del message_queues[s]
