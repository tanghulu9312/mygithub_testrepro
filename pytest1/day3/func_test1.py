#!/usr/bin/env python
#Author:TangHu
'''
函数特点：
1.代码复用
2.可扩展性
'''
#
#
# def test1(x,y):
#     print(x)
#     print(y)
# #test1(1,2)   #与形参一一对应
# test1(y=3,x=2)    #与形参无关
#
# #test1(y=90,2) #位置参数不能在关键词参数后面
#
# def test2(x,y,z):
#     print("this is ",x)
#     print("this is ",y)
#     print("this is ",z)
# test2(2,z=8,y=90)
#
# #默认参数特点：调用函数的时候，默认参数非必填
# def test3(x,y=45):
#     print("this is ",x)
#     print("this is ",y)
# test3(2,y=90)
# test3(20)
#
#
# #实参不固定,args:接受多个位置参数
# def test4(*args):
#     print(args)
#
# test4(1,12,32,32,32,32)
# test4(*['a','b','c'])
#
# def test5(x,*args):
#     print(x)
#     print(args)
# test5(2,3,4,5,6,7)

#**kwargs:把N个关键字参数，转换成字典的方式
# def test6(**kwargs):
#     print(kwargs)
# test6(**{'luoqiang':32,'sex':'M'})
# test6(name='tanghu',age=25)
#test6(3,4)
# def test7(name,*args,**kwargs):
#     print(name)
#     print(*args)
#     print(kwargs)
# test7('tanghu',age='23',sex='falman')
#
# def test7(name,age=42,*args,**kwargs):
#     print(name)
#     print(age)
#     print(args)
#     print(kwargs)
#
# test7('tanghulu',53,habbix='baskteball')

'''
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()
'''

'''
def tester(start):
    state=start
    def nested(label):
        print(label,state)
    return nested
F=tester(0)
F('abcd')
'''

'''
def tester2(start):
    state=start
    def nested(lable):
        nonlocal state
        print(lable,state)
        state+=1
    return nested
F=tester2(0)
F('abcd')
F('SPAM')
F('CHAIN')
G=tester2(99)
G('TANGHULU')
G('FAFI')
F('BOOK')
'''

'''
spam=99
def tester3():
    #spam = 99
    def nested():
        nonlocal spam
        print("current:",spam)
        spam+=1
    return nested
F=tester3()
F()
F()
'''

'''
def tester(start):
    global state
    state=start
    def nested(lable):
        global state
        print(lable,"current:",state)
        state+=1
    return nested

F=tester(59)
F("jams")
F("Curry")

G=tester(0)
G('Tompson')
G("Smith")
F("This value is F...")
'''











