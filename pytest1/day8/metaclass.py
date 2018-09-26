#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:metaclass.py
@time:2018-08-03-20-47
'''
class MyType(type):
    def __init__(self,what,bases=None,dict=None):   #1
        print("---MetaType__init ")
        super(MyType,self).__init__(what,bases,dict)
    def __call__(self, *args, **kwargs):    #2
        print("---MetaType__call")
        obj=self.__new__(self,*args,**kwargs)
        self.__init__(obj,*args,**kwargs)

class Foo(object):
    __metaclass__=MyType
    def __init__(self,name):
        self.name=name
        print("Foo---init__")
    def __new__(cls, *args, **kwargs):
        print("Foo----new__")
        return object.__new__(cls)  #继承父类的__new__方法
#对象的实例化实际上是通过__new()__来调用的
#一般创建类不用自己写new，new一般是从自己父类继承。
#如需定制化自己的类，就可以自己写new方法
f=Foo("Tanghu")
