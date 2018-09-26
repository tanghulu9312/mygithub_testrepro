#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test6.py
@time:2018-08-29 21:42
'''
import threading,time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%s\n"%n)
    semaphore.release()
if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    for i in range(21):
        t=threading.Thread(target=run,args=(i,))
        t.start()



