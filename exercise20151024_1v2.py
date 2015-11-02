#!/usr/bin/env python
# coding: utf-8
### exercise20151024_1v2.py
'''
商品定价，装饰器模式，优惠：满100减20满减梯度优惠，周六日8折，春节折上折8折。
对总价进行操作
'''

"""满100减20"""
def Everyday_deco(func):
    def wrapper(values):   #函数包装
        limit = 20      #减20
        count = func(values)
        return count - count/100 * limit    #满减梯度优惠
    return wrapper

"""8折"""
def Weekend_deco(func):
    def wrapper(values):   #函数包装
        limit = 0.8     #8折
        return func(values) * limit
    return wrapper

"""商品定价"""
def pricing(**kwargs):
    total = reduce((lambda x,y: x+y), (v for v in kwargs.values())) #购物总价
    if total >= 100:
        total_deco = price(total)  #优惠后价格
    return "原价列表：{0}\n原价总价：{1}\n优惠后总价：{2}".format(kwargs, total, total_deco)

"""计价策略"""
@Everyday_deco
@Weekend_deco
def price(values):
    return values

print pricing(HUAWEI=3000, Iphone=5288, Thinkpad=7000)
