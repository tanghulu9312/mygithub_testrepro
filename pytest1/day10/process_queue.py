#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:process_queue.py
@time:2018-08-31 09:42
'''
from multiprocessing import Process,Queue
import time
def f(qq):
    print("in child:",qq.qsize())
    #print("in fuc f q value:%s"%qq.get())
    qq.put(("zhangsan",23,"gsd",[2,33]))

if __name__ == '__main__':
    q=Queue()
    q.put("test")
    p=Process(target=f,args=(q,))

    p.start()
    p.join()
    print("start:",q.get_nowait())