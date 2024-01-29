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
    # ds = sorted(t_list.items(),key=lambda s:s[1],reverse=True)
    print(ds)

# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n - 1):  # 外层循环控制需要经过多少次比较
#         for j in range(0, n - i - 1):  # 内层循环控制每次比较的长度
#             if arr[j] > arr[j + 1]:  # 如果前面的数字大于后面的数字，则交换两个数字的位置
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

def demo_3():
    str_1 = 'bdackmkdbb'
    set_1 = set()
    for i in str_1:
        if i not in set_1:
            set_1.add(i)
        else:
            print(i)
            return i

#输入一个字符串，求出字符串里字符出现最多的数量
def find_str(s):
    if len(s)==0 :
        return 0
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            count[char] +=1
    arr = []
    for k,v in count.items():
        arr.append((k,v))
    for i in range(len(arr) - 1):  # 外层循环控制需要经过多少次比较
        for j in range(0, len(arr) - i - 1):  # 内层循环控制每次比较的长度
            if arr[j][1] > arr[j + 1][1]:  # 如果前面的数字大于后面的数字，则交换两个数字的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[-1][0]

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

# 打印数组中出现次数过半的数
def find_mid_num(in_list):
    n = len(in_list)
    if n == 0:
        return 0
    conut = {}
    for j in in_list:
        if j not in conut:
            conut[j] = 1
        else:
            conut[j] += 1
    m = [(k, v) for k, v in conut.items() if v >= n / 2]
    mid_num =[]
    for k, v in conut.items():
        if v >= n / 2:
            mid_num.append((k,v))
    return mid_num

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        return sorted

"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
def find_len(nums):
    list_len = len(nums)
    if list_len == 0:
        return 0
    for i in range(0, list_len):
        for j in range(0, list_len - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    res = m = 1
    for n in range(list_len - 1):
        if nums[n] == nums[n - 1]:
            continue
        if nums[n + 1] - nums[n] == 1:
            m += 1
            res = max(res, m)
        else:
            m = 1
    return res

def longestConsecutive(nums):
        res = 0
        hash_dict = dict()
        for num in nums:
            # 新进来哈希表一个数
            if num not in hash_dict:
                # 获取当前数的最左边连续长度,没有的话就更新为0
                left = hash_dict.get(num-1,0)
                # 同理获取右边的数
                right = hash_dict.get(num+1,0)
                """不用担心左边和右边没有的情况
                因为没有的话就是left或者right0
                并不改变什么
                """
                # 把当前数加入哈希表，代表当前数字出现过
                hash_dict[num] = 1
                # 更新长度
                length = left+1+right
                res = max(res,length)
                # 更新最左端点的值，如果left=n存在，那么证明当前数的前n个都存在哈希表中
                hash_dict[num-left] = length
                # 更新最右端点的值，如果right=n存在，那么证明当前数的后n个都存在哈希表中
                hash_dict[num+right] = length
                # 此时 【num-left，num-right】范围的值都连续存在哈希表中了
                # 即使left或者right=0都不影响结果
        return res

if __name__ == '__main__':
    # demo_test()
    # ss = find_mid_num(in_list="ac")
    # print(ss)
    sort_list = merge(nums1=[1,2,3,4],m=4,nums2=[2,4,6,8],n=4)
    ss = longestConsecutive(nums = [1,2,3,4,7,8,9,10,11,12,100])
    print(ss)
    print(sort_list)