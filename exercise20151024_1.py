#!/usr/bin/env python
# coding: utf-8
### exercise20151024_1.py
'''
商品定价，装饰器模式，优惠：满100减20，周六日8折，春节折上折8折。
对单品进行操作
'''

"""满100减20"""
def Everyday_deco(func):
    def wrapper(values):   #函数包装
        limit = 20      #减20  
        return func(values) - limit
    return wrapper

"""8折"""
def Weekend_deco(func):
    def wrapper(values):   #函数包装
        limit = 0.8     #8折
        return func(values) * limit
    return wrapper

"""商品定价"""
def pricing(**kwargs):
    for keys,values in kwargs.items():
        kwargs[keys] = "%.2f" % (price(values)) #保留2位小数
    return kwargs

"""计价策略"""
@Everyday_deco
@Weekend_deco
def price(values):
    return values

print pricing(HUAWEI=3000, Iphone=5288, Thinkpad=7000)
