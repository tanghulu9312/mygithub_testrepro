#!/usr/bin/env python
#Author:TangHu
import json
x='[null,1,3,4,5,6]'
#print(eval(x)) 报错，无法解析null类型

print(json.loads(x))
#我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，
# 在Python中叫pickling


dic={'name':'tanghulu','age':25,'sex':'male'}
print(type(dic))

j=json.dumps(dic)
print(type(j))
