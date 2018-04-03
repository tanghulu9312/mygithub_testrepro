#!/usr/bin/env python
#Author:TangHu
name="tanghu"
name="TangHu"
title="my Name Is tanghu  "
print(title.count('a'))    #统计字符串出现的次数
print(name.capitalize())   #首字母大写
print(name)
print(name.casefold())      #我理解的是初始化吧不会返回变量的新值
print(title.center(20,'*')) #总长度为20居中对齐，不够位的以*号左右两端补齐
print(title.find('m'))      #查找某个字符串的字符，找到第一次出现的位置，立即返回它的索引

info="my age is {age} and addr is {addr}"

print(info.format(age=12,addr="changsha"))      #格式化输出
print(info.format_map({"age":12,"addr":"changsha"}))        #格式化输出,可以传入一个字典
item="asfe"
print(item.isdigit())       #判断是否为纯数字
print(title.index('m'))     #查找某个字符串的字符，找到第一次出现的位置，立即返回它的索引(跟find方法的作用类似)
print(item.isalnum())       #判断字符串是否是一个含有大小写字母，数字的字符串
print(item.isalpha())       #判断字符串是否只包含字母
print(item.isdecimal())     #判断字符串是否是一个十进制的整数
print(item.isidentifier())  #判断字符串是否是一个合法的标识符
print(title.islower())      #判断字符串是否都是小写字母
print(item.isnumeric())     #判断是否为纯数字,用法跟isdigit()类似
print(item.isprintable())   #判断是否是可打印的
print(item.isspace())       #判断是否是一个空格
print(title.istitle())      #判断是是否是一个标题 （首字母大写）
print(item.isupper())       #判断字符串是否都是大写字母
print("+".join(item))       #返回一个字符串，它是字符串的连接iterable。元素之间的分隔符是"+"。
print(item.ljust(10,"*"))   #在Unicode字符串的长度宽度中返回左对齐。填充使用指定的填充字符完成（默认是空格）
print(item.rjust(10,"*"))   #在Unicode字符串的长度宽度中返回右对齐。填充使用指定的填充字符完成（默认是空格）
print("".maketrans("a","A"))     #
print(title.partition('Is'))#把一个字符串分成头部+分割字符+尾部
print(title.rstrip())
print(title.split(' '))     #分割字符串
print(item.startswith("A")) #判断是否以A开头
print(title.strip())        #去掉首尾两端的空格
print(item.swapcase())      #大写转小写，小写转大写
print(title.title())        #将字符串转换成一个标题（首字母大写）

'''
speak=input("请输入你想问的：")

intab = "今天星期几？"
outtab = "今天星期四"
trantab = speak.maketrans(intab, outtab)  # 制作翻译表


#translate(table) 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,
#要过滤掉的字符放到 deletechars 参数中；table -- 翻译表，翻译表是通过 maketrans() 方法转换而来

print(speak.translate(trantab))
'''

print(item.upper())     #转换成大写
