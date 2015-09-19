#!/usr/bin/env python
# coding:utf-8
#### 计算平面坐标中两点距离
#### exercise20150919_4.py

class Point(object):    #平面坐标计算类
        def __init__(self, x, y):       #坐标初始化
                self.X = x
                self.Y = y
        def juli(self, other):  #传入标点对象
                return pow(pow(self.X - other.X, 2) + pow(self.Y - other.Y, 2), 0.5)    #>两点距离计算

a = Point(3,4)  # a点
b = Point(1,2)  # b点
print a.juli(b) #计算 a点到 b点的距离
