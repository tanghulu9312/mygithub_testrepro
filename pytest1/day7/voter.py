#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:voter.py
@time:2018-07-28-14-18
'''
#检查投票情况，如果是第一次投可以，如果投过了就不能再投
voted={"zhangsan":True,"lisi":True}
def check_voter(name):
    if voted.get(name):
        print("他已经投过票了！")
    else:
        voted[name]=True
        print("让他投票！")

check_voter("lisi")
