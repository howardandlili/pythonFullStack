#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/2


# 生成器都是迭代器，但是迭代器不一定是生成器

l=[1,2,3,4]
d=iter(l) # iter()方法就是把列表做成一个迭代器，可以用这个方法的就是可迭代对象
print(d) #<list_iterator object at 0x0000000000B3EBA8>
"""
迭代器有两个条件：
1.有iter方法
2.有nest()方法
"""

for i in d:
    print(i)
"""
从这里我们就可以找到其实for循环一共做了三件事
1.把可迭代对象做成迭代器
2.把迭代器使用next方法
3.把异常抛出了退出
"""