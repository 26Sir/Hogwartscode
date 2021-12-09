#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对字符串列表的操作
切片：s [start: stop: setup] [开始：结束：步长]  步长从开始数，间隔步长的绝对值取值，比如
"""

# int_a = [1, 2, 3, 4, 5, 6, 7]
    
    # '123456789'
# print(int_a[1:3])
# # 取第一个到第八个，步长为2,从第一个开始算，间隔两个取值然后依次类推
# print(int_a[0:8:2])
# # 字符串反转
# print(int_a[::-1])
# # 取出倒数第几个
# print(int_a[-4::])
# int_a.append('ss')
# print(int_a)


# url = list("http://c.biancheng.net/shell/")
#
# #使用索引访问列表中的某个元素
# print(url[3])  #使用正数索引
# print(url[-4])  #使用负数索引
#
# #使用切片访问列表中的一组元素
# print(url[9: 18])  #使用正数切片
# print(url[9: 18: 3])  #指定步长
# print(url[-6: -3])  #使用负数切片
#
# url.append('sp')
# url.extend('ss')
# url.insert(1,'oo')
# print(url)

# print(dir(dict))
scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())

a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
#向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four']=100
print(a)
print(b)
#由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)
print(a)
print(b)