#!/usr/bin/env python
#coding:utf-8
### exercise20151017_2.py
"""
生成随机序列号，包括大写字母、数字，可以指定长度，不会生成重复序列号
"""

def jhm(length):
    import random
#    sum = pow(36, length)   #激活码组合总量
#--------生成激活码待选字符列表
    chr_list = ["0","1","2","3","4","5","6","7","8","9"]
    for lettr in xrange(65, 91):    #生成基本字符列表
        chr_list.append(chr(lettr))

    Licence_List = chr_list[:]  #初始化激活码列表
    tmp_list = []       #初始化临时容器

    for i in xrange(length-1):      #控制序列号位数
        for values in chr_list:
            tmp_list += jhm_count(Licence_List, values)     #序列号复杂度要求
        Licence_List = tmp_list[:]
        tmp_list = []

    Licence_Cnt = len(Licence_List)     #序列号总数
#    if sum != Licence_Cnt:
#        return "Error:序列号列表生成错误"

    num = random.randint(0, Licence_Cnt)    #生成随机数取序列号
    Licence_Cache = Licence_List[num]
    Licence_List.pop(num)       #删除序列库中被取出序列号
    return Licence_Cache        #返回被取出序列号
        

def jhm_count(Licence_List, values):        #序列号复杂度实现函数
    Licence_List_tmp = Licence_List[:]
    for keys in xrange(len(Licence_List)):
        Licence_List_tmp[keys] += values
    return Licence_List_tmp
### -------------------------------   
print jhm(3)
