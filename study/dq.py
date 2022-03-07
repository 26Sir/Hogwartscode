#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(0, 10)
b = np.arange(0, 15)
c = np.arange(0, 20)
d = np.arange(0, 30)
e = np.arange(10, 40)
f = np.arange(0, 100)


def pick_arange(arange, num):
    if num > len(arange):
        print("# num out of length, return arange:", end=" ")
        return arange
    else:
        output = np.array([], dtype=arange.dtype)
        seg = len(arange) / num
        for n in range(num):
            if int(seg * (n + 1)) >= len(arange):
                output = np.append(output, arange[-1])
            else:
                output = np.append(output, arange[int(seg * n)])
        print("# return new arange:", end=' ')
        return output

print(a)
print(pick_arange(a, 10))
print(pick_arange(a, 11))
print(pick_arange(b, 10))
print(pick_arange(c, 10))
print(pick_arange(d, 10))
print(pick_arange(e, 10))
print(pick_arange(f, 10))
print(pick_arange(f, 30))
