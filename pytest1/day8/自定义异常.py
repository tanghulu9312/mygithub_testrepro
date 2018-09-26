#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:自定义异常.py
@time:2018-08-09 21:21
'''
class SelfException(Exception):
    def __init__(self,msg):
        self.message=msg
    def __str__(self):
        return self.message

try:
    raise SelfException("我自己定义的异常")
except SelfException as e:
    print(e)