#!/usr/bin/env python
#Author:TangHu
import hashlib
#利用md5进行用户登陆网站进行注册之后密码加密的基本事例，加深理解

def md5(arg):   #这是加密函数，将传进来的函数加密
    md5_pwd=hashlib.md5(bytes('abc',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()

def log(user,pwd): #登录时候的函数，由于md5不能反解，因此登录的时候用正解
    with open('db.config','r',encoding='utf-8') as f:
        for line in f:
            u,p = line.strip().split('|')
            if u==user and p == md5(pwd):   #登录时验证用户名以及加密的密码跟之前的保存是否一样
                return True

def register(user,pwd): #注册的时候把用户名和加密的密码写进文件，保存起来
    with open('db.config','a',encoding='utf-8') as f:
        temp=user+'|'+md5(pwd)
        f.write(temp)

i=input('1.表示登录，2.表示注册')
if i == '2':
    user=input('用户名：')
    pwd=input('密码：')
    register(user,pwd)
elif i == '1':
    user=input('输入登录用户名：')
    pwd=input('输入登录密码：')
    r=log(user,pwd)
    if r==True:
        print("登录成功！")
    else:
        print("登陆失败")
else:
    print("账号不存在！")