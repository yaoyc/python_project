#!/usr/bin/env python
#coding:utf-8
### 打印一个三角形
### 只打印边框
### exercise20151017_1.py

def sjx(n):
    for i in xrange(1,n+1):
        print " " * (n - i),    
#------处理第一行与最后一行  
        if i == 1:
            print "*"
            continue
        elif i == n:
            print "* " * i
            continue
#------
        print "*",
        for space in xrange(2,i+1):
            if space == i:
                print "*"
            else:
                print " ",
#------
sjx(10)
