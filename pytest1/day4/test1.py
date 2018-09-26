#!/usr/bin/env python
#Author:TangHu
from __future__  import print_function
import sys
import os
import fileinput
'''
#sys.argv是一个报存命令行参数的普通列表。
print(sys.argv)
'''

'''
def main():
    sys.argv.append(" ")
    #从命令行参数中获取文件名称，
    filename=sys.argv[1]
    #然后判断文件是否存在，如果文件不存在，则提示用户该文件不存在
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists ')
    elif not os.access(filename,os.R_OK):
        raise SystemExit(filename + ' is not accessible ')
    else:
        print(filename + ' is accessible ')
if __name__ == '__main__':
    main()
'''

'''
#读取标准输入
for line in sys.stdin:
    print(line,end=" ")
'''

'''
#fileinput 读取内容比sys.stdin更加灵活。
# fileinput既可以从标准输入中读取数据，也可以从文件中读取数据。
for line in fileinput.input():
    meta=[fileinput.filename(),fileinput.fileno(),fileinput.filelineno(),fileinput.isfirstline(),fileinput.isstdin()]
    print(*meta,end=" ")
    print(line,end=" ")

'''

#使用systemExit异常打印错误消息
sys.stdout.write('hello')
sys.stdout.write('world')