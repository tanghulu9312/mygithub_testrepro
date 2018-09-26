#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:proccess_test.py
@time:2018-08-31 09:11
'''
import multiprocessing
import os

def run():
    print("start running.....")
    print("child process pid:%s" %os.getpid())
    print("parent pid:%s" % os.getppid())
def f():
    run()


if __name__ == '__main__':
    p1=multiprocessing.Process(target=f)
    p1.start()
    print(os.getpid())

