#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:hostsmanager.py
@time:2018-08-30 16:42
'''
import configparser
import paramiko
import queue
'''
需求:
主机分组
主机信息配置文件用configparser解析
可批量执行命令、发送文件，结果实时返回，执行格式如下 
batch_run  -h h1,h2,h3   -g web_clusters,db_servers    -cmd  "df -h"　
batch_scp   -h h1,h2,h3   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/　
主机用户名密码、端口可以不同
执行远程命令使用paramiko模块
批量命令需使用multiprocessing并发
'''
q=queue.Queue()
cf=configparser.ConfigParser(allow_no_value=True)
cf.read("hostconfig")   #读取配置文件
sections=cf.sections()  #获取分组
while True:
    print("1.主机分组信息")
    print("2.批量执行命令")
    choice=input("请输入您的选择：").strip()
    if choice=="1":
        for sec in sections:
            print(sec)
        while True:
            name=input("请输入您想查看的主机分组名(按q返回上一级):")
            if name.upper() == "Q":
                break
            if cf.has_section(name):
                str_host=cf.get(name,"hostname").split(",")
                str_ip=cf.get(name,"ip").split(",")
                str_port = cf.get(name, "port").split(",")
                str_username = cf.get(name, "username").split(",")
                str_password=cf.get(name, "password").split(",")
                print(str_password,str_username)
                for host in str_host:
                    print(host)
                while True:
                    operter_host=input("输入你想操作的主机(按q返回上一级)：")
                    if operter_host.upper() == "Q":
                        break
                    if operter_host in str_host:
                        n=str_host.index(operter_host)
                        while True:
                            cmd=input("请输入你想执行的命令(按q返回上一级)：")
                            if cmd.upper()=="Q":
                                break
                            ssh=paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
                            ssh.connect(hostname=str_ip[n],port=str_port[n],username=str_username[n],password=str_password[n])

                            stderr,stdout,stdin=ssh.exec_command(cmd)
                            print(stdout.read())
                            print(stderr.read())
