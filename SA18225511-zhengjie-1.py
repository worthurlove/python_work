#Function:Calcullate the volume and surface of a sphere frome its radius
#Author:worthurlove
#Date:2018.9.20

import math


def Calcullate_volume(radius):
    '''
    根据半径计算球的体积，公式：V = (4/3)*pi*r^3
    '''
    volume = (4 * math.pi * radius**3) / 3
    return volume


def Calcullate_area(radius):
    '''
    根据半径计算球的表面积，公式：S = 4*pi*r^2
    '''
    area = 4 * math.pi * radius**2
    return area


def sphere():
    '''
    用户输入半径，输出球的体积和表面积
    '''
    radius = float(input('请输入球的半径:'))
    print("球体的体积为：{0}".format(Calcullate_volume(radius)))
    print("球体的表面积为：{0}".format(Calcullate_area(radius)))


sphere()#调用球体函数
