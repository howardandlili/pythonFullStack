#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

set = False    # 设置set 当输入为q就可以退出

list = [    # 购物清单
    ["iphone",5800],
    ["bike",800],
    ["macbook",17500],
    ["book",75],
    ["apple",5]
]

shopp_list=[]


sal = 1000
balance = sal

while not set :
    print("=====货物清单=start=====")
    for index,item in enumerate(list,1): #打印货物清单
        print(index,item)
    print("=====货物清单=end=====")

    choose = input("输入您要买的东西编号：")
    if choose.isdigit() :
        choose = int(choose)-1
        if choose+1 <= len(list):
            print(len(list))
            if balance >= list[choose][1]:
                shopp_list.append(list[choose])
                print("=====购物清单=start=====")
                total = 0
                for shop_index,shop_item in enumerate(shopp_list,1):#打印购物车
                    total += shop_item[1]#计算购物车总价

                    print(shop_index,shop_item)
                balance = sal - total#计算余额
                print("=====购物清单=end===价钱为%s==余额为%s===："%(total,balance))
            else:

                print("you don't have enough money !!!")
        else:
            print("请输入正确数字或者q退出")
    elif choose == "q":
        set = True
    else:
        print("请输入正确数字或者q退出")
print("welcome back")