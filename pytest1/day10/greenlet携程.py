#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:greenlet携程.py
@time:2018-08-31 14:04
'''
from greenlet import greenlet
def test1():
    print("a")
    gr2.switch()
    print("c")
    gr2.switch()


def test2():
    print("b")
    gr1.switch()
    print("d")
gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()