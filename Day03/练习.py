#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/2


"""
使用文件读取拿到最长的一行
"""
# print(max(len(x) for x in open("file","r")))
# max(len(x.strip()) for x in open("file","r"))

def add(s, x):
 return s + x

def gen():
 for i in range(4):
  yield i

base = gen()
for n in [1,10]:
 base = (add(i, n) for i in base)

print (list(base))

'''
核心语句就是:
for n in [1, 10]:
 base = (add(i, n) for i in base)
在执行list(base)的时候，开始检索，然后生成器开始运算了。关键是，这个循环次数是2,也就是说，有两次生成器表达
式的过程。必须牢牢把握住这一点。
生成器返回去开始运算，n = 10而不是1没问题吧，这个在上面提到的文章中已经提到了，就是add(i, n)绑定的是n这个
变量，而不是它当时的数值。
然后首先是第一次生成器表达式的执行过程:base = (10 + 0, 10 + 1, 10 + 2, 10 +3),这是第一次循环的结
果(形象表示，其实已经计算出来了(10,11,12,13))，在这个时候base已经改变了 所以第二次的时候是拿(10,11,12,13)，来计算的然后第二次，
base = (10 + 10, 11 + 10, 12 + 10, 13 + 10) ,终于得到结果了[20, 21, 22, 23].
'''