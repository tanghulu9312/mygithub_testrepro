#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:Demo.py
@time:2018-08-05 17:27
'''
class Demo(object):
    def __init__(self,name):
        self.name=name

    def info(self):
        print("my name is %s" %self.name)
def myinfo(self):
    print("my info is %s" % self)
#判断类里有没有这个方法，有就调用
d=Demo("zhangsan")
chioce=input(">>:")

if hasattr(d,chioce):
    getattr(d,chioce)()
else:
    setattr(d,chioce,myinfo)
    getattr(d,chioce)("zhangsan")