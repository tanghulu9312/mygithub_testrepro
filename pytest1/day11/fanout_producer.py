#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:fanout_producer.py
@time:2018-09-04 20:52
'''
import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

messages="hello Rabbits world"

channel.exchange_declare(exchange='demo',exchange_type='fanout')

channel.basic_publish(exchange='demo',routing_key='',properties=pika.BasicProperties(delivery_mode=2),body=messages)

print("发布消息完成。")

channel.close()