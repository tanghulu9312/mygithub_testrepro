#!/usr/bin/env python
#Author:TangHu
# -*- conding:utf-8 -*-

import subprocess
'''
#执行命令，返回命令执行状态 ， 0 or 非0
res=subprocess.call(['dir'],shell=True)
print(res)
#执行命令，如果命令结果为0，就正常返回，否则抛异常
res1=subprocess.check_call(['dir'],shell=True)
print(res1)
#执行命令，并返回结果，注意是返回结果，不是打印，下例结果返回给res
res2=subprocess.check_output(['dir'],shell=True)
print(res2)

#接收字符串格式命令，返回元组形式，第一个元素是执行状态，第二个是命令结果
res3=subprocess.getstatusoutput('ping www.baidu.com')
print(res3)
'''
#接收字符串格式的命令，并返回结果
res4=subprocess.getoutput('systeminfo')
print(res4)


subprocess.Popen()