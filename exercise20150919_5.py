#!/usr/bin/env python
# coding:utf-8
### 迭代器实例
### exercise20150919_5.py

class Reverse(object):          #字符串翻转
        def __init__(self, a_str):
                self.xstr = a_str
                self.len = len(a_str)
        def __iter__(self):     #迭代器声明
                return self
        def next(self):         #迭代
                if self.len == 0:
                        raise StopIteration()
                self.len -= 1
                return self.xstr[self.len]

for i in Reverse('abcdef'):
        print i
