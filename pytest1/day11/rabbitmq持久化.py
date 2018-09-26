#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:rabbitmq持久化.py
@time:2018-09-04 19:48
'''
import pika

#生成一个连接
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#生成一个队列
channel=connection.channel()
#声明一个队列
channel.queue_declare(queue='hello5',durable=True)
#发布消息
channel.basic_publish(exchange='',routing_key='hello5',body='hello world5...!',properties=pika.BasicProperties(delivery_mode=2))

channel.close()
