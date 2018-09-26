#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:direct_consumer.py
@time:2018-09-05 09:22
'''
import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='demo1',exchange_type='direct')

random_queue=channel.queue_declare(exclusive=True)
queue_name=random_queue.method.queue

severities=sys.argv[1:]

if not severities:
    sys.stderr.write("用例：%s [info] [warning] [error]\n" %sys.argv[0])
    sys.exit(1)

for severitie in severities:
    channel.queue_bind(exchange='demo1',queue=queue_name,routing_key=severitie)

print("等待接收新的消息。。。")



def callback(ch,method,properties,body):
    print("%r:%r" %(method.routing_key,body))
channel.basic_consume(callback,queue=queue_name)
channel.start_consuming()