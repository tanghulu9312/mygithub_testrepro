#!/usr/bin/env python
#Author:TangHu
import time

def consumer(name):
    print("准备吃包子啦~")
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))



def producer(name):
    c1=consumer("zhangsan")
    c2=consumer("lisi")
    c1.__next__()
    c2.__next__()
    print("我要开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c1.send(i)
        c2.send(i)
producer("tanghu")