#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:队列.py
@time:2018-08-30 15:25
'''
import queue
#先进先出
q=queue.Queue()
q.put("disk a")
q.put("disk b")
q.put("disk c")

for i in range(q.qsize()):
    print(q.get())

#后进先出 last in first out
q1=queue.LifoQueue()
q1.put(1)
q1.put(2)
q1.put(3)

for m in range(q1.qsize()):
    print(q1.get())

#优先级队列
q2=queue.PriorityQueue()

q2.put((10,"zhangsan"))
q2.put((2,"lisi"))
q2.put((12,"wangwu"))
q2.put((3,"zhaoliu"))


for m in range(q2.qsize()):
     print(q2.get())