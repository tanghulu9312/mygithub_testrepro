#!/usr/bin/env python
#Author:TangHu
# -*- coding: GBK -*-

#读写文件练习

'''
f=open('hello_openfile.txt','r',encoding='utf-8');
data=f.read()
print(data)
'''
'''
#以写模式打开文件会创建一个新的文件
f=open('openfile1.txt','w',encoding='utf-8')
f.write('abcdefg')
f=open('hello_openfile.txt','r',encoding='utf-8')
print(f.read())
'''
'''
#以追加模式打开文件，则会将写入的内容追加到文件末尾
f=open('hello_openfile.txt','a',encoding='utf-8')
f.write('\nabcdefghijkmnopqrstuvwxyz')
f=open('hello_openfile.txt','r',encoding='utf-8')
print(f.read())
'''
'''
#以读追加模式打开的文件，既可以读也可以写。
f=open('hello_openfile.txt','r+',encoding='utf-8')
f.seek(1467)
f.write('\n火箭能不能赢球，关键不仅在于灯泡组合的发挥，还在于外线射手群。\n')
print(f.read())
'''
'''
f=open('hello_openfile.txt','r',encoding='utf-8')

#循环读，一行行地
for line in f.readlines():
    print(line)
'''
'''
f=open('hello_openfile.txt','r',encoding='utf-8')

#循环读,跳过第10行不读
for index,line in enumerate(f.readlines()):
    if index==9:
        continue
    print(line)
'''

'''
f=open('hello_openfile.txt','r',encoding='utf-8')

#循环读
for line in f:
    print(line)
'''
#with作用：读写操作完毕后自动关闭；可以同时打开多个文件
with open('hello_openfile.txt.bak','r',encoding='utf-8') as f,\
        open('hello_openfile.txt','r',encoding='utf-8') as f_new:
            for line in f_new:
                print(line)

