#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test4.py
@time:2018-08-29 20:34
'''
import threading
import time
num=0
def run(n):
    lock.acquire()
    global num
    num+=1
    lock.release()
lock=threading.Lock()

t_obj=[]
for i in range(1000):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()
print("---------all threads has finished------",threading.current_thread())
print("num:",num)