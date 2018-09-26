#!/usr/bin/env python
#Author:TangHu
import shelve
'''
s = shelve.open('test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
finally:
    s.close()
'''
s=shelve.open('test_shelf.db')
try:
    existing=s['key1']
finally:
    s.close()

print(existing)