#!/usr/bin/env python
#Author:TangHu

import random
#方法一：生成一个4位数的中英文混合随机数
def v_code1():
    strNum=" "
    for i in range(4):

        currentNum=random.randrange(0,9)

        if i==currentNum:
            tmp=chr(random.randint(65,90))
        else:
            tmp=random.randrange(0,9)
        strNum+=str(tmp)
    print("方法一生成的验证码是：",strNum)
v_code1()
#方法二：生成验证码
def v_code2():
    code=""
    for m in range(5):
        #生成一个随机数字
        num=random.randint(0,9)
        charStr=chr(random.randint(65,90))
        item=random.choice([num,charStr])
        code+=str(item)
    print("方法二生成的验证码是：",code)

v_code2()







print(random.random()) #(0,1)  ----float 大于0且小于1之间的小数

print(random.randint(1,9)) #[1,9]   大于等于1且小于等于9之间的数

print(random.randrange(1,9))    #[1,9)  大于等于1且小于9之间的数

print(random.choice([1,3,5,7,9]))   #固定的列表中选取一个元素

print(random.sample([1,3,4,5,6,7,[2,3,4]],3))   #列表中任意三个元素组成一个新的列表

print(random.uniform(1,9)) #大于1小于9的小数

temp=[1,2,3,4,5,6]
random.shuffle(temp)    #断乱temp的顺序，相当于洗牌。
print(temp)