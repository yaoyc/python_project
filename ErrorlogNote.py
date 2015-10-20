#!/usr/bin/env python
# coding:utf-8
### ErrorlogNote.py
"""
将程序错误信息输出到日志 /var/tmp/app.log
"""

import logging
logger = logging.getLogger('app')
log_file = logging.FileHandler('/var/tmp/app.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_file.setFormatter(formatter)
logger.addHandler(log_file)
logger.setLevel(logging.WARNING)
logger.error("We have a problem")
logger.info("Not log this info")

#######################################################
#使用示范
#vim exercise20151017_3.py
#----
#import ErrorlogNote
#logger = ErrorlogNote.logger
#
#def foo(s):
#    return 10/int(s)
#
#def bar(s):
#    return foo(s) * 2
#
#def main():
#    try:
#        bar('0')
#    except StandardError, e:
#        logger.exception(e)     #输出全部报错信息
##        logger.error(e)        #只输出报错提示
#main()
#print 'END'
#
##################################################
