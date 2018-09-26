#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:rabbitmq_test1.py
@time:2018-09-04 16:26
'''
import pika

#生成一个连接
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#生成一个管道
channel=connection.channel()
#生成一个队列
channel.queue_declare(queue="hello")
#RabbitMQ消息永远不能直接发送到队列，它总是需要经过一个交换。
channel.basic_publish(exchange='',routing_key='hello',body="hello world!")

print("Start send 'hello world' ")

connection.close()
