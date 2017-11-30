#!/user/bin/env python
# DATE : 2017/11/30 0030
__author__ = 'Howie'

# 函数是有自己的作用域的

# def f():
#     a = 1


# 那么这个a变量只能作用于函数体内
'''
python中的作用域分4种情况：

L：local，局部作用域，即函数中定义的变量；
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
G：globa，全局变量，就是模块级别定义的变量；
B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。
'''
# x = int(2.9)  # int built-in
#
# g_count = 0  # global
# def outer():
#     o_count = 1  # enclosing
#     def inner():
#         i_count = 2  # local
#         print(o_count)
#     # print(i_count) 找不到
#     inner()
# outer()
#
# # print(o_count) #找不到

# count = 10  # 全局变量
#
#
# def outer():
#     global count # 如果一定要引用全局变并且还要一样的变量名那么就要用这个方法
#     print(count) #像这样就是不行的为什么呢~因为在print 下面还有一步是定义count，记得！！局部变量是不能修改全局变量的！所以会出错，所以如果要引用全局变量那么就不能再使用一样的变量名！
#     count = 100
#     print(count)
#
#
# outer()
# print(count) #这样就会全局变量给修改了~很危险的操作

# def outer():
#     count = 10
#     def inner():
#         nonlocal count
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()