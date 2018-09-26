#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:direct_publisher.py
@time:2018-09-05 09:12
'''
import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()
channel.exchange_declare(exchange='demo1',exchange_type='direct')

severity=sys.argv[1] if len(sys.argv) > 1 else 'info'

message=''.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='demo1',routing_key=severity,body=message)

print("发送：%r:%r" %(severity,message))
connection.close()