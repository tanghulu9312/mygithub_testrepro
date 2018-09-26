#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:__new__.py
@time:2018-08-03-20-30
'''
#Python中一切皆对象，类其实也是对象。那么类的类是谁?type
class Foo(object):
    def __init__(self,name):
        self.name=name

f=Foo("Alex")
print(type(f))
print(type(Foo))
#创建类的方式：
def __init__(self,name,age):
    self.name=name
    self.age=age

def func(self):
    print("hello %s" %self.name)

Tang=type("Tang",(object,),{'func':func,'__init__':__init__})

print(type(Tang))
t=Tang("tanghu",22)
t.func()
