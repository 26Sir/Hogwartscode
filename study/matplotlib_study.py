#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

def matp(x,y):
    # y = [0.21, 0.01, 0.0, 0.9]#纵轴坐标数据
    # y =[]
    # x = [1, 2,3,4] #横轴坐标数据，如果不写，默认数据就是自增1
    # x = []
    plt.title("cpu Test")#图片标题
    
    plt.xlabel("time(s)") #横轴文字
    x1 = list(range(len(x)))
    plt.xticks(x1,rotation=45, fontsize=5)
    
    plt.ylabel("cpu(%)")#纵轴文字
    
    plt.yscale('linear') #设置线性轴，包括: linear、log、symlog、logit
    
    # plt.plot(y,color="blue",linewidth=2,marker="o",markersize=5,markerfacecolor="yellow",markeredgewidth=1,markeredgecolor="red")
    plt.plot(y,color="blue",linewidth=2,markersize=5)
    plt.savefig('../data/sn.png')
    plt.show() #图片展示

if __name__ == '__main__':
    y = [0.21, 0.01, 0.0, 0.9,0.3,0.55,0.23,0.46,0.67]
    x = [1.9, 2, 3, 4,5,6,7,8,9]
    matp(x,y)