#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:简单爬虫.py
@time:2018-08-31 15:06
'''
from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all()  #把当前程序的所有IO操作作上标记
def f(url):
    print("GET:%s" %url)
    resp=request.urlopen(url)
    data=resp.read()
    print("%d bytes received from %s." %(len(data),url))
    f=open("pachong.html",'wb+')
    f.write(data)
urls=[
    #'https://www.python.org',
    'https://www.hnjtjh.com/traffic_index/Dynamic_work.php',
    'https://baijiahao.baidu.com/s?id=1597728095861104318&wfr=spider&for=pc'
]
time_start=time.time()
for url in urls:
    f(url)
print("同步cost",time.time()-time_start)
async_time=time.time()
gevent.joinall([
    #gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://www.hnjtjh.com/traffic_index/Dynamic_work.php'),
    gevent.spawn(f,'https://baijiahao.baidu.com/s?id=1597728095861104318&wfr=spider&for=pc')
])
print("异步cost:",time.time()-async_time)
