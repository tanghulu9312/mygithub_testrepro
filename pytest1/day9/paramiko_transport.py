#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:paramiko_transport.py
@time:2018-08-28 21:40
'''
import paramiko

transport=paramiko.Transport('192.168.8.122','22')
transport.connect(username='tanghu',password='admin123')

ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command('ls')
print(stdout.read())
transport.close()