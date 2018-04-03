#!/usr/bin/env python
#Author:TangHu

#books.append("oracle从入门到精通")
#books.insert(0,"python系统自动化运维")
#books[1]="java设计模式"
#books.pop()
#del books[2]
#books.remove(books[1])
#print(books.count("Linux基础学习"))
#books.reverse()
#books.sort()
#books.clear()
#books2=[]
#books.extend(books2)
#浅copy
import copy
books=["Linux服务器架设",["Linux基础学习","zabbix监控搭建"],"docker架构"]
books3=books.copy()
print(books)
print(books3)

books[1][0]="ansible权威指南"

print(books)
print(books3)

a=1
b=a
print(a,b)
print(a==b)
print(a is b)
a=2
print(a==b)
print(a is b)
print(a,b)

c="abc"
d=copy.copy(c)
print(c==d)
print(c is d)
print(c,d)

#深拷贝其实就是父类和子类都拷贝，拷贝的是值而不是引用，内存地址不同。
e=[1,[2,3],4]
f=copy.deepcopy(e)
print("e==f?",e==f)
print("e is f",e is f)
print(e)
print(f)
print(id(e))
print(id(f))
e[1][0]=22
print("e==f?",e==f)
print("e is f",e is f)
print(e)
print(f)
print(id(e))
print(id(f))

#复制语句其实就是浅拷贝，实际上就是对象的引用，指向同一个对象；操作的都是同一块内存地址
g=[5,[6,7],8]
h=g
print("g==h?",g==h)
print("g is h",g is h)
print(g)
print(h)
g[1][0]=66
print("g==h?",g==h)
print("g is h",g is h)
print(g)
print(h)
print(id(g))
print(id(h))

#列表切片
names=["zhangsan","lisi",["wangwu","zhaoliu"],"zhouba"]
print(names[:])
print(names[0:-1])
print(names[-3:-1])
