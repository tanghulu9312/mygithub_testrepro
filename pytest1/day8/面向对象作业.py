#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:面向对象作业.py
@time:2018-08-01-11-07
'''
import pickle
'''
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里
'''
#学校类
class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.courses=Courses




#学校成员类
class SchoolMember(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
#管理员类
class Administrator(SchoolMember):
    def __init__(self,name,age):
        super(Administrator,self).__init__(name,age)
        self.school=School
        self.teacher=Teacher
        self.student=Student
        self.classes=Classes
        self.courses=Courses

    def create_school(self):
        school=self.school
        school.name=input("请输入学校名称：")
        school.addr=input("请输入学校地址：")
        school.course=self.create_coures()

        f=open("school.txt","ab")
        school_data=pickle.dumps(school)
        f.write(school_data)
        f.close()
        return school

    def create_teacher(self):
        teacher=self.teacher
        teacher.name = input("请输入老师的姓名：")
        f = open("teacher.txt", 'ab')
        teacher_date = pickle.dumps(teacher)
        f.write(teacher_date)
        f.close()
        return teacher


    def create_classes(self):
        classes=self.classes
        classes.name = input("请输入班级的名称：")
        classes.semester = input("请输入班级的学期：")
        classes.startTime = input("请输入班级开课的时间：")

        f = open("classes.txt", 'ab')
        classes_date = pickle.dumps(classes)
        f.write(classes_date)
        f.close()
        return classes
    def create_coures(self):
        courses= self.courses
        courses.name = input("请输入课程的名称：")
        courses.period = input("请输入课程周期：")
        courses.price = input("请输入课程价格：")
        f = open("courses.txt", "ab")
        courses_data = pickle.dumps(courses)
        f.write(courses_data)
        f.close()
        return courses

#学生类
class Student(SchoolMember):
    def __init__(self, name, age,is_tuirition):
        super(Student,self).__init__(name, age)
        self.classes=Classes
        self.is_tuirition=is_tuirition
#老师类
class Teacher(SchoolMember):
    def __init__(self,name):
        super(Teacher,self).__init__(name)
#班级类
class Classes(object):
    def __init__(self,name,semester,startTime):
        self.name=name
        self.semester=semester
        self.startTime=startTime
        self.courses=Courses
        self.teacher=Teacher
        self.classesRecord=ClassesRecord

#课程类
class Courses(object):
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
#课程记录类
class ClassesRecord(object):
    def __init__(self,node,teachTime):
        self.classes=Classes
        self.node=node
        self.teachTime=teachTime
        self.studyRecord=StudyRecord
#学习记录类
class StudyRecord(object):
    def __init__(self,status,statusTime,grade):
        self.classesRecord=ClassesRecord
        self.status=status
        self.statusTime=statusTime
        self.grade=grade
        self.student=Student


'''
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程

'''
admin=Administrator("老王",22)

#管理员创建讲师、学院、班级

def create():
    school=admin.create_school()

    teacher=admin.create_teacher()

    classes=admin.create_classes()

    f=open("school.txt","rb")
    school_info=pickle.loads(f.read())
    f.close()
    print(school_info.name,school_info.addr,school_info.course.name,)
'''
学员视图， 可以注册， 交学费， 选择班级，
'''
def register():
    student_name=input("请输入学生名称：")
    student_age=input("请输入学生年龄：")

    f=open("classes.txt","rb")
    classes_data=pickle.loads(f.read())
    f.close()
    f=open("courses.txt","rb")
    courses_info=pickle.loads(f.read())
    print(courses_info)
    tuirition=input("请输入您的缴费金额（%s）：" %courses_info.price)
    if tuirition==courses_info.price:

        student=Student(student_name,student_age,"已缴费")
        student.classes=classes_data
        f=open("student.txt","ab")
        student_data=pickle.dumps(student)
        f.write(student_data)
        print("恭喜您注册成功！")
def show_studentInfo():
    f=open("student.txt","rb")
    student_info=pickle.loads(f.read())
    print(""" %s:学生注册信息
            姓名：%s
            年龄：%s
            班级：%s
            缴费情况：%s
    
    """ %(student_info.name,student_info.name,student_info.age,student_info.classes,student_info.is_tuirition))

create()
#register()
#show_studentInfo()
