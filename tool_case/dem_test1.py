#!/usr/bin/env python
# -*- coding: utf-8 -*-

#给一个升序数组mums=[0,0,1,1,1,2,3,3,4]，请原地删除重复出现的元素，使每个元素只出现一次，返回删除后数
mums=[0,0,1,1,1,2,3,3,4]

# new_mus = []
# for i in mums:
#     if i not in new_mus:
#         new_mus.append(i)
#
# print(new_mus,len(new_mus))
#
#
# print(list(set(mums)))

for i in mums:
    if mums.count(i) >1:
        mums.remove(i)
print(mums,len(mums))
