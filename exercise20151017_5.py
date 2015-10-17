#!/usr/bin/env python
# coding:utf-8
### exercise20151017_5.py
'''
简短地生成随机序列号，包括大小写字母、数字，可以指定长度
使用模块实现
'''
#生成随机密码
from random import choice
import string

# string.letters 生成大小写字母 a-zA-Z
# string.digits 生成数字 0-9
def GenPassword(length=8,chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

if __name__=="__main__":
    for i in range(10):     #生成10个随机序列号
        print(GenPassword(8))     #长度为8
