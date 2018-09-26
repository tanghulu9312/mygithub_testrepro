#!/usr/bin/env python
#Author:TangHu
import json

f=open("test.txt",'r')
text=json.loads(f.read())
print(text)
print(type(text))
print(text["birthday"])