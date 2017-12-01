#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/11/30


# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)


# 斐波那契数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34
# 0、1、(0+1) (0+1)+1 (0+1)+(0+1)+1
#用递归的话思路分成简单清晰


def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(6))


#循环

def fibo1(n):
    before = 0
    after = 1
    for i in range(n-2):
        ret = before + after
        before = after
        after = ret
    return ret


print(fibo1(6))


