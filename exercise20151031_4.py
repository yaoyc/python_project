#!/usr/bin/env python
# coding: utf-8
### exercise20151031_4.py
"""使用python模块生成子进程池
子进程执行顺序不是固定的，因为子进程拥有独立的系统资源，父进程可以先于子进程结束"""


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print "Run task %s (%s)..." %(name, os.getpid())
    start = time.time()     #开始时间
    time.sleep(random.random() * 3)
    end = time.time()       #结束时间
    print "Task %s runs %0.2f seconds." %(name, (end - start))

if __name__ == '__main__':
    print "Parent process %s." % os.getpid()
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print "Waiting for all subprocesses done..."
    p.close()
    p.join()    #等待子进程工作结束后，父进程再结束
    print "All subprocesses done."
