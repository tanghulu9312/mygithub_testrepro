#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:rabbitmq_test_client.py
@time:2018-09-04 17:17
'''
import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.queue_declare(queue='hello5',durable=True)

def callback(ch,method,properties,body):
    print("[X] 接收到消息%s" %body)
channel.basic_consume(callback,queue='hello5',no_ack=True)

print("等待接收消息。。。")

channel.start_consuming()