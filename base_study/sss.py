#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def getint(s):
#     if type(s) == int:
#         # print(s)
#         return s
#     elif type(s) == str:
#         return 0
#     elif type(s) == list or type(s) == tuple:
#         result = 0
#         for i in range(0, len(s)):
#             result += getint(s[i])
#         # print(result)
#         return result
#     else:
#         return 0


# s = [11,2,'s',[3,7],(68,-1),"123",9]
# print(getint(s))
# sum = 0
# for i in range(0, len(s)):
#     sum = sum + int(getint(s[i]))
# print(sum)



# def Sum(s):
#     sums = 0
#     for ch in s:
#         if isinstance(ch, str):
#             pass
#         if isinstance(ch, int):
#             sums += ch
#         if isinstance(ch, list):
#             sums += Sum(ch)#列表中嵌套层次不限2层,要用递归
#         if isinstance(ch, tuple):
#             sums += Sum(ch)#列表中嵌套层次不限2层,要用递归
#     return sums
# '''
# 列表或元组的数字元素求和,求列表中数字和,列表中嵌套层次不限2层
# 注意：1.列表中的字符串不用参与计算
#      2.列表中嵌套层次不限2层,要用递归
# '''
# print(Sum(s))


# string,char,cnt=input(),input(),0
# for i in string:
#     if(i==char):
#         cnt+=1
# print(cnt)

str = 'abc123abc456aa'
d = {}
for x in str:
    if not x in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1
print(d)