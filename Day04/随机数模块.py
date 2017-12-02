#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/12/3


import random, string


# print(random.random())#限定在（0,1）的随机数
# print(random.randint(1,8))#限定在（1,8）的随机数是正整数
# print(random.randrange(1,8))#和上面一样，只不过是不包括8的上面会包括
# print(random.choice("hello"))#限定在元素的元素
# print(random.sample([123,4,[1,2]],2))#限定在元素随机2个元素
# print(random.sample([123,4,[1,2]],2))#限定在元素随机2个元素

#玩一个验证码5位数的
# def v_code():
#     low = string.ascii_lowercase
#     num = string.digits
#     code_list = "".join((low, num)) #这样有可能会把列表弄得很大
#     code = "".join(random.sample(code_list, 5))
#     return code
#
#
# print(v_code())

# def v_code():
#     code = ''
#     for i in range(5):
#         if random.randrange(99)%3 == 0: #这样就大概可以控制数字的概率
#             add = str(random.randrange(10))
#         else:
#             add = chr(random.randrange(97,123))
#         code += add
#     print(code)
#
# v_code()

def v_code():
    code = ''
    for i in range(5):
        add = random.choice(str(random.randrange(10))+chr(random.randrange(97,123)))
        code += add
    print(code)
v_code()