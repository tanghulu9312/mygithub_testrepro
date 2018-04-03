#!/usr/bin/env python
#Author:TangHu
# name="tanghu"
# passwd="admin"
count=0
#1.提示用户输入用户名和密码
while count<3:
    username=input("请输入用户名：")
    password=input("请输入您的密码：")
    readinfo=open(r"c:\Python\practice\logininfo.txt",'r')

    readname=readinfo.readline()
    readpasswd=readinfo.readline()

    index1=readname.index('"')+1
    name=readname[index1:-2]

    index2=readpasswd.index('"')+1
    passwd=readpasswd[index2:-1]
    print(passwd)
    print(name)

    if (username==name) & (password==passwd):
        print("登录成功，欢迎进入XXXX系统！")
        break
    else:

        print("用户名或者密码错误，请重新登录。")
    count+=1
else:
    print("输入错误超过三次，请两小时后再登录")