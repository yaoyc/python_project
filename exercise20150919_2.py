#!/usr/bin/env python
# coding:utf-8
##### 判断是否为回文字符串（对称）
##### exercise20150919_2.py
# return 0 --> Ok
# return 1 --> Fail

# method_1
def Str_1(str):
        if str == str[::-1]:    #直接翻转比较
                return 0
        return 1
print Str_1("aba")
print Str_1("abcba")
print Str_1("abcra")

print "*"*20    #分隔线
# method_2
def Str_2(str):
        lenth = len(str) / 2
        for i in xrange(lenth):         
                if str[i] != str[-(i+1)]:       #首尾比较
                        return 1
        return 0

print Str_2("aba")
print Str_2("abcba")
print Str_2("abcra")
