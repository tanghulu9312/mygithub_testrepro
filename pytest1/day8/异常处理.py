#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:异常处理.py
@time:2018-08-09 21:10
'''
a=3
b="tang"
dic=["abc","tanghulu"]
try:
    dic[3]
    #c=a+b
    #from day8 import aa
    #print(c)

except TypeError as e:
    print(e.args)
except ImportError as e:
    print(e.args)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("主代码执行完，执行该块")
finally:
    print("捕获异常小练习...finally,有错没错都会执行！")