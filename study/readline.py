#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs


def readtxt():
    f = codecs.open('data.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
    line = f.readline()  # 以行的形式进行读取文件
    list1 = []
    while line:
        a = line.split()
        b = a[2:3]  # 这是选取需要读取的位数
        # list1.append(b)  # 将其添加在列表之中
        list1.extend(b)
        line = f.readline()
    f.close()
    
    print(list1)
    return list1


if __name__ == '__main__':
    readtxt()
