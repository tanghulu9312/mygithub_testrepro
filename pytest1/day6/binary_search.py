#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:binary_search.py
@time:2018/07/24/09/53
'''

def binary_search(num,list_num):
    '''

    :param num:需要查找的数字
    :param list_num: 查找的列表
    :return:
    '''
    low=0
    high=len(list_num)-1
    while low<=high:
        #查找列表中间的那个数字的位置
        # 如果mid为浮点数，则向下取整
        mid=int((low+high)/2)
        guess=list_num[mid]

        if num==guess:
            return mid
        elif num>guess:
            low=guess+1
        else:
            high=guess-1
test_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

print(binary_search(7,test_list))