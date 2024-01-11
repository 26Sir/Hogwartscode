#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 性能测试脚本，实现功能支持si接口， 每一秒突增100qps，持续达5分钟 以hhttp协议为例

# import requests
#
# def demo_test(all_time,jg_time=1,up_qps=100):
#     all_times = all_time * 60
#     for i in range(all_times):
#         #请求对应接口，一次发送请求数量为up_qps，默认100次
#         for j in range(up_qps):
#             r = requests.get("https://www.baidu.com")
#         print(f"第{i+1}个100qps请求成功")
#
# if __name__ == '__main__':
#     demo_test(all_time=5)

"""
["{"name":"张三","score":80}","{"name":"李四","score":100}","{"name":"王五","score":10}","{"name":"赵六","score":99}","{"name":"何齐","score":60}"]

按照得分来，进行排序 按照原有格式输出
"""


def demo_test():
    input_list = ["{'name':'张三','score':80}", "{'name':'李四','score':100}", "{'name':'王五','score':10}",
                  "{'name':'赵六','score':99}", "{'name':'何齐','score':60}"]
    name_list = []
    score_list = []
    for i in input_list:
        print(i)
        # print(i["name"])
        # print(i['score'])
        # name_list.append(i["name"])
        score_list.append(i["score"])
    sort_score_list = sorted(score_list)
    print(sort_score_list)


def demo_3():
    str_1 = 'bdackmkdbb'
    set_1 = set()
    for i in str_1:
        if i not in set_1:
            set_1.add(i)
        else:
            print(i)
            return i


def find_second_unique(s):
    count = {}  # 创建一个空字典用于记录每个字符及其出现次数

    for char in s:
        if char not in count:
            count[char] = 1  # 初始化计数为1
        else:
            count[char] += 1  # 将该字符的计数加1
    # second_unique = None  # 定义变量存放第二个唯一字符
    #
    # for key, value in count.items():
    #     if value == 1 and second_unique is None:
    #         second_unique = key  # 当遇到第二个唯一字符时赋值给变量
    
    list_s = list(s)
    one_list = []
    for listi in list(s):
        i_index = list_s.index(listi)
        if listi not in list_s[i_index+1:]:
            one_list.append(listi)
    print(f"第二次出现的唯一字符{one_list[1]}")

    first_unique = None  # 第一个只出现一次的字符
    second_unique = None  # 第二个只出现一次的字符
    for char in s:
        if count[char] == 1:
            if first_unique is None:
                first_unique = char  # 记录第一个只出现一次的字符
            else:
                second_unique = char  # 记录第二个只出现一次的字符，并退出循环
                break
            
    return second_unique
    
    






if __name__ == '__main__':
    # demo_test()
    # 测试示例
    string = "bdackmkdbb"
    result = find_second_unique(string)
    # print(set(string))
    print("第二个唯一字符是:", result)
    # demo_3()