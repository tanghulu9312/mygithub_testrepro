#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:pymysql_test2.py
@time:2018-09-18 15:05
'''
#需求：用户登录后，查看所拥有的权限

import pymysql
#inp=input("choice:")
#passwd=input("password:")
connection=pymysql.Connect(host='localhost',user='tanghu',password='admin123',database='student')

cur=connection.cursor()
# inp_int=[]
# for i in inp.split():
#     inp_int.append(int(i))
# inp_tup=tuple(inp_int)
#sql="select * from user where user_name=%s and password=%s"
#sql="select * from user"
#sql="insert into user(user_name,user_age,password) values(%s,%s,%s)"
sql="insert into user(user_name,user_age,password) values(%s,%s,%s)"
#sql="delete from user where user_id = %s"
#sql="update user set user_name=%s where user_id=%s"
'''
#cur.execute(sql,(user,passwd))
#查询结果只有一个
#result=cur.fetchone()
cur.execute(sql)
result=cur.fetchone()
print(result)
result=cur.fetchone() #指针自动往下移动
print(result)
cur.scroll(1,mode='absolute')  #指针回滚到绝对位置
result=cur.fetchone()
print(result)
cur.scroll(1,mode='relative')   #指针回滚到相对位置
result=cur.fetchone()
print(result)
'''
'''
#查询结果有多个
cur.execute(sql)

cur.fetchall()   #取所有的查询结果
'''

user_list=[
    ("haoqianlong",22,'admin'),
    ("zhangjinliang",22,'admin'),
    ("zhengyizhou",20,'admin')
]
#批量插入
cur.executemany(sql,user_list)

print(cur.lastrowid)
connection.commit()

'''
#删除
print(inp_tup)
cur.execute(sql,inp_tup)
connection.commit()
'''

'''
#修改
cur.execute(sql,("童琦龙",5))
connection.commit()

cur.close()
connection.close()
'''




































