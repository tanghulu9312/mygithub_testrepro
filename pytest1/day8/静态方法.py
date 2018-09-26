#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:静态方法.py
@time:2018-08-01-21-04
'''
class Animal(object):
    m=123
    def __init__(self,name,fur):
        self.name=name
        self.fur=fur
    def eat(self):
        pass
    @staticmethod
    def animal(self):
        #静态方法是不可以访问实例变量和类变量的方法
        print(self.name)

class Cat(Animal):
    def eat(self):
        print("%s is eating fish!" %self.name)

class Dog(Animal):
    def eat(self):
        print("%s is eating 骨头！" %self.name)

c=Cat("mimi","blak")
d=Dog("Wowa","yellow")
# Animal.animal(c)
# Animal.animal(d)

d.animal()