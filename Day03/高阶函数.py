#!/user/bin/env python
# DATE : 2017/11/30 0030
__author__ = 'Howie'


def f(n):
    return n*n


def foo(a,b,f):
    c = f(a)+f(b)
    return c

print(foo(2,3,f)) #f是一个函数名，把一个函数名当做一个参数传给另外一个函数