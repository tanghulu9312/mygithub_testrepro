#!/usr/bin/env python
#Author:TangHu
import os
import time
import sys
print(os.getcwd())  #返回当前工作目录，即当前Python脚本工作的目录路径
os.chdir(r"D:\tools\PycharmProjects")   #改变当前脚本工作目录，相当于shell下的cd
print(os.getcwd())

print(os.curdir)    #返回当前目录：（.）

print(os.pardir)    #获取当前目录的父目录字符串名：（‘..’）

#os.makedirs('ostest/os_test')  #可生成多层递归目录

#os.rmdir('ostest') #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中的rmdir dirname
print(os.listdir(r'd:/tools'))  #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

print(os.stat(r'd:/tools/putty'))   #获取文件或目录信息

print(os.sep)  #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

print(os.linesep) #输出当前平台使用的行终止符，win下为“\t\n",Linux下为“/”

print(os.pathsep)   #输出用于分割文件路径的字符串 win下为；Linux下为：

print(os.name)  #输出字符串指示当前使用平台。win--->'nt'  Linux--->'posix'

#print(os.system("bash command"))    #运行shell命令，直接显示

print(os.environ)   #获取系统环境变量

print(os.path.abspath('.')) #返回path规范化的绝对路径

print(os.path.split(r'D:\tools\PycharmProjects\pytest1\day6')) #将path分割成目录和文件名二元数组返回

print(os.path.dirname(r'D:\tools\PycharmProjects\pytest1\day6'))    #返回path的目录。

print(os.path.basename(r'D:\tools\PycharmProjects\pytest1\day6'))   #返回path后的文件名

print(os.path.exists(r'D:\tools\PycharmProjects\pytest1\day6')) #如果path存在，返回True,否则返回False

print(os.path.isabs(r'D:\tools\PycharmProjects\pytest1\day6'))  #如果path是绝对路径返回True，否则返回false

print(os.path.isfile(r'D:\tools\PycharmProjects\pytest1\day6\os模块.py'))     #如果path是一个存在的文件则返回True

print(os.path.isdir(r'D:\tools\PycharmProjects\pytest1\day6'))  #如果path是一个存在的目录，则返回True

print(os.path.join(r'D:\tools\PycharmProjects\pytest2','day7')) #将多个路径组合后返回

print(os.path.getatime(r'D:\tools\PycharmProjects\pytest1\day6\time模块.py'))     #返回path所指向的文件或者目录的最后存取时间

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getatime(r'D:\tools\PycharmProjects\pytest1\day6\time模块.py'))))

print(os.path.getmtime(r'D:\tools\PycharmProjects\pytest1\day6\random模块.py'))   #返回path所指向的文件或者目录的最后修改时间

print(os.path.getsize(r'D:\tools\PycharmProjects')) #返回path的大小
#在Linux和Mac平台上，该函数(os.path.normcase)会原样返回path，
# 在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
print(os.path.normcase('c:/Users\\System32'))

a='/Users/tanghulu/ostest/\\a1\\\\a2\\\ostest.py'
print(os.path.normpath(a))  #规范化路径，如..和/

'''
#os路径处理
possible_topdir=os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir,
    os.pardir
))
sys.path.insert(0,possible_topdir)
'''