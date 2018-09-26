#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:创建类的第二种方法.py
@time:2018-08-05 16:43
'''

def talking(self):
    print("%s正在学英语。。" %self.name)
def __init__(self,name):
    self.name=name
#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员
Demo=type("Demo",(object,),{"__init__":__init__,"func":talking})
d=Demo("zhangsan")
print(d.func())
