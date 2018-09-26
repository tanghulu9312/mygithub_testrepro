#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test3.py
@time:2018-08-29 20:11
'''
import threading
import time

def run(n):
    print('[%s]-------runing-----\n' %n)
    time.sleep(2)
    print('-----done-----')

def main():
    for i in range(5):
        t=threading.Thread(target=run,args=(i,))
        t.start()
        t.join(1)#让线程等待
        print('starting thread',t.getName())

m=threading.Thread(target=main,args=[])
m.setDaemon(True) #将main线程设置为Daemon线程，他作为程序主线程的守护线程
m.start()
m.join(timeout=1)
print("-----------main threadin done----------")