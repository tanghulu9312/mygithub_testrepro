#!/usr/bin/env python
#Author:TangHu

import json
dic={'name':'tanghulu','age':23,'sex':'male'}
j=json.dumps(dic)
f=open(r'C:\Python\practice\json_test.py','w')
#f.write(j)
f.write(str(dic))
f.close()