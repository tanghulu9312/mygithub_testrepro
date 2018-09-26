#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:ooptest.py
@time:2018-07-31-14-26
'''


class Role(object):
    #类变量
    n=123
    n_list=[]
    #私有的变量
    __private_var="can`t edit"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("%s shooting..." %self.name)

    def got_shot(self):
        print("ah...,%s got shot..." %self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name))


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
#实例变量
r1.n="from r1 edit"
r1.n_list=["i am r1"]

print("r1:",r1.n,r1.n_list)

r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
print("r2:",r2.n,r2.n_list)

r1.got_shot()
r2.buy_gun("M416")