#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test5.py
@time:2018-08-29 21:12
'''
#递归锁
import threading
import time
num,num2=0,0
lock=threading.RLock()
def run1():
    print("-----run1-----")
    lock.acquire()
    global num
    num+=1
    lock.release()
    return num
def run2():
    print("-----run2-----")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res=run1()
    print("-------between------run1 and run2")
    res2=run2()
    lock.release()
    print(res,res2)

for i in range(3):
    t=t=threading.Thread(target=run3)
    t.start()
while threading.active_count() !=1:
    print("线程个数：",threading.active_count())
else:
    print("--------all threads done------------")
    print(num,num2)