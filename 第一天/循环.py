#!/user/bin/env python
__author__ = 'Howie'
# number1 = 1

# while number1 <= 5:
#     number2 = 0
#     print(number1, end="_")
#     while number2 <= 7:
#         if number2 == 7:
#             print(number2)
#             break
#         print(number2, end="-")
#
#         number2 += 1
#     number1 += 1

# while number1 <= 9:
#     number2 = 1
#     while number2 <= 9:
#         if number1 == number2:
#             print(number2, "*", number1, "=", number1 * number2)
#             break
#         print(number2, "*", number1, "=", number1 * number2, end="   ")
#         number2 += 1
#     number1 += 1

# number1 = int(input("x:"))
# number2 = int(input("y:"))
#
#
#
# while number2 != 0:
#     num1 = number1
#     while num1 != 0:
#         print("*", end=" ") # 宽是用来负责打印几个#
#         num1 -= 1
#     print("") # 高是用来负责换行
#     number2 -= 1

# line = 5
# line1 = line
#
# while line > 0:
#     num = line1
#     while num >= line:
#         print("*", end="")
#         num -= 1
#     print()
#     line -= 1


num = 1

while num <= 9 :
    sec = 1
    while sec <= num: #
        print(sec,"*",num,"=",num*sec,end="\t")
        sec += 1
    print()
    num += 1