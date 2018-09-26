#!/usr/bin/env python
#Author:TangHu
import pickle

f=open(r'C:\Python\practice\pickle_test.py','rb')
data=pickle.loads(f.read())
print(data)