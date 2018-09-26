#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:描述类.py
@time:2018-08-05 16:02
'''
class Dog(object):
    """这是一个用于构建狗实例的类"""
    def __init__(self,name):
        self.name=name
    def info(self):
        print("my name is %s" %self.name)
    def __call__(self, *args, **kwargs):
        print("__cal__方法")
    def __str__(self):
        print("__str__")
        name="我是str函数的返回值"
        return name
    def __getitem__(self, name):
        print("__getitem__",name)
    def __setitem__(self,name, value):
        print("__setitem__",name,value)
    def __delitem__(self, key):
        print("__delitem__",key)

d=Dog("HuaHua") #执行__init__
print(d.__doc__)   #输出类的描述信息

print(d.__module__) #表示当前操作的对象在哪个模块

print(d.__class__)  #表示当前操作的对象的类是什么

#print(d.__init__()) #构造方法，通过类创建对象时，自动触发执行

#d.__del__析构方法，当对象在内存中被释放时，自动触发执行。
#此方法一般无需定义，一般都是交给Python解释器执行，析构函数的执行是由解释器在进行垃圾回收时自动触发执行的

#d() 构造方法的执行是由创建对象触发的，即对象=类名();而对于__call_-方法的执行是由对象加括号触发执行的
#d()执行__call__方法

print(d.__dict__)   #查看类或对象中的所有成员

print(d)    #如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值

d[d.name]
d["name"]="zhangsan"
#del d.name
print(d.name)
