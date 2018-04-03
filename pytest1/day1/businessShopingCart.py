#!/usr/bin/env python
#Author:TangHu
#1、从文件中取出商品信息：商品列表 编号、名称、价格
#1.1、读出文件
infile=open(r'c:\Python\practice\goods.txt','r')
srcLines=infile.readlines()
#1.2对读出的字符串进行操作
#2定义一个空列表用于存储分割出来的商品信息

goodsList=[]
lgood=''

for line in srcLines:

    if line.startswith('i'):
        times=int(line[line.index('=')+1:-2])


    elif line.startswith('g'):
        goods = line[line.index('=') + 1:line.index('\n') - 1].split(';')
        for temp in goods:
            # 2.1把分割出来的商品信息加入空列表
            goodsList.append(temp.split(','))
    else:
        userMoney = int(line[line.index('=') + 1:])


infile.flush()
infile.close()


# 3.构建系统界面

while True:
    print("*"*45)
    print(" "*35)
    print(" "*8,"*欢迎进入XXX网上商城后台管理系统*")
    print(" "*35)
    print("*"*45)

    #显示商品列表
    print("-"*60)
    print("商品编号      商品名称          商品价格         商品数量")
    print("-"*60)
    for goodTemp in goodsList:

        print("   %d          %s         %d           %d" %(int(goodTemp[0]),goodTemp[1],int(goodTemp[2]),int(goodTemp[3])))
        print("-"*60)
    # 给出选项
    print("===>1.修改商品")
    print("===>2.添加商品")
    print("===>3.删除商品")
    print("===>4.退出系统")
    #提示用户选择
    user_choice=input("请输入你的选择：")
    if user_choice.isdigit():
        lgood=''
        goods=[]
        if user_choice=='1':

            #根据用户输入的商品编号对商品进行修改
            userInputId=input("请输入你要修改的商品编号：")
            if userInputId.isdigit():
                for goodTemp2 in goodsList:
                    if userInputId==goodTemp2[0]:
                        #给出修改的商品属性选项
                        print("1.修改商品名称")
                        print("2.修改商品价格")
                        print("3.修改商品数量")
                        user_choice2 = input("请输入你的选择：")
                        if user_choice2 == '1':
                            goods_name=input("请输入商品的名称：")
                            goodTemp2[1]=goods_name
                        if user_choice2 == '2':
                            goods_price=input("请输入商品的价格：")
                            goodTemp2[2]=goods_price
                        if user_choice2 == '3':
                            goods_count=input("请输入商品的数量：")
                            goodTemp2[3]=goods_count
                        else:
                            print("非法输入！重新操作！")
                            continue
                for tt1 in goodsList:
                    lgood += str(tt1[0]) + ',' + tt1[1] + ',' + str(tt1[2]) + ',' + str(tt1[3]) + ';'
                filein = open(r'c:\Python\practice\goods.txt', 'w')
                filein.write('goodslist=' + lgood + '\n' + 'i=' + str(times + 1) + ';\n' + 'userMoney=' + str(userMoney))
                filein.flush()
            else:
                print("非法输入，请重新操作！")
                continue
        elif user_choice=='2':
            # 根据用户输入的商品编号对商品进行添加
            InputGoodsId = input("请输入你要添加的商品编号（不能与列表中的商品编号相同）：")
            #判断列表中是否有此商品编号
            if InputGoodsId.isdigit():
                for goodTemp2 in goodsList:
                    if InputGoodsId not in goodTemp2:
                        InputGoodsName = input("请输入你要添加的商品名称：")
                        InputGoodsPrice = input("请输入你要添加的商品价格：")
                        InputGoodsNum = input("请输入你要添加的商品数量：")
                        goods.append(InputGoodsId)
                        goods.append(InputGoodsName)
                        goods.append(InputGoodsPrice)
                        goods.append(InputGoodsNum)
                        goodsList.append(goods)
                        for tt1 in goodsList:
                            lgood += str(tt1[0]) + ',' + tt1[1] + ',' + str(tt1[2]) + ',' + str(tt1[3]) + ';'
                        filein = open(r'c:\Python\practice\goods.txt', 'w')
                        filein.write('goodslist=' + lgood + '\n' + 'i=' + str(times + 1) + ';\n' + 'userMoney=' + str(userMoney))
                        filein.flush()
                    else:
                        print("你输入的商品编号已经存在，请重新输入！")
                        break
            else:
                print("非法输入，请重新操作！")
                continue
        elif user_choice=='3':
            # 根据用户输入的商品编号对商品进行修改
            userInputId = input("请输入你要删除的商品编号：")
            if userInputId.isdigit():
                for goodTemp3 in goodsList:
                    if userInputId == goodTemp3[0]:
                        goodsList.remove(goodTemp3)
                for tt1 in goodsList:
                    lgood += str(tt1[0]) + ',' + tt1[1] + ',' + str(tt1[2]) + ',' + str(tt1[3]) + ';'
                filein = open(r'c:\Python\practice\goods.txt', 'w')
                filein.write('goodslist=' + lgood + '\n' + 'i=' + str(times + 1) + ';\n' + 'userMoney=' + str(userMoney))
                filein.flush()
            else:
                print("非法输入，请重新操作！")
                continue
        elif user_choice=='4':
            break
    else:
        print("非法输入，请重新操作！")
        continue
    filein.flush()
    filein.close()