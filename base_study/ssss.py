#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from collections import Counter
#
# a = "asdwfdscsdfeadw"
#
# s = Counter(a)
# print(a.encode())
# print(s)
# print(isinstance(s,dict))
#
#
# print((s))




from datetime import datetime

cur_date = datetime.now().strftime('%Y-%m-%d').split('-')
cur_date = input('请输入要计算的日期，例：2021-3-5：').split('-')
print(cur_date)  # 2021-3-5
cur_year = int(cur_date[0])
cur_month = int(cur_date[1])
cur_day = int(cur_date[2])

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if cur_year % 400 == 0 or (cur_year % 4 == 0 and cur_year % 100 != 0):
    month_day[1] = 29
    if cur_month == 1:
        days = cur_day
    else:
        days = sum(month_day[0:cur_month - 1]) + cur_day


print(days)