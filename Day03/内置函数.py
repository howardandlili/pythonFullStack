#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/11/30


# str1 = ['a', 'b', 'c', 'd']
#
#
# def fun1(s):
#     if s != 'a':
#         return s
#
#
# ret = filter(fun1, str1) # filter(),是把一个可迭代的对象放到一个函数里面去过滤
#
# print(list(ret))  # ret是一个迭代器对象


# str2 = [1,2,3,4]
#
# def fun2(s):
#
#     return s + 1
#
# ret = map(fun2, str2) # map()， 是把一个可迭代的对象放到一个函数里面再操作一次。
#
# print(ret)      #  map object的迭代器
# print(list(ret))#  ['aalvin', 'balvin', 'calvin', 'dalvin']
'''
对sequence中的item依次执行function(item)，将执行结果组成一个map object迭代器返回.
map也支持多个sequence，这就要求function也支持相应数量的参数输入：
'''

# def f(x,y):
#     s = x + y
#     return s
#
# ret = map(f,range(1,11),range(11,21))# 等于两个列表按顺序拿一个个出来处理，一人一个！
# print(list(ret)) # [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

#
# from functools import reduce
#
#
# def f(x,y):
#     return x*x + y*y
#
# print(reduce(f,range(1,4))) #等于是把一个列表的元素的前两个处理后的值变成列表的第一个元素再和后一个元素做处理知道最后

#匿名函数
add = lambda a,b : a + b

print (add(2,3))