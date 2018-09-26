#!/usr/bin/env python
#Author:TangHu
import pickle
'''
import json

info={
    "name":"zhangsan",
    "age":25,
    "birthday":"10月24日"
}

f=open("test.txt",'w')
f.write(json.dumps(info))
f.flush()
f.close()
'''
def sayhi(name):
    print(" hi ",name)

info={
    "name":"zhangsan",
    "age":25,
    "birthday":"10月24日",
    "func":sayhi
}
f=open("test.txt",'w')
f.write(pickle.dumps(info))
f.flush()
f.close()