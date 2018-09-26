#!/usr/bin/env python
#Author:TangHu
import hmac
h=hmac.new('abc'.encode('utf-8'))

h.update('hello'.encode('utf-8'))
print(h.hexdigest())

#要想保证hmac最终结构一致，必须保证：
#1：hmac.new括号内指定的初始key一样
#2：无论update多少次，校验的内容累加到一起是一样的内容

h1=hmac.new(b'admin')
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2=hmac.new(b'admin')
h2.update(b'helloworld')
print(h2.hexdigest())

h3=hmac.new(b'adminhelloworld')
print(h3.hexdigest())