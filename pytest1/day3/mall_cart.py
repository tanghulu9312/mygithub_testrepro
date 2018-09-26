#!/usr/bin/env python
#Author:TangHu
#-*购物车程序*-
'''
需求：
    1.启动程序后，让用户输入自己的工资，然后打印商品列表
    2.允许用户根据商品编号购买商品
    3.用户选择商品后，检测余额是否够，够就直接付款，不够就提醒
    4.可随时退出，退出时打印已购买商品和余额

    用户入口：
    1.商品信息存在文件里
    2.已购商品，余额记录
    商家入口：
    2.可以添加商品，修改商品价格
'''

#打开登录次数文件
def openTimeFile():
    file=open(r'c:\Python\practice\times.txt','r')
    return file

#打开存款文件
def openMoneyFile():
    file = open(r'c:\Python\practice\money.txt', 'r')
    return file

#打开商品列表文件并展示商品列表
def showGoods():
    # 定义一个空列表用于存储分割出来的商品信息
    goodsList=[]

    fileGoods=open(r'c:\Python\practice\goodsList.txt', 'r')

    for line in fileGoods.readline():
        goods = line[line.index('=') + 1:line.index('\n') - 1].split(';')
        for temp in goods:
            # 把分割出来的商品信息加入空列表
            goodsList.append(temp.split(','))

    print("-" * 60)
    print("商品编号      商品名称          商品价格         商品数量")
    print("-" * 60)

    for goodTemp in goodsList:
        print("   %d          %s         %d           %d" % (
                int(goodTemp[0]), goodTemp[1], int(goodTemp[2]), int(goodTemp[3]))
              )
        print("-" * 60)
    fileGoods.flush()
    fileGoods.close()

#如果购物车有商品则显示购物车列表
# 已购商品集合
def showCart():

    # 定义一个购物车列表
    shopingCart = []
    fileCart=open('C:\Python\practice\cart.txt','r')
    cartSrt=fileCart.read()
    cart = cartSrt[cartSrt.index('=') + 1:cartSrt.index('\n') - 1].split(';')
    if cart != ['']:
         for temp in cart:
            # 2.1把分割出来的商品信息加入空列表
            shopingCart.append(temp.split(','))
         print("-" * 25, "已购商品列表", "-" * 25)
         print("商品编号      商品名称          商品价格         商品数量")
         print("-" * 50)
         totalMoney=0
         for tt in shopingCart:
             totalMoney = totalMoney + int(tt[3]) * int(tt[2])
             print("   %d          %s             %d            %d " % (
                 int(tt[0]), tt[1], int(tt[2]), int(tt[3])))
             print("-" * 50)
    # 用户根据商品编号购买商品
    idStr = input("请选择你需要购买的商品编号(如需添加多个商品，请以逗号分隔)：")




#打开购物车文件
def openCartFile():
    file=open('C:\Python\practice\cart.txt','r')
    return file



#判断用户是否是第一次登录
def isFirstLogin():
    #从文件中获取登录次数
    fileTime=openTimeFile()
    for line in fileTime.readline():
        times = int(line[line.index('=') + 1:-2])
        print('这是你第%d次登陆系统！' % (times + 1))

        # 判断是否是第一次登录
        if times == 0:
            # 如果是第一次登录系统，需要提示用户存钱到账户；后面登录只需要读取存在文件中的余额
            Money = int(input("请存入一定金额的钱到账户，开始输入存入金额："))
            fileMoney=openMoneyFile()
            fileMoney.writelines('Money+=',str(Money))
        #如果不是第一次登录，则打印商品列表并判断购物车有无商品，如果购物车有商品则显示购物车列表
        showGoods()

