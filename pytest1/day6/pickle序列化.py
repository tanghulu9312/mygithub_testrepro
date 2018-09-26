#!/usr/bin/env python
#Author:TangHu
import pickle
dic={"name":"tanghulu","address":"ChangSha","Email":10000}

f=open(r'C:\Python\practice\pickle_test.py','wb')

p=pickle.dumps(dic)

f.write(p)
f.close()