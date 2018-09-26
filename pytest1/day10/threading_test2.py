#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test2.py
@time:2018-08-29 20:03
'''
#线程继承式调用
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num

    def run(self):#定义每个线程要运行的函数
        print("runing on number:%s" %self.num)
        time.sleep(3)

if __name__== '__main__':
    t1=MyThread(1)
    t2=MyThread(2)
    t1.start()
    t2.start()
