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


if __name__ == '__main__':
    demo_test()