#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test7.py
@time:2018-08-30 08:36
'''
import threading
#递归锁和互斥锁的区别

num=0
lock=threading.Lock()
def baozi():
    print("开始做包子了。。。。")
    lock.acquire()
    global num
    num+=1
    lock.release()
    print("做了%s个包子"%num)
    print("-"*20)

def eat():
    print("准备吃包子了。。。。")
    lock.acquire()
    global num
    lock.release()
    print("吃了%s个包子"%num)
    print("-" * 20)
for i in range(50):
    bz=threading.Thread(target=baozi)
    bz.start()

    et = threading.Thread(target=eat)
    et.start()



while threading.active_count() !=1 :
    print("当前线程数是：",threading.active_count())
else:
    print("----------主线程执行完毕-------------")