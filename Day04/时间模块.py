#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/3


import time

# print(help(time)) #打印模块的帮助
#比较常用都的
#格式化字符输出本地时间
struck_time = time.localtime()
print(time.strftime("%Y--%m--%d  %H:%M:%S",struck_time))