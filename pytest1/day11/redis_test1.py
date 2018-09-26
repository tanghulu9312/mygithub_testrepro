#!/usr/bin/env python
#Author:TangHu

import redis
'''
r=redis.Redis(host='localhost',port=6379)
r.set('name','tanghu')
print(r.get('name'))
'''

pool=redis.ConnectionPool(host='localhost',port=6379)
r=redis.Redis(connection_pool=pool)
r.set('name','tanghu')
print(r.get('name'))