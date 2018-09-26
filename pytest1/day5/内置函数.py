#!/usr/bin/env python
#Author:TangHu
import  functools

'''
res=filter(lambda n:n>5,range(10))
for i in res:
    print('i:',i)

common=map(lambda k:k*k,range(20))
for j in common:
    print('j:',j)
'''

'''
res=functools.reduce(lambda x,y:x+y,range(10))
print(res)
'''

a=set([123,23,232,54,32])
d=frozenset(a)

print(globals())