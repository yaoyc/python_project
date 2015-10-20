#!/usr/bin/env python
# coding:utf-8
### exercise20151017_3.py
"""
错误处理机制 try 之 raise 用法
"""

def foo(s):
    n = int(s)
    return 10 / n
def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print "Error!"
        raise   #不带参数，将当前错误原样抛出
        #raise ValueError("input error!")    #错误类型转换
    else:
        pass
    finally:
        pass
def main():
    bar("0")

main()

####################################
#不加 raise 的输出结果为：
#Error!
#
#加 raise 的输出结果为：
#Error!
#Traceback (most recent call last):
#  File "exercise20151017_3.py", line 24, in <module>
#    main()
#  File "exercise20151017_3.py", line 22, in main
#    bar("0")
#  File "exercise20151017_3.py", line 13, in bar
#    return foo(s) * 2
#  File "exercise20151017_3.py", line 10, in foo
#    return 10 / n
#ZeroDivisionError: integer division or modulo by zero
##########################################
