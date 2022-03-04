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
    
    plt.ylabel("cpu(%)")#纵轴文字
    
    plt.yscale('linear') #设置线性轴，包括: linear、log、symlog、logit
    
    plt.plot(y,color="blue",linewidth=2,marker="o",markersize=5,markerfacecolor="yellow",markeredgewidth=1,markeredgecolor="red")
    plt.savefig('../data/sn.png')
    plt.show() #图片展示

if __name__ == '__main__':
    y = [0.21, 0.01, 0.0, 0.9]
    x = [1, 2, 3, 4]
    matp(x,y)