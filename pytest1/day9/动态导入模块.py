#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:动态导入模块.py
@time:2018-08-09 21:31
'''

import importlib
Demo=importlib.import_module("lib.Demo")
print(Demo.Demo("动态导入").tell())

