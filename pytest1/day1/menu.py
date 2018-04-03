#!/usr/bin/env python
#Author:TangHu
#需求：三级菜单，可依次进入各子菜单
#一级：网站栏目
# 二级：编程语言：Java，php,python,c语言
# 二级：软件设计：架构设计，面向对象，设计模式
# 二级：数据库技术：MySQL，sqlserver,oracle,NoSql

#定义一个网站栏目的列表，作为一级栏目名称

menu={
    "website":[
        {"programLanguage":["java","php","python","c语言"]},
        {"programDesign":["架构设计","面向对象","设计模式"]},
        {"database":["Mysql","oracle","NoSql","sqlserver"]},
    ]
}

#设置系统界面
while True:
    print("*"*30)
    print(" "*30)
    print(" "*8,"*欢迎进入博客园*"," "*10)
    print(" "*8,"1.进入一级菜单"," "*10)
    print(" "*8,"2.进入二级菜单"," "*10)
    print(" "*8,"3.进入三级菜单"," "*10)
    print(" "*30)
    print("*"*30)
    #提示用户选择
    choice=input("请选择：")
    if choice=="1":
        templist=list(menu.keys())
        for temp in templist:
            print(temp)
    elif choice=="2":
        for temp2 in menu.values():
            for t2 in temp2:
                for i in t2.keys():
                    print(i)

    elif choice=="3":
        for temp3 in menu.values():
            for t3 in temp3:
                for j in t3.values():
                    print(j)
    elif choice==0:
        break