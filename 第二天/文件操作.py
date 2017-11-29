#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/11/28
import os, sys
#修改源文件

#打开两个文件一个源文件一个是临时文件
with open("file1", "r+", encoding="utf-8") as f1, open("file2", "w+", encoding="utf-8") as f2:
    for line in f1: #开始一行行的读取源文件
        if "惊回千里梦" in line:#匹配要修改的行
            line = line.replace("惊回千里梦", "123")#开始操作
        f2.write(line)#写入到临时文件去
os.remove("file1")#删除源文件
os.rename("file2", "file1")#改临时文件名为源文件
