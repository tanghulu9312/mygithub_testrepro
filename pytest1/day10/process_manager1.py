#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:process_manager1.py
@time:2018-08-31 10:25
'''
from multiprocessing import Process,Manager
import os

def f(d,l):
    d[1]="123"
    d['2']=2
    d["pid %s" %os.getpid()]=os.getpid()
    l.append(1)
    print("----------in the func f------")
    print(l)
    print(d)
if __name__ == '__main__':
    with Manager() as manager:
        d=manager.dict()
        l=manager.list(range(5))

        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        l.append("in the parent")
        print("----------in the func main------")
        print(d)
        print(l)
