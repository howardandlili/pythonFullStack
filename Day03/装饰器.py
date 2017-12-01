#!/user/bin/env python
# DATE : 2017/12/1 0001
# __author__ = 'Howie'


import time

"""
闭包有两个条件：
1.内函数
2.引用外环境变量
"""


# def outer():
#     x = 10
#
#     def inner():
#         print(x)
#     return inner  # 这样inner就是闭包
#
#
# outer()()

def show_time(foo):
    def inner():
        start = time.time()
        foo()
        end = time.time()
        print("times:", (end - start))
    return inner #  这样我就可以把想要的操作的内存地址拿到手了

def foo():
    time.sleep(1)
    print("foo.....")


def bar():
    time.sleep(1)
    print("bar.....")
# foo()
# show_time(foo) #功能实现但是调用方式改变了


foo = show_time(foo) #把拿到手的内存地址改成和原来的函数一样的名字

foo() # 这样就可以直接调用原来的函数名（记得不是原来的函数只是名字一样）来达到想要的扩展效果
