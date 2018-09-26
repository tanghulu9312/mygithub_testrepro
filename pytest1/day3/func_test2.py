#!/usr/bin/env python
#Author:TangHu
#知识点一：局部变量和全局变量
#知识点而：函数递归
#知识点三：高阶函数

#1.局部变量只在函数作用域内起作用
# color="green"
# name="lvluo"
# def test1():
#     name="flower"
#     color="black"
#     print(name,color)
# test1()
# print(color,name)
# def test2(name,color):
#     print("this here office have %s they color is %s" %(name,color))
#
# test2('huaer','green')

#2.递归
# def test3(n):
#     print(n+1)
#     return test3(n+1)
# test3(1)

#3.高阶函数
def test4(a,b,f):
    print(f(a)+f(b))
test4(3,-7,abs)