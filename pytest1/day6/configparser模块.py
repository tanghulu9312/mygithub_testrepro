#!/usr/bin/env python
#Author:TangHu

import configparser
config=configparser.ConfigParser()
config.read('my.ini',encoding="utf-8")

'''
#查看所有的标题
res=config.sections()
print(res)

#查看标题client下所有key=value的key
options=config.options('client')
print(options)

#查看标题mysql下所有key=value的（key,value）格式
item_list=config.items('mysql')
print(item_list)

#查看标题mysqld下port的值====>字符串格式
value=config.get("mysqld",'port')
print(value,type(value))

#查看标题mysqld下port的值====>整数格式
value2=config.getint("mysqld",'port')
print(value,type(value2))

#查看标题mysqld下default-engine的值====>布尔类型格式
value3=config.getboolean("mysqld","default-engine")
print(value3)

#查看标题mysqld下sync_master_info的值====>浮点数格式
value4=config.getfloat("mysqld","sync_master_info")
print(value4)
'''

#删除整个标题mysql
config.remove_section("mysql")

#删除标题下的某个k1和k2
config.remove_option("mysqld","datadir")
'''
#判断是否存在某个标题
print(config.has_section("mysql"))
#判断某个标题是否存在datadir
print(config.has_option("mysqld","datadir"))
'''
#添加一个标题
config.add_section("test_config")
#在标题test_config下添加name='egon',age=18
config.set("test_config","name","egon")
config.set("test_config","age",str(20))
#最后将修改的内容写入文件，完成最终的修改
config.write(open('test_config.ini','w'))