#!/usr/bin/env python
# coding: utf-8
### exercise20151031_2.py
"""fork生成子进程过程
返回两个值。返回0 给子进程，代表创建成功。返回非0 给父进程，代表子进程注册"""

import os
p = os.fork()
print "Process (%s) start..." % os.getpid()

if p == 0:
    #返回0，给子进程，代表创建成功
    print "child Process (%s) and my parent is %s." % (os.getpid(), os.getppid())
else:
    #返回非0，给父进程，代表子进程注册
    print "I (%s) just created a child Process (%s)." %(os.getpid(), p)   
