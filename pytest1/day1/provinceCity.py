#!/usr/bin/env python
#Author:TangHu
#创建一个字典用于存储数据
data={
    "湖南省":{
        "长沙市":{
            "芙蓉区":["杨家山","袁家岭","火车站"],
            "雨花区":["高桥大市场","东塘","雨花亭"],
            "天心区":["黄兴广场","省政府","植物园"],
        },
        "株洲市":{
                    "天元区":["湖南工大","山塘冲","谭家塘"],
                    "荷塘区":["富家坡","株洲站","荷塘铺"],
                    "芦淞区":["沙塘湾","岳山冲","火车南站"],
                },
        "湘潭市": {
            "雨湖区": ["湘潭大学", "湖南科大", "湘潭站"],
            "岳塘区": ["菊花塘", "市政府", "双马镇"],

        },
        "衡阳市": {
            "蒸湘区": ["汽车站", "市政府", "银光社区"],
            "珠晖区": ["衡阳站", "回雁峰", "万达广场"],
            "石鼓区": ["华耀城", "帝景山庄", "虎形山"],
        }
    },
    "湖北省":{
            "武汉市":{
                "江岸区":["三阳广场","中医医院","市政府"],
                "汉阳区":["动物园","七里庙","墨水湖"],
                "武昌区":["丁字桥","景洪花园","江弘新村"],
            },
            "宜昌市":{
                        "伍家岗区":["宜昌东站","三峡物流园","宝塔河"],
                        "夷陵区":["晓溪塔森林公园","中华鲟园","客运站"],
                        "西陵区":["长途汽车站","时代购物广场","市政府"],
                    },

        },
    "江西省": {
        "南昌市": {
            "西湖区": ["洪城大市场", "南昌动物园", "象湖湿地公园"],
            "东湖区": ["八一广场", "滕王阁", "系马桩"],
            "青山湖区": ["艾溪湖森林公园", "天香园", "瑶湖郊野森林公园"],
        },
        "漳州市": {
            "赣县区": ["赣州东站", "梅林湿地公园", "赣州农校"],
            "南康区": ["东山公园", "丫丫服装厂", "南康中学"],
            "章贡区": ["中央公园", "樱花公园", "赣州站"],
        },

    }

}


while True:
    # 用户进入系统之后，可以看到所有一级菜单
    print("\033[31;1m===>进入一级菜单\033[1m")
    for first in data:
        print(first)
    #让用户选择
    user_chioce=input("请输入你的选择(按q退出系统)：")
    # 根据用户的选择展示不同的内容
    if user_chioce in data.keys():
        while True:
            print("\033[31;1m===>进入二级菜单\033[1m")
            for second in data[user_chioce]:
                print(second)
            print("-"*20)
            user_chioce2 = input("输入你想进入的下一级\033[31;1m'菜单名'\033[1m，或者按\033[31;1m'q'\033[1m返回上一级菜单：")
            if user_chioce2 in data[user_chioce].keys():
                while True:
                    print("\033[31;1m===>进入三级菜单\033[1m")
                    for three in data[user_chioce][user_chioce2]:
                        print(three)
                    print("-" * 20)
                    user_chioce3 = input("输入你想进入的下一级\033[31;1m'菜单名'\033[1m，或者按\033[31;1m'q'\033[1m返回上一级菜单：")
                    if user_chioce3 in data[user_chioce][user_chioce2].keys():
                        while True:
                            print("\033[31;1m===>进入四级菜单\033[1m")
                            for four in data[user_chioce][user_chioce2][user_chioce3]:
                                print(four)
                            print("-" * 20)
                            user_chioce4 = input("按\033[31;1m'q'\033[1m返回上一级菜单：")
                            if user_chioce4.lower() == 'q':
                                break
                            else:
                                print("***你的输入有误，请重新输入！***")
                                continue
                    elif user_chioce3.lower()=='q':
                        break
                    else:
                        print("***你的输入有误，请重新输入！***")
                        continue
            elif user_chioce2.lower()=='q':
                break
            else:
                print("***你的输入有误，请重新输入！***")
                continue
    elif user_chioce.lower()=='q':
        break
    else:
        print("***你输入的菜单名不存在，请重新输入！***")
        continue

