#!/usr/bin/env python
#Author:TangHu
import sys
#-*购物车程序*-
'''
需求：
    1.启动程序后，让用户输入自己的工资，然后打印商品列表
    2.允许用户根据商品编号购买商品
    3.用户选择商品后，检测余额是否够，够就直接付款，不够就提醒
    4.可随时退出，退出时打印已购买商品和余额
'''
#构建商品列表 编号、名称、价格
goods={1:("Lenovo",3000),2:("ViewSonic",1000),3:("iphone",5000),4:("huawei",2000),5:("xiaomi",500),6:("vivo",1500)}
#定义一个购物车
shopingCart=[]
#构建系统界面
# 提示用户输入工资，
userMoney = input("请输入您的账户余额：")
if userMoney.isdigit():
    money=int(userMoney)
    while True:
        print("*"*35)
        print(" "*35)
        print(" "*8,"*欢迎进入XXX网上商城*"," "*15)
        print(" "*35)
        print("*"*35)



        #显示商品列表
        print("-"*40)
        print("商品编号      商品名称          商品价格")
        print("-"*40)
        for id in goods:

            print("   %d          %s         %d" %(id,goods[id][0],goods[id][1]))
            print("-"*40)
        #用户根据商品编号购买商品
        idStr=input("请选择你需要购买的商品编号(如需添加多个商品，请以逗号分隔)：")
        idList=idStr.split(",")
        #将用户输入的id列表转换成整型列表
        intList=[]
        for strID in idList:
            intList.append(int(strID))
        #如果用户输入的id在商品列表的id中，就将其加入购物车
        for sid in intList:
            for j in goods:
                if sid==j:
                    shopingCart.append(goods.get(j))

        #检测余额是否够，够就直接付款，不够就提醒
        totalMoney=0
        #求购物车中商品的总和
        for sp in shopingCart:
            totalMoney+=sp[1]

        if money-totalMoney>=0:
            # 显示商品列表
            print("-" * 50)
            print("商品编号      商品名称          商品价格         数量")
            print("-" * 50)

            i=0
            #将列表转换成集合，显示前去掉重复的商品，如果有重复在商品数量上体现
            sc=set(shopingCart)
            for spd in sc:
                print("   %d          %s             %d          %d" % (i, spd[0], spd[1],shopingCart.count(spd)))
                print("-" * 50)
                i+=1
            print("你的账户余额还剩：\033[31;1m%d\033[0m" %(money-totalMoney),"元")
        else:
            print("\033[31;1m您的账户余额已不足！\033[0m")
            break
else:
    print("您输入的工资格式不正确")



