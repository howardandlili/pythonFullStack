#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/11/26

'''
作业三：多级菜单
三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典
'''

# 构建菜单字典
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {
        "山东1市": {
            "山东11县": {
                "山东11村": {}
            },
            "山东12县": {
                "山东12村": {}
            },

        },
        "山东2市": {
            "山东21县": {
                "山东21村": {}
            },
            "山东22县": {
                "山东22村": {}
            },

        },

    },
}

#这里主要是利用列表的顺序来记得父层，当前层和子层，为的就是回退

current_dic = menu

current_list = []

last_dic = {}

current_dic_list = []

while True:
    current_list = [] #把当前名字初始化
    # print("last_dic",last_dic)
    for k,v in current_dic.items():
        current_list.append(k) #把当前名字加到列表中
    for i,v in enumerate(current_list,1):
        print(i,v) #把名字加入关联标号
    choice = input("choice:")
    if choice == 'b':
        # print("qain",current_dic_list)
        current_dic = current_dic_list[-1] #列表的最后一个元素就是上一次的当前环境
        current_dic_list.pop() #只要回退了就要把最后一个元素删掉，目的是方便找到父层
        # print("hou",current_dic_list)
        # continue
    elif choice == 'q':
        current_dic = menu
        # print(current_dic)
        current_dic_list = []
        # continue
    else:
        choice = int(choice) - 1
        current_dic_list.append(current_dic) #把当前环境加入列表主要是记录层数的顺序
        choice_name = current_list[choice] #更加标号把keyname拿出来
        # last_dic = current_dic
        current_dic = current_dic[current_list[choice]] #把当前环境重新定到子层
        # print("current_dic_list",current_dic_list)
