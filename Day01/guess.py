#!/user/bin/env python
__author__ = 'Howie'
number = 100
while True:
    youNO = input("输入你的数值")
    youNO = int(youNO)
    if youNO == number:
        print("对了") #良好的习惯 就是让程序块点完成~
        break
    elif youNO < number:
        print("小了")
    else:
        print("大了")
