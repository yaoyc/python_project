#!/usr/bin/env python
#coding:utf-8
###### 递归练习 ########
###### f(0) = 1
###### f(1) = 1
###### f(n) = f(n-1) + f(n-2)
###### exercise20150919_1.py

def func(N):
        if N == 0 or N == 1:
                return 1
        else:
                return func(N-1) + func(N-2)

print func(0)
print func(1)
print func(2)
