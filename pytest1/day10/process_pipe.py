#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:process_pipe.py
@time:2018-08-31 10:11
'''
from multiprocessing import Process,Pipe

def f(conn):
    conn.send(["name","password","address"])
    print("child recv:",conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(child_conn,))
    p.start()
    print("parent recv:",parent_conn.recv())
    parent_conn.send(["username","passwd","addr"])
    p.join()