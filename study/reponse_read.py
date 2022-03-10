#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re
from study.matplotlib_study import matp


def readtxt():
    f = codecs.open('respone_time_2022_03_07.log', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
    line = f.readline()  # 以行的形式进行读取文件
    list1 = []
    while line:
        # a = line.split("time:")
        a = re.split('time:|-秒\n', line)
        b = a[1:2]  # 这是选取需要读取的位数
        # list1.append(b)  # 将其添加在列表之中
        list1.extend(b)  # 将列表相加得到最后完整的一列数据
        line = f.readline()
    f.close()
    list1 = [float(x) for x in list1]
    print(list1)
    list2 = sorted(enumerate(list1), key=lambda x: x[1])
    # print(list2)
    return list1


def pick_arange(arange, num):
    if num > len(arange):
        print("# num out of length, return arange:", end=" ")
        return arange
    else:
        output = []
        seg = len(arange) / num
        for n in range(num):
            if int(seg * (n + 1)) >= len(arange):
                output.append(arange[-1])
            else:
                output.append(arange[int(seg * n)])
        print("# return new arange:", output)
        return output


if __name__ == '__main__':
    six = [0.177388, 0.016313, 0.102537, 0.010836, 0.034788, 0.006065, 0.020654, 0.00785, 0.008291, 0.006095, 0.008397,
           0.02267, 0.019705, 0.592305, 0.039456, 0.026491, 0.03162, 0.02119, 0.020514, 2.212011, 0.038621, 0.035103,
           0.081671, 0.021487, 0.021477, 0.09231, 0.273191, 0.140423, 0.020559, 0.028786, 0.011911, 0.018937, 0.010598,
           0.009495, 0.006943, 0.005847, 0.009793, 0.006276, 0.008608, 0.013677, 0.005939, 0.008043, 0.00639, 0.274004,
           0.069972, 0.247297, 0.496712, 0.008302, 0.008506, 0.00996, 0.008758, 0.007629, 0.122132, 0.015459, 0.007035,
           0.015889, 0.014468, 0.017074, 0.020357, 0.016779, 0.017331, 0.00738, 0.009206, 0.007502, 0.134073, 0.177951,
           0.188491, 0.828798, 0.213619, 0.229378, 0.199218, 0.064078, 0.011714, 0.238599, 0.012371, 0.012918, 0.061287,
           0.060404, 0.077472, 0.068994, 0.061358, 0.065392, 0.059311, 0.067301, 0.064069, 0.142213, 0.062422, 0.029051,
           0.02545, 0.032491, 0.009267, 0.009274, 0.006316, 0.036086, 0.007707, 0.116874, 0.108421, 0.018687, 0.034207,
           0.01042, 0.006144, 0.008399, 0.007146, 0.031606, 0.008739, 0.006387, 0.009846, 0.007797, 0.016242, 0.021636,
           0.040709, 0.009904, 0.010349, 0.023128, 0.006046, 0.008991, 0.008457, 0.011593, 0.006131, 0.008739, 0.007634,
           0.01086, 0.008848, 0.006912, 0.025909, 0.007809, 0.227931, 0.009621, 0.008595, 0.005604, 0.0145, 0.021162,
           0.031993, 0.029743, 0.008728, 0.011026, 0.006359, 0.008986, 0.008329, 0.024168, 0.059831, 0.02663, 0.008616,
           0.007682, 0.006351, 0.009066, 0.0084, 0.129604, 0.006656, 0.008187, 0.007986, 0.132031, 0.209505, 0.008589,
           0.009245, 0.057505, 0.047951, 0.042466, 0.068701, 0.043091, 0.048027, 0.072775, 0.045078, 0.039727, 0.061775,
           0.040563, 0.00851, 0.008467, 0.045349, 0.051834, 0.049357, 0.038277, 0.009466, 0.028906, 0.009372, 0.050013,
           0.042726, 0.010812, 0.032191, 0.007039, 0.046983, 0.036014, 0.008316, 0.047407, 0.007172, 0.048468, 0.039631,
           0.009418, 0.055584, 0.006779, 0.061085, 0.041253, 0.042022, 0.088497, 0.041682, 0.043361, 0.035865, 0.038321,
           0.039077, 0.042964, 0.041268, 0.04082, 0.038437, 0.038115, 0.008688, 0.010732, 0.006179, 0.008556, 0.192421,
           0.023481, 0.112281, 0.120149, 0.040248, 0.026084, 0.025619, 0.022267, 0.02087, 0.022327, 0.022134, 0.022062,
           0.021593, 0.023198, 0.022643, 0.023822, 0.313746, 0.063237, 0.059804, 0.079719, 0.084551, 0.06325, 0.066458,
           0.075815, 0.094316, 0.058352, 0.061383, 0.077179, 0.077961, 0.071241, 0.059485, 0.074527, 0.074073, 0.066732,
           0.062687, 0.074786, 0.078439, 0.061711, 0.065127, 0.077494, 0.080786, 0.061145, 0.071308, 0.07978, 0.056257,
           0.040892, 0.033729, 0.035967, 0.038545, 0.007553, 0.00685, 0.008087, 0.006316, 0.008719, 0.007065, 0.008383,
           0.008104, 0.006405, 0.027259, 0.008738, 0.007228, 0.008857, 0.008071, 0.008034, 0.006918, 0.007849, 0.006779,
           0.006915, 0.007308, 0.007295, 0.006452, 0.006153, 0.006566, 0.007669, 0.013281, 0.007266, 0.008703, 0.020819,
           0.013263, 0.008946, 0.127626, 0.202065, 0.232146, 0.110061, 0.01971, 0.023762, 0.025046, 0.024058, 0.023654,
           0.020183, 0.024402, 0.021854, 0.009028, 0.010705, 0.005576, 0.009289, 0.158686, 0.096092, 0.381736, 0.11769,
           0.024024, 0.023552, 0.023248, 0.024803, 0.027537, 0.02325, 0.023649, 0.020967, 0.010408, 3.342102, 0.008518,
           0.005958, 0.011008, 0.00766, 0.06308, 0.071779, 0.055357, 0.069038, 0.064487, 0.058081, 0.974286, 0.052104,
           0.048546, 0.089371, 0.048561, 0.047955, 0.046184, 0.04642, 0.053461, 0.055153, 0.051353, 0.04728, 0.213895,
           0.480251, 0.38741, 0.304377, 0.283418, 0.266124, 0.298325, 109.562683, 0.573877, 0.04443, 0.013986, 0.010975,
           0.005571, 0.009218, 0.00721, 0.073478, 0.059448, 0.076238, 0.069319, 0.0597, 0.068532, 0.061338, 0.075513,
           0.030336, 0.440722, 0.030369, 0.029871, 0.028744, 0.027635, 0.027512, 0.026114, 0.030605, 0.031994, 0.031073,
           0.090937, 0.23169, 0.093872, 0.388359, 0.119055, 0.274934, 0.087588, 0.311221, 0.146238, 0.386968, 0.071156,
           0.266515, 0.080835, 0.220997, 0.072802, 0.252932, 0.008437, 0.014015, 0.006153, 0.008363, 0.006638, 0.036064,
           0.03692, 0.034882, 0.032978, 0.032236, 0.032257, 0.032922, 0.029121, 0.036222, 0.039872, 0.028314, 0.031872,
           0.577069, 0.586426, 0.539984, 0.553605, 0.552403, 0.574404, 0.542687, 0.538972, 0.546573, 0.526611, 0.550451,
           0.535876, 0.536218, 0.546387, 0.542953, 0.359627, 0.020021, 0.021474, 0.017903, 0.022603, 0.028274, 0.018349,
           0.017874, 0.017484, 0.214975, 0.34841, 0.201476, 0.020545, 0.009409, 0.008755, 0.006233, 0.010741, 0.008501,
           0.057363, 2.256149, 0.07003, 0.051121, 1.140095, 0.068433, 0.040033, 0.063679, 0.069854, 0.086878, 0.011628,
           1.781196, 1.382813, 0.568678, 0.025299, 0.032029, 0.008729, 0.009677, 0.005836, 0.008832, 0.006482, 0.008152,
           0.01432, 0.05181, 0.010926, 0.085622, 0.011353, 0.009482, 0.008049, 0.006467, 0.009339, 0.007206, 0.513962,
           0.008815]
    # pick_arange(readtxt(), 100)
    # x = ['2:50:40', 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16]
    x = ["2:50:40", '2:50:50', '2:51:60', '2:50:40', '2:50:40', '2:50:40', '2:50:40', 8, 9, 10, 11, 12, 13, 14, 15, 16]
    matp(pick_arange(six, 100))
