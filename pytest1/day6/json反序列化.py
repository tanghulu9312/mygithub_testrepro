#!/usr/bin/env python
#Author:TangHu
import json

f=open(r'C:\Python\practice\json_test.py')
date=json.loads(f.read())

print(date)