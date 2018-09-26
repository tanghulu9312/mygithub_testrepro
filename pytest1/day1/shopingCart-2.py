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
新需求：
    用户入口：
    1.商品信息存在文件里
    2.已购商品，余额记录
    商家入口：
    2.可以添加商品，修改商品价格
'''




#3.定义一个购物车
shopingCart=[]
newCart=[]
# 2定义一个空列表用于存储分割出来的商品信息




filein=open(r'c:\Python\practice\goods.txt','r')
Lines=filein.readlines()

for line in Lines:
    if line.startswith('g'):
        # 1、从文件中取出商品信息：商品列表 编号、名称、价格
        # 1.1、读出文件
        # 1.2对读出的字符串进行操作
        goods = line[line.index('=') + 1:line.index('\n') - 1].split(';')
        goodsList = []
        for temp in goods:
            # 2.1把分割出来的商品信息加入空列表
            goodsList.append(temp.split(','))

    elif line.startswith('c'):
        #已购商品集合
        complate = line[line.index('=') + 1:line.index('\n') - 1].split(';')
        if complate != ['']:
            for temp in complate:
                # 2.1把分割出来的商品信息加入空列表
                shopingCart.append(temp.split(','))
                print('第一次登录购物车',shopingCart)

    elif line.startswith('i'):
        times=int(line[line.index('=')+1:-2])
        print('这是你第%d次登陆系统！' % (times+1))


        # 判断是否是第一次登录
        if times==0:
            # 如果是第一次登录系统，需要提示用户存钱到账户；后面登录只需要读取存在文件中的余额
            Money=int(input("请存入一定金额的钱到账户，开始输入存入金额："))
            lgood = ''
            for tt1 in goodsList:
                lgood += str(tt1[0]) + ',' + tt1[1] + ',' + str(tt1[2]) + ',' + str(tt1[3]) + ';'
            sgoods = ''
            filetime = open(r'c:\Python\practice\goods.txt', 'w')
            filetime.writelines('goodslist=' + lgood + '\n' +'complatelist='+sgoods+'\n'+ 'i=' + str(times + 1) + ';\n' + 'userMoney=' + str(Money))

            filetime.flush()
            filetime.close()

filein.flush()
filein.close()

fileMon = open(r'c:\Python\practice\goods.txt', 'r')
fileMonLines = fileMon.readlines()
for monLine in fileMonLines:
    if monLine.startswith('u'):
        userMoney = int(monLine[monLine.index('=') + 1:])
        print(userMoney)
        print("你的账户余额为：%d" % userMoney)


while True:
    print("*"*35)
    print(" "*35)
    print(" "*8,"*欢迎进入XXX网上商城*"," "*15)
    print(" "*35)
    print("*"*35)


    fileG= open(r'c:\Python\practice\goods.txt', 'r')
    fileGLines = fileG.readlines()
    goodsList = []

    for GLine in fileGLines:

        if GLine.startswith('g'):
            # 1、从文件中取出商品信息：商品列表 编号、名称、价格
            # 1.1、读出文件
            # 1.2对读出的字符串进行操作
            goods = GLine[monLine.index('=') + 1:GLine.index('\n') - 1].split(';')
            for temp in goods:
                # 2.1把分割出来的商品信息加入空列表
                goodsList.append(temp.split(','))

    print("-" * 60)
    print("商品编号      商品名称          商品价格         商品数量")
    print("-" * 60)

    for goodTemp in goodsList:
        print("   %d          %s         %d           %d" % (
            int(goodTemp[0]), goodTemp[1], int(goodTemp[2]), int(goodTemp[3])))
        print("-" * 60)

    #用户根据商品编号购买商品
    idStr=input("请选择你需要购买的商品编号(如需添加多个商品，请以逗号分隔)：")
    if idStr.lower()=='q':
        lgood = ''
        sgoods = ''

        for tt1 in goodsList:
            lgood += str(tt1[0]) + ',' + tt1[1] + ',' + str(tt1[2]) + ',' + str(
                int(tt1[3]) - newCart.count(tt1)) + ';'
        totalMoney = 0
        for tt2 in shopingCart:
            sgoods += str(tt2[0]) + ',' + tt2[1] + ',' + str(tt2[2]) + ',' + str(newCart.count(tt2)) + ';'
        fileq = open(r'c:\Python\practice\goods.txt', 'w')
        fileq.write('goodslist=' + lgood + '\n' + 'complatelist=' + sgoods + '\n' + 'i=' + str(
            times + 1) + ';\n' + 'userMoney=' + str((userMoney - totalMoney)))
        fileq.flush()
        fileq.close()
        break
    idList=idStr.split(",")
    #将用户输入的id列表转换成整型列表
    intList=[]
    for strID in idList:
        intList.append(int(strID))

    #如果购物车没有任何东西
    tempID={}
    for inputId in intList:
        tempID[inputId] = intList.count(inputId)
    tempSP=[]
    for sp in shopingCart:
        tempSP.append(sp[0])
    def addGoods():
        for tid in tempID.keys():
            for goods in goodsList:
                if tid == int(goods[0]):
                    tempCart1 = []
                    tempCart1.extend(goods)
                    tempCart1[3]=tempID.get(tid)
                    shopingCart.append(tempCart1)


    if shopingCart==[]:
        addGoods()
    else:
        for id in tempID.keys():
            for sp in shopingCart:
                if int(sp[0]) == id:
                    sp[3] = str(int(sp[3]) + tempID.get(id))
                    break
                else:
                    addGoods()





    #
    # if shopingCart==[]:
    #     for inputId in intList:
    #         for goodTemp in goodsList:
    #             if inputId == int(goodTemp[0]):
    #                 tempCart1=[]
    #                 tempCart1.extend(goodTemp)
    #                 tempCart1[3]=1
    #                 shopingCart.append(tempCart1)
    #
    #                 print('this test--->',goodsList)
    #
    # #如果购物车里有商品，那么则判断购物车商品中的商品id是否与用户输入的Id相等，相等则数量+1。不相等就直接加入购物车。
    # else:
    #     #shopingCart != []:
    #     for inputId2 in intList:
    #         for goodTemp2 in shopingCart:
    #             for goodsTemp in goodsList:
    #                 if inputId2 == int(goodTemp2[0]):
    #                     goodTemp2[3]=int(goodTemp2[3])+1
    #                     break
    #
    #                 else:
    #                     if inputId2==int(goodsTemp[0]):
    #                         tempCart3 = []
    #                         tempCart3.extend(goodsTemp)
    #                         tempCart3[3] = 1
    #                         shopingCart.append(tempCart3)
    #
    #             break
    #         break
    #
    #
    #
    #
    #

    # 显示商品列表

    print("-" * 25, "已购商品列表", "-" * 25)
    print("商品编号      商品名称          商品价格         商品数量")
    print("-" * 50)

    totalMoney=0
    for tt in shopingCart:
        totalMoney=totalMoney+int(tt[3])*int(tt[2])
        print("   %d          %s             %d            %d " % (
            int(tt[0]), tt[1], int(tt[2]), int(tt[3])))
        print("-" * 50)

    #检测余额是否够，够就直接付款，不够就提醒
        # 求购物车中商品的总和

    if userMoney-totalMoney>0:
        lgood = ''
        sgoods = ''
        for tt2 in goodsList:
            for tt3 in shopingCart:
                if tt3[0]==tt2[0]:
                    if tt2[3]==100:
                        tt2[3]=int(tt2[3]) - int(tt3[3])
                    else:
                        tt2[3]=100-int(tt3[3])

                sgoods += str(tt3[0]) + ',' + tt3[1] + ',' + str(tt3[2]) + ',' + str(tt3[3]) + ';'
            lgood += str(tt2[0]) + ',' + tt2[1] + ',' + str(tt2[2]) + ',' + str(tt2[3]) + ';'


        if userMoney==2000:
            filein = open(r'c:\Python\practice\goods.txt', 'w')
            filein.write('goodslist='+lgood+'\n'+'complatelist='+sgoods+'\n'+'i='+str(times+1)+';\n'+ 'userMoney='+str((userMoney-totalMoney)))
            print("你的账户余额还剩：\033[31;1m%d\033[0m" % (userMoney - totalMoney), "元")
        else:
            filein = open(r'c:\Python\practice\goods.txt', 'w')
            filein.write('goodslist=' + lgood + '\n' + 'complatelist=' + sgoods + '\n' + 'i=' + str(
                times + 1) + ';\n' + 'userMoney=' + str((20000 - totalMoney)))
            print("你的账户余额还剩：\033[31;1m%d\033[0m" % (20000 - totalMoney), "元")




    else:
        print("\033[31;1m您的账户余额已不足！\033[0m")
        break

    filein.flush()
    filein.close()
    #根据商品ID来，加入购物车1，2，3加入。



