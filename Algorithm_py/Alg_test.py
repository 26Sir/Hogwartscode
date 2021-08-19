#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 十大排序算法
arr = [1,4,7,3,12,3,34,56,23,67,22]

def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[i]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr