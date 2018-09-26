#!/usr/bin/env python
#Author:TangHu
import logging
'''
logging.warning("密码错误超过三次，请明天再登录！")
logging.critical("操作频繁，请十分钟后再操作")
logging.debug("此处明显错误，请仔细检查")
logging.info("这是一条提示信息")
logging.error("致命错误！！")

'''

# logging.basicConfig(filename='example.log',format='%(name)s%(thread)s%(asctime)s%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning("开始记录日志文件了")

logger=logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

print(ch)
print(logger)
#
# fh = logging.FileHandler("example.log")
# fh.setLevel(logging.WARNING)
# formatter=logging.Formatter('%(name)s%(thread)s%(asctime)s%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
