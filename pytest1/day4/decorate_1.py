#!/usr/bin/env python
#Author:TangHu
#装饰器联系

#（1）函数即变量
#（2）不改变被装饰函数代码
#（3）不改变被装饰函数调用方式
import time


# def decorate_test():
#     print("记录日志...")
#
# def test1():
#     decorate_test()
#     print("in the test1....")
# test1()

def timer(func):
    def decorate(*args,**kwargs):
        start_time=time.time()
        time.sleep(3)
        func(*args,**kwargs)
        stop_time=time.time()
        print("这个函数的运行时间是：%s秒" %(stop_time-start_time))

    return decorate

@timer
def test1():
    print("in the test1....")

@timer
def test2(name,age):
    print("test2:",name,age)

# test1=timer(test1)
# test1()

test1()
test2("tanghu",23)