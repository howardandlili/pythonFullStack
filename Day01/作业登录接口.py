#!/user/bin/env python
__author__ = 'Howie'
'''
作业一：博客

作业二：编写登陆接口

输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定
 


'''

data = {}

cout = 0

lock_list = []

flake = False

with open("lock_list") as k:
    for locke_name in k.readlines():
        lock_list.append(locke_name.strip()) #把被锁的名单放到列表中
        # print(lock_list)

while cout < 3 and flake == False:
    username = input("Username:")
    pwd = input("Password:")
    if username not in lock_list: #检查是否在锁名单中
        with open("user_list", "r+") as f:
            for line in f.readlines():
                if username == line.split(":")[0]: #检查是不是有这个名字的
                    data["username"] = line.split(":")[0]
                    data["pwd"] = line.split(":")[1].strip()
                    # print(data)
                    if username == data["username"] and pwd == data["pwd"]:
                        print("ok")
                        flake = True
                        break
                    else: #错误开始计算
                        cout += 1
                        print("error,you have %s time" % (3 - cout))
                        break
                else:#没有这个名字的
                    cout += 1
                    print("do not have the username,,you have %s time" % (3 - cout))
                    break
    else:
        print(username, "have be lock!!")
        break
else:
    if not flake:
        print(username, "have be lock!!")
        with open("lock_list", "a") as l:
            l.write(username + '\n')
