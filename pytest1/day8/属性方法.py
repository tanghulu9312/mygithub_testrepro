#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:属性方法.py
@time:2018-08-05 14:50
'''
'''
class Dog(object):
    def __init__(self,name):
        self.name=name
    @property
    def eat(self):
        #属性方法的作用就是通过@property把一个方法变成一个静态属性
        print("%s is eating" %self.name)

d=Dog("HuaHua")
d.eat
'''
#属性方法的应用----检查航班状态
class Flight(object):
    def __init__(self,name):
        self.flight_name=name

    def checking_status(self):
        print("checking flight %s status" %self.flight_name)
        return 1
    @property
    def flight_status(self):
        status=self.checking_status()
        if status==0:
            print("%s航班被取消了。。。" %self.flight_name)
        elif status==1:
            print("%s航班已到达！" %self.flight_name)
        elif status ==2:
            print("%s航班延误。。。" %self.flight_name)
        else:
            print("不能检查%s航班状态，请稍后再试。" %self.flight_name)
    #修改航班状态
    @flight_status.setter
    def flight_status(self,status):
        status_dic={
            0:"被取消",
            1:"已到达",
            2:"已延误"
        }

        print("\033[31;1m 航班状态已经被改变成 %s\033[0m" %status_dic.get(status))
    #删除航班状态
    @flight_status.deleter
    def flight_status(self):
        print("航班状态已被删除。")

f=Flight("C910")
f.flight_status
f.flight_status=2
del f.flight_status
