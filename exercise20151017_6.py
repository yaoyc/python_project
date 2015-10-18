#!/usr/bin/env python
#coding:utf-8
### exercise20151017_6.py
"""
生成随机序列号，包括大写字母、数字，可以指定长度，不会生成重复序列号
以random方式实现，即用即取
"""
import random
import string
def jhm(length):
#--------生成序列号待选字符列表，包括大写字母、数字
    chr_list = string.digits + string.letters[:len(string.letters)/2]
#----------------------------
    chr_sum = len(chr_list)
    Licence_sum = pow(chr_sum, length)   #序列号组合总量
#----------------------------------
    Licence_old = []  #初始化已激活序列号列表
#--------------------------------
    while True:
        Licence = jhm_compute(length, chr_sum, chr_list)    #生成序列号
        if len(Licence) == length:          #判断长度要求
            if Licence not in Licence_old:      #判断是否为已激活序列号
                break

    Licence_old.append(Licence)     #更新已激活序列号列表
    old_sum = len(Licence_old)      #已激活序列号总数
    sup_sum = Licence_sum - old_sum     #剩余序列号总数
    Licence_Cache = Licence         #新生成序列号，可用序列号
    return "已激活序列号总数：{0}\n剩余序列号总数：{1}\n新生成序列号：{2}".format(old_sum, sup_sum, Licence_Cache)

def jhm_compute(length, chr_sum, chr_list):     #生成序列号
    Licence = "0"
    for count in xrange(length):
        num_choice = random.randint(0, chr_sum-1)    #生成随机数取序列号
        Licence += chr_list[num_choice]
    Licence = Licence[1:]
    return Licence
#------------------------
print jhm(80)




###############################################################
#--------------Start 交互界面，可不使用----------------------
### 数据持续性存储未解决
#def showmenu():
#    user_IN = '''
#***请按以下提示输入选项***
#1: 生成序列号
#0: 退出
#
#Enter choice:'''
#    length_limit = 100  #序列号长度限制
#    length_IN = '''
#***请输入生成序列号长度***
#提示：限定长度 {0} 位以内
#
#Enter choice:'''.format(length_limit)
#    while True:
#        while True:
#            try:
#                user_input = int(raw_input(user_IN).strip())
#            except (EOFError, KeyboardInterrupt, ValueError):
#                user_input = 0
#        
#            if str(user_input) not in "01":
#                print "输入错误，重新输入"
#            else:
#                break
#        if user_input == 0:
#            break
#        else:
#            try:
#                length_input = int(raw_input(length_IN).strip())
#            except (EOFError, KeyboardInterrupt, ValueError):
#                user_input = 0
#
#            if length_input > length_limit:
#                print "序列号长度超出"
#            else:
#                print jhm(length_input)
#
#if __name__ == "__main__":
#    showmenu()
#--------------END 交互界面，可不使用----------------------
