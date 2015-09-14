#!/usr/bin/env python
#coding:utf-8
###################################################
#### check string seriation(检测字符串顺序排列)####
##################################################

def str_seriation_check(str):
#       "-*-检测字符串顺序排列-*-"
#       print str_seriation_check.__doc__
        print "-*-检测字符串顺序排列-*-"
        if len(str) < 2:
                return "字符串太短"
        for i in xrange(len(str)):
                if i >= 1:
                        if str[i-1] <= str[i]:
                                continue
                        else:
                                return "Fail,字符串不是按顺序排列的. 第 {} 位大于第 {} 位.".format(i, i+1)
        return "OK,字符串是按顺序排列的."

if __name__ == "__main__":
        print str_seriation_check('abcdfe')
