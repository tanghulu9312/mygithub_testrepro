#!/usr/bin/env python
#Author:TangHu
import shutil
import os
import zipfile,tarfile
#将文件内容拷贝至另一个文件
shutil.copyfileobj(open('os模块.py','r',encoding='utf-8'),open('new.xml','w',encoding='utf-8'))
#拷贝文件
shutil.copyfile('sys模块.py','new2.txt')
#仅拷贝权限。内容，组，用户均不变
shutil.copymode('new.xml','new2.txt')

print(os.path.getmtime(r'D:/tools/PycharmProjects/pytest1/day6/new.xml'))
print(os.path.getmtime(r'D:/tools/PycharmProjects/pytest1/day6/new2.txt'))
#仅拷贝状态信息
shutil.copystat('new.xml','new2.txt')
print(os.path.getmtime(r'D:/tools/PycharmProjects/pytest1/day6/new.xml'))
print(os.path.getmtime(r'D:/tools/PycharmProjects/pytest1/day6/new2.txt'))
#拷贝文件和权限
shutil.copy('time模块.py','new3.txt')
#拷贝文件和状态信息
shutil.copy2('random模块.py','new4.txt')
#递归地拷贝文件
#shutil.copytree('Atm','abc',ignore=shutil.ignore_patterns('*.pyc','tmp*'))
#递归地删除文件
#shutil.rmtree('Python')
#递归地移动文件，它类似mv命令，其实就是重命名
#shutil.move('abc','testshutil')
#创建压缩包并返回文件路径
#shutil.make_archive("shutil_make_archive.zip","zip",r"D:\wordpress")

'''
#压缩
z=zipfile.ZipFile('zip_test.zip','w')
z.write(r'C:\Python')
z.close()
'''
'''
#解压
z=zipfile.ZipFile('zip_test.zip','r')
z.extractall(path='.')
z.close()
'''
'''
#压缩
t=tarfile.open('python.tar','w')
t.add(r'C:\Python\practice',arcname="pytest1.py")
t.add(r'C:\Python\practice',arcname="pytest2.py")
t.close()
'''

#解压缩
t=tarfile.open(r'D:\tools\PycharmProjects\pytest1\day6\python.tar','r')
t.extractall(r"d:/tools")
t.close()