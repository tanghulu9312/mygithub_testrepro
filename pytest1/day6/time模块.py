#!/usr/bin/env python
#Author:TangHu
import time
'''
在Python中，通常有这几种方式来表示时间：
1、时间戳(timestamp)：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
我们运行“type(time.time())”，返回的是float类型
2、格式化的时间字符串(Format String)
3、结构化的时间(struct_time)：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一周中的第几天，一年中第几天，夏令时)
'''
print(time.time())  #时间戳

print(time.strftime("%Y-%m-%d %H:%M:%S")) #当前时间的格式化时间字符串

print(time.localtime())     #本地时区的struct_time

print(time.gmtime())        #UTC时区的struct_time

#格式化的字符串时间<-----（转换）---->结构化的时间<------（转换）----->时间戳

print(time.strptime("2018-07-13 14:02:07","%Y-%m-%d %H:%M:%S")) #格式化的字符串时间-----（转换）---->结构化的时间

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  #结构化的时间--（转换）--->格式化的字符串时间

print(time.localtime(1531462577.690112))    #时间戳转换成本地结构化的时间
print(time.gmtime(1531462577.690112))       #时间戳转换成夏令时的结构化时间

print(time.mktime(time.strptime("2018-07-13 14:02:07","%Y-%m-%d %H:%M:%S")))    #结构化时间转换成时间戳

print((1531461727/3600/24/365)+1970)
# asctime([t]) : 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。
print(time.asctime(time.localtime()))
# ctime([secs]) : 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为
# None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))
print(time.ctime(time.time()))