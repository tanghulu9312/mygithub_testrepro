#!/usr/bin/env python
#Author:TangHu
import sys
import os
#import login
#print(sys.path)
#print(sys.argv)

#cmd_rs=os.system("dir")
#cmd_rs=os.mkdir("new_dir")
#print(cmd_rs)
msg="你好，世界！"
bmsg=msg.encode("utf-8")
print(bmsg)
dmsg=bmsg.decode()
print(dmsg)

