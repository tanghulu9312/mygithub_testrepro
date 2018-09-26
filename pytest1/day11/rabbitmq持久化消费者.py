#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:rabbitmq持久化消费者.py
@time:2018-09-04 19:53
'''
import pika
import time

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='hello5',durable=True)

def callback(ch,method,properties,body):
    print('接收到消息：%s' %body)
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,queue='hello5')
print('等待接受消息。。。')
time.sleep(30)
channel.start_consuming()