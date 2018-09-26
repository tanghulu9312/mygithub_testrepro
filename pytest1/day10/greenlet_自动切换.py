#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:greenlet_自动切换.py
@time:2018-08-31 14:17
'''
import gevent

def func1():
    print("start func1...")
    gevent.sleep(2)
    print("begain start func1...")

def func2():
    print("start func2...")
    gevent.sleep(1)
    print("begain start func2...")

def func3():
    print("start func3...")
    gevent.sleep(0)
    print("begain start func3...")


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3)
])