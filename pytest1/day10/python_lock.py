#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:python_lock.py
@time:2018-08-31 11:04
'''
from multiprocessing import Process,Lock

def run(l,num):
    #l.acquire()
    print("hello python process %s" %num)
    #l.release()

if __name__ == '__main__':
    lock=Lock()
    for num in range(20):
        p=Process(target=run,args=(lock,num,))
        p.start()