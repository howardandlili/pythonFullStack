#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/


"""
作业要求：
1.要求进入每个页面都需要求认证
2.如果已经登录了就不需要再登录
3.根据不同的页面要求不同的媒介认证（自己和微信）
目录结构：
1.本地认证文件local_user。
2.微信认证人间wx_user。
"""

login_status = [False, False]


# auth装饰器登录操作
def login(medium):
    def inner(func):
        def wrapper():
            # 多重判断页面和页面的auth状态
            while (not login_status[0] and medium == "local_user") or (not login_status[1] and medium == "wx_user"):
                username = input("输入账号：")
                password = input("输入密码：")
                with open(medium, "r+") as f:
                    for line in f:
                        if username == line.strip().split(":")[0] and password == line.strip().split(":")[1]:
                            print("登录成功")
                            if medium == "local_user":
                                login_status[0] = True
                            else:
                                login_status[1] = True
                        else:
                            print("账号密码错误")
            else:
                func()

        return wrapper

    return inner


# 主页
@login(medium="local_user")
def home():
    print("this is Home!!!")


# 个人信息
@login(medium="wx_user")
def user_info():
    print("this is user_info!!!")


# 小说页面
@login(medium="local_user")
def book():
    print("this is book!!!")


home()
user_info()
book()
