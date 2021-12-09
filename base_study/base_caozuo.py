#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
统计字符串中每个字符出现的次数
'''
# from collections import Counter
#
# my_list = ['a','a','b','b','b','c','d','d','d','d','d']
# count = Counter(my_list)
#
# print(count)

'''
不借助第三个元素交换两个变量的值
'''
# a =1
# b =2
# a,b =b,a
#
# print(a)
# print(b)

my_sl = (1,3,42,6,72,9)
    # '1234567'

print(type(my_sl))
len1 = len(str(my_sl))
sum0 = 0
for i in range(len1):
    sum0 = sum0 + i
    
print(sum0)

for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s ' %(i,j,i*j),end='')
    print()

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d×%d=%d ' % (j, i, i*j), end='')
        j += 1
    i += 1
    print(' ')


for i in range(1,10):
    six = (" ".join(["%d*%d=%d" % (j, i, i*j) for j in range(1, i+1)]))
    print(six)
    