#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:类方法.py
@time:2018-08-05-14-44
'''
#类方法和普通方法的区别是：类方法只能访问类变量，不能访问实例变量。
class Dog(object):
    name="我是类变量"    #类变量
    def __init__(self,name):
        self.name=name  #实例变量

    @classmethod
    def eat(self):
        print("%s is eating" %self.name)

d=Dog("HuaHua")
d.eat()