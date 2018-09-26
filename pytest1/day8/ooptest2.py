#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:ooptest2.py
@time:2018-07-31-20-19
'''
#面向对象----继承

class company(object):
    def __init__(self,id,name,addr,telphone):
        self.id=id
        self.name=name
        self.addr=addr
        self.telphone=telphone
    def yiled(self):
        print("%s:以经营IT电子产品盈利！" %self.name)
    def info(self):
        print("%s公司 位于: %s ,公司电话号码是：%s" %(self.name,self.addr,self.telphone))

# heidou=company("100010","黑豆","长沙市",18767676767)
#
# heidou.info()
class makeBussines(object):
    def bussines(self,obj):
        print("%s 公司委托 %s公司寻址办公地点租赁" %(self.name,obj.name))

class internet(company,makeBussines):
    def __init__(self,money):
        self.money=money

    def total(self):
        print("本公司法定注册资本是 %d" %self.money)

class sale(company):
    def __init__(self,saler):
        self.saler=saler
    def trands(self):
        print("今年销售人员同比增加%s" %self.saler)





h=internet(900000)

h.id="10086"
h.name="黑豆"
h.addr="长沙市"
h.telphone="89677267"
h.yiled()
h.info()

s=sale("50%")
s.id="10087"
s.name="链家地产"
s.addr="长沙市"
s.telphone="896788989"
s.info()
s.trands()

h.bussines(s)
