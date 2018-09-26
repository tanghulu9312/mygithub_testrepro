#!/usr/bin/env python
#Author:TangHu
# -*- coding: GBK -*-
#文件修改练习

f=open('hello_openfile.txt','r',encoding='utf-8')
f_new=open('hello_openfile.txt.bak','w',encoding='utf-8')

for line in f.readlines():
    if '呼唤我姓名' in line:
        line=line.replace('呼唤我姓名','认真呼唤唐虎的姓名')
    f_new.write(line)