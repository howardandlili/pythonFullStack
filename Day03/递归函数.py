#!/user/bin/env python
# DATE : 2017/11/30 0030
__author__ = 'Howie'


# 使用普通函数
# def f(n):
#     z = 1
#     while n > 0:
#         z *= n
#         n -= 1
#     return z
#
#
# print(f(5))


# 使用递归函数


def recursive(n):
    if n == 1:
        return 1
    return n * recursive(n - 1)  # 其实就是 5*4*3*2*recursive(1) 改变的只是不断从return传回去的参数


print(recursive(5))
'''
这里有两要点
1.函数调用自己
2.什么时候结束，结束的时候return什么
'''
