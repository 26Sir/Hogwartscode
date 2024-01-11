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

import json
def demo_test():
    t_list = [{'name':'张三','score':80}, {'name':'李四','score':100}, {'name':'王五','score':10},{'name':'赵六','score':99}, {'name':'何齐','score':60}]
    # t_list = ['{"name":"张三","score":80}','{"name":"李四","score":100}','{"name":"王五","score":10}','{"name":"赵六","score":99}','{"name":"何齐","score":60}']
    n = len(t_list)
    score_list = []
    # print(json.loads(tets))
    # for i in range(n-1):
    #     # print(t_list[i])
    #     for j in range(0, n - i - 1):  # 内层循环控制每次比较的长度
    #         if t_list[j]['score'] > t_list[j + 1]['score']:
    #             t_list[j], t_list[j + 1] = t_list[j + 1], t_list[j]
    #             print(t_list[j])
        # if arr[j] > arr[j + 1]:  # 如果前面的数字大于后面的数字，则交换两个数字的位置
        #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # for i in t_list:
    #     for k,v in i.items():
    #         print(k,v)
    #     print(i)
    ds = sorted(t_list,key=lambda s:s['score'],reverse=True)
    ds = sorted(t_list.items(),key=lambda s:s[1],reverse=True)
    print(ds)

# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n - 1):  # 外层循环控制需要经过多少次比较
#         for j in range(0, n - i - 1):  # 内层循环控制每次比较的长度
#             if arr[j] > arr[j + 1]:  # 如果前面的数字大于后面的数字，则交换两个数字的位置
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# # 测试样例
# array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(array)
# print("排序结果为：", array)

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
    demo_test()