#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:topic_publiser.py
@time:2018-09-05 11:20
'''
import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='demo2',exchange_type='topic')
messageType=sys.argv[1] if len(sys.argv)>1 else 'anonymous.info'
message=''.join(sys.argv[2:]) or 'hello world! this is exchange-topic'

channel.basic_publish(exchange='demo2',routing_key=messageType,body=message)