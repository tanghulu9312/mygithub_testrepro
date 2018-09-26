#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:fanout_consummer.py
@time:2018-09-04 20:57
'''
import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='demo',exchange_type='fanout')

random_queue=channel.queue_declare(exclusive=True,durable=True)
queue_name=random_queue.method.queue

channel.queue_bind(queue=queue_name,exchange='demo')
def callback(ch,propertites,method,body):
    print("接收到消息：%s" %body)



channel.basic_consume(callback,queue=queue_name)

channel.start_consuming()