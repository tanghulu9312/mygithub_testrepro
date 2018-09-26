#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:topic_comsummer.py
@time:2018-09-05 11:57
'''
import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='demo2',exchange_type='topic')

random_queue=channel.queue_declare(exclusive=True)
queue_name=random_queue.method.queue

mesaageTypes=sys.argv[1:]

if not mesaageTypes:
    sys.stderr.write("用例：%s[binding_key]...\n"%sys.argv[0])
    sys.exit(1)

for mesaageType in mesaageTypes:
    channel.queue_bind(queue=queue_name,exchange='demo2',routing_key=mesaageType)

print("等待接收消息。。。")
def callback(ch,method,properties,body):
    print("接收到消息：%s" %body)


channel.basic_consume(callback,queue=queue_name)
channel.start_consuming()