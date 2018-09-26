#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:findSmallest.py
@time:2018/07/24/14/06
'''
'''
list=[2,1,5,3,4,98,6]

#选择排序
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

temp=selectionSort(list)
print(temp)


#递归
def countdown(i):
    if i>0:
        print(i)
        countdown(i-1)
    else:
        exit()
countdown(100)

def sum(arr):
    total=0
    for x in arr:
        total+=x
    return total
tt=sum([1,2,3,4])
print(tt)

#数组求和
def sum_arr(arr):
    if arr==[]:
        return 0
    return arr[0]+sum(arr[1:])
list=[1,2,3,4,5]
tt1=sum_arr(list)
print(tt1)
print(list[1:])

#编写一个递归函数来计算列表包含的元素数
def sum_num(arr):
    if arr==[]:
        return 0
    return 1+sum_num(arr[1:])
nu=sum_num(list)
print(nu)
'''
'''
#找出列表中最大的数字
list=[1,6,3,4,5]
def findBigNum(arr):
    if len(arr)==2:
        return arr[0] if arr[0]>arr[1] else arr[1]
    bigSum=findBigNum(arr[1:])
    return arr[0] if arr[0]>bigSum else bigSum
bb=findBigNum(list)
print(bb)

'''
list=[5,12,9,1,3,4]
'''
def findBigNum(arr):

    if len(arr)==2:
        if arr[0] > arr[1]:
            return arr[0]
        else:

            return arr[1]

    else:

        bigNum=findBigNum(arr[1:])


    if arr[0] > bigNum:
        return arr[0]
    else:
        return bigNum
bb=findBigNum(list)
print(bb)
'''
#快速排序
def quicksort(array):

    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less =[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i > pivot ]
        return quicksort(less)+[pivot]+quicksort(greater)
qq=quicksort(list)
print(qq)