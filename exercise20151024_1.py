#!/usr/bin/env python
# coding: utf-8
### exercise20151024_1.py
'''
商品定价，装饰器模式，优惠：满100减20，周六日8折，春节折上折8折。
'''

"""满100减20"""
def Everyday_deco(func):
    def wrapper(**kwargs):   #函数包装
        limit = 20      #减20  
        return {n: kwargs[n] - limit for n in kwargs}
        func(**kwargs)      #调用原始函数
    return wrapper


"""8折"""
def Weekend_deco(func):
    def wrapper(**kwargs):   #函数包装
        limit = 0.8     #8折
        return {n: kwargs[n] * 0.8 for n in kwargs}
        func(**kwargs)
    return wrapper

"""商品定价"""
@Everyday_deco
@Weekend_deco
def pricing(**kwargs):
    return kwargs

#print pricing(HUAWEI=3000, Iphone=5288, Thinkpad=7000)
