#!/usr/bin/env python
# coding:utf-8
### 函数化实例
### exercise20150919_6.py

class Student(object):
        def __init__(self, name):
                self.name = name
        def lili(self):
                print "lili"
        def __call__(self):     #函数化声明
                print('my name is %s' %self.name)

s = Student('harry')    #实例化类
s()     #函数化实例
