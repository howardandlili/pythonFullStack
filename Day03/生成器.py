#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/2


# 列表生成式
# a = [x for x in range(10)]
# a = [x * x for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 那么如果放函数行不行？
def f(n,y):
    return n+y

def l():
    for i in range(3):
        yield i

g = l()

for y in [1,10]:
    g = (f(x,y) for x in g)# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    # for i in g:
    #     print(i)
# print(g)


# OK那么生产器是怎么样的呢~？
# a = ((x) for x in range(10))


# 生成器本身就是一个可迭代对象：



print(list(g))


# 生成器的两种方式：
# 1.是上面那样通过((x) for x in range(10)) 这样
# 2.是通过yield来做

# def foo():
#     print("ok1")
#     yield 1 #当执行到这来的时候就会返回1并且跳出函数，然后等到第二次next的到来直接在这里开始往下面走
#     print("ok2")
#     yield 2

# print(foo()) # <generator object foo at 0x0000000000D511A8> 看已经变成了一个生成器了

# for循环后面的是一个可迭代对象，那么什么的可迭代对象呢~？
# 可迭代对象：就是一个有__iter__方法的对象
# [].__iter__()
# {}.__iter__()
# foo().__iter__()
# 这些都是可迭代对象

#
# for i in foo():
#     print(i)

# fib数列


# def fib(Max):
#     n, before, after = 0, 0, 1
#     for i in range(Max-2):
#         after += before
#         before = after
#     return after

# def fib(m):
#     n, before, after = 0, 0, 1
#     while m > n:
#         # print(after)
#         yield after
#         before, after = after, after + before  # 这样的赋值是先运行右边的！一点要记得
#         n += 1
#
#
# f = fib(5)
# for i in f:
#     print(i)



#send()方法

# def f():
#     print("ok1")
#     conut = yield 1 # 在这里会先截断返回一个值给next，然后send方法传了一个参数进来给了conut~
#     print(conut)
#     print("ok2")
#     yield 2
#
#
# g = f()
#
# next(g)
# g.send("outer")

# def add(x,y):
#     print(x,y)
#
# for n in [1, 10]:
#     base = (add(i, n) for i in [0,1,2,3])
# print(list(base))