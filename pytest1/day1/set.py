#!/usr/bin/env python
#Author:TangHu
#去重
list_1=[1,2,3,4,4,5,6,5]
list_1=set(list_1)
print(list_1)

#交集
list_2=set([1,2,3,4])
list_3=set([1,3,5,7,9])
print(list_2.intersection(list_3))
print('list_2和list_3的交集',list_2 & list_3)
#并集
print(list_2.union(list_3))
print('list_2和list_3的并集',list_2 | list_3)
#差集
print(list_2.difference(list_3))
print('list_2和list_3的差集',list_2 - list_3)
#子集
list_4=set([1,5,7])
print(list_4.issubset(list_3))
print(list_3.issuperset(list_4))

#对称差集
print(list_2.symmetric_difference(list_3))
print('list_2和list_3的对称差集',list_2 ^ list_3)

#增加
list_2.add(99)
print(list_2)
#删除
list_2.remove(1)

print(list_2)
#判断元素是否在里面
print(99 in list_2)
#复制
list_5=list_2.copy()
print(list_5)
#删除 对比
list_5.pop()
#list_5.remove('a') #删除不存在的元素会报错
list_5.discard('a') #删除不存在的元素不会报错
#print(list_2.clear()) #删除所有元素
list_6=set([10,11,12,14])
list_7=set([10,9,8,6])

#移除交集
#list_6.difference_update(list_7)

print(list_6.intersection(list_7))
#移除无交集部分
#list_6.intersection_update(list_7)
print(list_6)
#判断两个集合是否有交集
print(list_6.isdisjoint(list_7)) #有交集返回false
print(list_6.isdisjoint(list_2)) #无交集返回True

#求对称差集
list_6.symmetric_difference_update(list_7)
print(list_6)