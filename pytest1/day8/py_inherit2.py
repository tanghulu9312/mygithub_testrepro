#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:py_inherit2.py.py
@time:2018-07-31-21-56
'''
class School(object):

    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.teachers=[]
        self.students=[]
    #学生注册
    def register(self,stu_obj):
        self.students.append(stu_obj.name)
        print("%s 来学校报到注册！" %stu_obj.name)

    #老师注册
    def staff_status(self,teacher_obj):
        self.teachers.append(teacher_obj.name)
        print("%s 老师入职！" %teacher_obj.name)
    #学生交学费
    def tuiration(self):
        for student in self.students:
            print("%s交学费了。。。" %student)
class SchoolMember(object):
    def __init__(self,name,age,addr,sex):
        self.name=name
        self.age=age
        self.addr=addr
        self.sex=sex
    def info(self):
        pass


class Teacher(SchoolMember):
    def __init__(self,name,age,addr,sex,salary):
        super(Teacher,self).__init__(name,age,addr,sex)
        self.salary=salary
    def info(self):
        print(
            """%s:老师信息
            name:%s
            age:%s
            addr:%s
            sex:%s
            salary:%f
            """ %(self.name,self.name,self.age,self.addr,self.sex,self.salary)
        )
class Student(SchoolMember):
    def __init__(self,name,age,addr,sex,grade):
        super(Student,self).__init__(name,age,addr,sex)
        self.grade=grade
    def info(self):
        print(
            """%s:学生信息
            name:%s
            age:%s
            addr:%s
            sex:%s
            grade:%s
            """ %(self.name,self.name,self.age,self.addr,self.sex,self.grade)
        )

t=Teacher("Alex","45","changsha","M",5690)
t.info()
s1=Student("zhangsan","23","changsha","F","Python开发班")
s2=Student("lisi","21","changsha","M","Linux运维")
s1.info()
sm=School("OldBoy","beijin")
sm.register(s1)
sm.register(s2)
sm.tuiration()
sm.staff_status(t)