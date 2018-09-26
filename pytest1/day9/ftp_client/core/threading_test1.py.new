#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:threading_test1.py
@time:2018-08-28 21:47
'''
import threading

def run(n):
    print("test %s" %n)

t1=threading.Thread(target=run,args=(1,))
t2=threading.Thread(target=run,args=(2,))
t1.start()
t2.start()

print(t1.getName())
print(t2.getName())