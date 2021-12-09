#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
计算字符串中所有数字的和
1.字符串中只有小写字母和数字
2.数字可能连续，也可能不连续
3.连续数字要当做一个数处理
如：'12abc34dc5' => 12 + 34 + 5 => 51
'''
s = '12ab100c34de5f'
def sum_of_num(s):
    num = 0
    for i in s:
        if not i.isdigit():
            s = s.replace(i, ' ')
    print(s)
    lt = s.split(' ')
    for j in lt:
        if j.isdigit():
            num += int(j)
    return num
print(sum_of_num(s))
