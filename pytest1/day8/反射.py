#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:反射.py
@time:2018-08-03-21-18
'''
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d=Dog("HuaHua")
def talk(self):
    print("%s 在大叫" %self.name)
#根据用户输入的不同调用不同的方法
choice=input(">>:").strip()
#hasattr判断一个对象里是否有对应的字符串的方法
if hasattr(d,choice):
    #getattr根据字符串找到对象里的对应的方法的内存中的地址
    #getattr(d,choice)("水果")
    #setattr(d,choice,"张三") #改变实例对象的属性值
    delattr(d,choice)   #删除实例对象的属性值
else:
    #对象里没有该方法则创建
    setattr(d,choice,None)
    print(getattr(d,choice))
    #setattr(d,choice,22)
    #print(getattr(d,choice))
print(d.name)