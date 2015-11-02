#!/usr/bin/env python
# coding: utf-8
### exercise20151031_3.py
"""使用python模块生成子进程"""

from multiprocessing import Process
import os

def run_proc(name):
    print "Run child Process %s (%s)..." %(name, os.getpid())

if __name__ == '__main__':
    print "Parent Process %s." % os.getpid()
    p = Process(target = run_proc, args = ("test",))
    print "Process will start."
    p.start()
    p.join()
    print "Process end"
