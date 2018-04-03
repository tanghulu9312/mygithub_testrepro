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
                newCart.append(temp.split(','))

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
                int(tt1[3]) - shopingCart.count(tt1)) + ';'
        totalMoney = 0
        for tt2 in newCart:
            sgoods += str(tt2[0]) + ',' + tt2[1] + ',' + str(tt2[2]) + ',' + str(shopingCart.count(tt2)) + ';'
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

    #如果是第一次登录，购物车没有任何东西，
    # 将用户输入的商品id跟商品id对比，如果相等，再判断跟购物车就加入购物车。
    #统计购物车商品数量？商品id,在加入购物车之前，判断id是否和购物车中的商品相等
    #相等，商品数量+1，不相等，直接加入购物车，数量为1
##如果是 第二次登录，  将用户输入的商品id跟商品id对比，如果相等，再判断跟购物车中的id是否相等，如果相等则购物车中的数量加一


    totalMoney=0
    #shopingCart = []
    for sid in intList:
        for goodTemp in goodsList:
            # 如果用户输入的id在商品列表的id中，就将其加入购物车
            if sid==int(goodTemp[0]) :

                #显示已购商品列表

                shopingCart.append(goodTemp)

                # for spc in shopingCart:
                #     if spc not in newCart:
                #         newCart.append(spc)
                if newCart==[]:
                    newCart.append(goodTemp)

                    newCart[newCart.index(goodTemp)][3] = 1

                else:
                    for spc in newCart:

                        if int(spc[0])==sid:
                            spc[3]=int(spc[3])+1
                            continue
                        else:
                            newCart.append(goodTemp)
                            newCart[newCart.index(goodTemp)][3] = 1

    print(shopingCart)
    # 显示商品列表

    print("-" * 25, "已购商品列表", "-" * 25)
    print("商品编号      商品名称          商品价格         商品数量")
    print("-" * 50)
    # for tt1 in shopingCart:
    #     totalMoney +=int(tt1[2])

    for tt in newCart:

        print("   %d          %s             %d            %d " % (
            int(tt[0]), tt[1], int(tt[2]), int(tt[3])))
        print("-" * 50)

    #检测余额是否够，够就直接付款，不够就提醒
        # 求购物车中商品的总和

    if userMoney-totalMoney>0:
        lgood = ''
        sgoods = ''

        for tt2 in goodsList:
            for tt3 in newCart:
                if tt2[0]==tt3[0]:
                    lgood += str(tt2[0]) + ',' + tt2[1] + ',' + str(tt2[2]) + ',' + str(int(tt2[3])-tt3[3]) + ';'

                totalMoney += int(tt3[2])*int(tt3[3])
                sgoods+=str(tt3[0]) + ',' + tt3[1] + ',' + str(tt3[2]) + ',' + str(tt3[3]) + ';'
        filein = open(r'c:\Python\practice\goods.txt', 'w')
        filein.write('goodslist='+lgood+'\n'+'complatelist='+sgoods+'\n'+'i='+str(times+1)+';\n'+ 'userMoney='+str((userMoney-totalMoney)))
        filein.flush()
        filein.close()

        print("你的账户余额还剩：\033[31;1m%d\033[0m" %(userMoney-totalMoney),"元")
    else:
        print("\033[31;1m您的账户余额已不足！\033[0m")
        break






