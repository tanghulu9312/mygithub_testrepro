#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:红绿灯.py
@time:2018-08-30 14:49
'''
import threading
import time

event=threading.Event()

def light():
    event.set()
    count=0
    while True:
        if count > 5 and count < 10:
            event.clear()#把标志位清了
            print("\033[41;1m red light is on ....\033[0m")
        elif count > 10:
            event.set()
            count = 0
        else:
            print("\033[42;1m green light is on....\033[0m")
        time.sleep(1)
        count+=1

def car(name):
    while True:
        if event.is_set():#代表绿灯
            print("%s is running..."%name)
            time.sleep(1)
        else:
            print("%s sees red light,waiting..." %name)
            event.wait()
            print("\033[34;1m  green light is on ,%s start going....\033[0m" %name)

l=threading.Thread(target=light)
l.start()
c=threading.Thread(target=car,args=("法拉利",))
c.start()