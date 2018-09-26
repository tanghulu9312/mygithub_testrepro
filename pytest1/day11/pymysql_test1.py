#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:pymysql_test1.py
@time:2018-09-18 14:23
'''
import pymysql

#user=input("username:")
#passwd=input("password:")

#获取连接
connection=pymysql.Connect(host='localhost',user='tanghu',password='admin123',database='student');

#获取游标
cur=connection.cursor(cursor=pymysql.cursors.DictCursor)  #默认是元组，可以修改成字典

#执行
# sql="select * from student_info where name=%(u)s and password=%(p)s"
#
# cur.execute(sql,{'u':user,'p':passwd})
sql="select * from user WHERE user_name='%s' and password='%s' "
sql=sql %("' or 1=1 -- ","ad123")
cur.execute(sql)
result=cur.fetchall()
#判断
print(sql)
print(result)

if result:
    print("登录成功。。。")
else:
    print("登录失败。。。")