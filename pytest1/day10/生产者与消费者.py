#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:生产者与消费者.py
@time:2018-08-30 15:46
'''
import threading,time
import queue
q=queue.Queue()
count=0
def Producer(name):
    while True:
        global count
        q.put("包子%s"%count)
        count+=1
        time.sleep(1)
def Consumer(name):
    while True>0:
        print("%s 取到 %s 并且吃了它。。。"%(name,q.get()))

p=threading.Thread(target=Producer,args=("zhangsan",))
p.start()
c=threading.Thread(target=Consumer,args=("小花",))
c1=threading.Thread(target=Consumer,args=("小黄",))
c.start()
c1.start()