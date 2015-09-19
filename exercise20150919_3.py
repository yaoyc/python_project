#!/usr/bin/env python
# coding:utf-8
######## 列表去重
######## exercise20150919_3.py

alist = [1,2,3,3,4,5,5,6,6]
print alist

def uniq(List):
        return list(set(List))  #转换为set集合去重，然后转换为list列表

print uniq(alist)
