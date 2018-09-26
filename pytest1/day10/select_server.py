#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:select_server.py
@time:2018-09-01 14:51
'''
import socket
import select
import sys
import queue

#生成一个socket实例
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)


server_address=("localhost",9999)
print("starting up on {} port {}".format(*server_address),file=sys.stderr)
#绑定地址和端口
server.bind(server_address)
#监听传入的连接
server.listen(5)
'''
参数select()是包含要监视的通信通道的三个列表。
第一个是要检查要读取的传入数据的对象列表，
第二个包含在缓冲区中有空间时将接收传出数据的对象，
第三个包含可能有错误的对象（通常是错误的组合输入和输出通道对象）。
服务器的下一步是设置包含要传递给的输入源和输出目标的列表select()。
'''
#
inputs=[server]
outputs=[]
'''
服务器主循环将连接添加到这些列表中或从这些列表中删除。
由于此版本的服务器将在发送任何数据之前等待套接字变为可写（而不是立即发送回复），
因此每个输出连接都需要一个队列作为通过它发送数据的缓冲区。
'''
message_queus={}
'''主要部分循环，调用select()阻塞并等待网络活动。'''
while inputs:
# Wait for at least one of the sockets to be
# ready for processing
    print("waiting for the next event",file=sys.stderr)
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)
    '''
    select()返回三个新列表，包含传入列表内容的子集。
    列表中的所有套接字 readable都有缓冲的传入数据，可供读取。
    writable列表中的所有套接字都在其缓冲区中有可用空间并可以写入。
    返回的套接字 exceptional有错误（“异常条件”的实际定义取决于平台）。
    
    “可读”套接字代表三种可能的情况。如果套接字是主“服务器”套接字，
    用于监听连接的套接字，那么“可读”条件意味着它已准备好接受另一个传入连接。
    除了将新连接添加到要监视的输入列表之外，此部分还将客户端套接字设置为不阻止。
    '''
    for s in readable:
        if s is server:
            connection,client_address=s.accept()
            print('connection from',client_address,file=sys.stderr)

            connection.setblocking(0)
            inputs.append(connection)

            message_queus[connection]=queue.Queue()
       #下一种情况是与已发送数据的客户端建立连接。
        #读取数据recv()，然后将其放在队列中，以便可以通过套接字发送回客户端。
        else:
            data=s.recv(1024)
            if data:
                print('received {!r} from {}'.format(data,s.getpeername()),file=sys.stderr,)
                message_queus[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            #没有可用数据的可读套接字来自已断开连接的客户端，并且流已准备好关闭。
            else:
                print('closing',client_address,file=sys.stderr)
                #停止监听
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                del message_queus[s]
        '''可写连接的情况较少。如果队列中有数据用于连接，则发送下一条消息。
        否则，将从输出连接列表中删除连接，以便下次循环时select()
        不指示套接字已准备好发送数据。'''
    for s in writeable:
        try:
            next_msg=message_queus[s].get_nowait()
        except queue.Empty:
            #没有等待的消息停止检查
            print(' ',s.getpeername(),'queue empty',file=sys.stderr)
            outputs.remove(s)
        else:
            print('sending {!r} to {}'.format(next_msg,s.getpeername()),file=sys.stderr)
            s.send(next_msg)

    #最后，如果socket出错，则关闭
    for s in exceptional:
        print('exceptional condition on',s.getpeername(),file=sys.stderr)
        #停止监听连接上的输入
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        #移除消息队列
        del message_queus[s]
