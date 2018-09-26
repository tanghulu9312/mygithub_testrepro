#!/usr/bin/env python
#Author:TangHu
import pickle

dic={"name":"tanghulu","address":"ChangSha","Email":10000}
print(type(dic))
p=pickle.dumps(dic)
print(type(p))

