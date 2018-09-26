#!/usr/bin/env python
#Author:TangHu

'''
import sys
#print(sys.argv) #命令行参数List,第一个元素是程序本身路径

print(sys.version)  #获取Python解释程序的版本信息

print(sys.maxsize)

print(sys.path) # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

print(sys.platform) #返回操作系统平台名称


#进度条练习
'''
import sys,time

for i in range(50):

    #\r默认表示将输出的内容返回到第一个指针，这样的话，后面的内容会覆盖前面的内容
    sys.stdout.write('%s\r' %('#'*i))
    sys.stdout.flush()
    time.sleep(0.1)