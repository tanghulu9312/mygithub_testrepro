#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:python_pool.py
@time:2018-08-31 11:30
'''
from multiprocessing import Process,Pool
import time
import os
def run(num):
    time.sleep(2)
    print("hello pool %s" %num)

def call(num):
    print("start exec call ---pid:%s" %(os.getpid()))

if __name__ == '__main__':
    pool=Pool(2)    #允许进程池里同时存在的进程是五个
    for num in range(10):
        #p=pool.apply(func=run,args=(num,))  #串行，同步执行
        #pool.apply_async(func=run,args=(num,))    #并行，异步执行
        pool.apply_async(func=run,args=(num,),callback=call)

    print("parent id:%s"%os.getpid())

    pool.close()
    pool.join()