#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

def matp(x,y,y1,labels):
    # y = [0.21, 0.01, 0.0, 0.9]#纵轴坐标数据
    # y =[]
    # x = [1, 2,3,4] #横轴坐标数据，如果不写，默认数据就是自增1
    # x = []
    min_num = min(min(y),min(y1))
    max_num = max(max(y),max(y1))
    plt.title("cpu Test")#图片标题
    # l = ["x","x","x","x","x2","x","x","x","x","x1"]
    plt.xlabel("time(s)") #横轴文字
    # plt.bar(x,l)
    plt.ylabel("cpu(%)")#纵轴文字
    plt.ylim(ymin=min_num,ymax=max_num)
    plt.yscale('linear') #设置线性轴，包括: linear、log、symlog、logit
    
    # plt.plot(y,color="blue",linewidth=2,marker="o",markersize=5,markerfacecolor="yellow",markeredgewidth=1,markeredgecolor="red")
    plt.plot(y,color="blue",linewidth=2,label="ss")
    plt.plot(y1,color="red",linewidth=1,label="ssss3s")
    plt.xticks(x, labels=labels,rotation=50)
    plt.legend()
    plt.savefig('../data/sn.png')
    plt.show() #图片展示

    # def draw(self):
    #     plt.figure(figsize=(15,5))
    #     plt.xlabel("METER NUM")
    #     plt.ylabel(self.field)
    #     plt.title("MID-"+self.field)
    #     y_ticks = np.linspace(int(self.min_field)-1,int(self.max_field)+0.8,20)
    #     print(f"最大值：{self.max_field},最小值：{self.min_field}")
    #     plt.yticks(y_ticks)
    #
    #     for i in range(len(self.error_list)):
    #         index_date = self.index_list[i].split("-")[-1] + "_" + self.field
    #         plt.plot(self.num_list,self.error_list[i],label = "id%d %s"%(i,index_date))
    #     plt.legend()
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     # print(cur_path)
    #     static_path = cur_path.split("common")[0]
    #     pic_name = self.es_ip_old + "_" + self.tg_id + "_" + self.field + "_" + "result.png"
    #     # plt.savefig(str(static_path) + 'report/'+ pic_name)
    #     plt.savefig('../../report/'+self.photo_name+'.png')
    #     # plt.show()

if __name__ == '__main__':
    # y = [0.21, 0.01, 0.0, 0.9,0.3,0.55,0.23,0.46,0.67,19.80]
    # y1 = [1.21, 1.01, 0.0, 1.9,1.3,1.55,2.23,0.46,0.67,29.80]
    # y = [0.0383, -0.0174, 0.0339, 0.0293, 0.0291, 0.017]
    # y1 = [0.0382, -0.0173, 0.0326, 0.0288, 0.0286, 0.0168]
    # labels = ['361879', '541096', '917693', '558615', '1056675', '347442']
    # x = range(len(labels))
    # x = list(range(0, 10))
    ys = ['001', '001', '001', '001']
    y =  [int(x1) for x1 in ys]
    y1s = ['003', '003', '004', '004']
    y1 = [int(x2) for x2 in y1s]
    labels = ['685057', '685057', '917693', '558615']
    x = range(len(labels))
    matp(x,y,y1,labels)