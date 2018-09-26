#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:paramiko模块.py
@time:2018-08-21 20:48
'''
import paramiko
#创建SSH对象
ssh=paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.8.122',port=22,username='tanghu',password='admin123')
#执行命令
stdin,stdout,stderr=ssh.exec_command('ping -c 3 192.168.8.22')
#获取命令结果
result=stdout.read()
print(result)
#关闭连接
ssh.close()
