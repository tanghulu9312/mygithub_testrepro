#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:py_inherit.py
@time:2018-07-31-21-20
'''
"""
py2 经典类是按深度优先来继承的，新式类是按广度优先来继承
py3 经典类和新式类都是按广度有限来继承的
"""
class A(object):
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    def __init__(self):
        print("C")
class D(B,C):
    pass
    # def __init__(self):
    #     print("D")
d=D()