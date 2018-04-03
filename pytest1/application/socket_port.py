#!/usr/bin/env python
#Author:TangHu
#端口扫描器
from __future__ import  print_function
from socket import *
def con_scan(host,port):
    conn=socket(AF_INET,SOCK_STREAM)
    try:
        conn.connect((host,port))
        print(host,port,'is avaliable')
    except Exception as e:
        print(host,port,'is not avaliable')
    finally:
        conn.close()
def main():
    host="192.168.6.124"
    for port in range(70,100):
        con_scan(host,port)
if __name__ == '__main__':
    main()