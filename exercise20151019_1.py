#!/usr/bin/env python
#coding:utf-8
### exercise20151019_1.py
'''
一个螺旋数字矩阵
输入一个数字n，打印出如下数字：
  1   2   3   4
 12  13  14   5
 11  16  15   6
 10   9   8   7
这是输入4的情况。
'''

def num_set(num):
    set_list = [[0]*num for i in xrange(num)]   #矩阵模板
    init_Y = 0    #Y轴，行
    init_X = 0    #X轴，列
    value = 1       #初始值
    count = 1       #初始圈数
#---direction = ("E", "S", "W", "N")
#---方向操作    右、下、左、上

    while True:
        direction = "E"     #初始化执行方向
#-------向右走
        while direction == "E":
            if init_Y > num - count:
                direction = "S"
                init_Y -= 1
                value -= 1
            else:
                set_list[init_X][init_Y] = value
                init_Y += 1
                value += 1
#-------向下走
        while direction == "S":
            if init_X > num - count:
                direction = "W"
                init_X -= 1
                value -= 1
            else:
                set_list[init_X][init_Y] = value
                init_X += 1
                value += 1
#-------向左走
        while direction == "W":
            if init_Y < count - 1:
                direction = "N"
                init_Y += 1
                value -= 1
            else:
                set_list[init_X][init_Y] = value
                init_Y -= 1
                value += 1
#-------向上走
        while direction == "N":
            if init_X < count:
                direction = "E"
                init_X += 1
                value -= 1
            else:
                set_list[init_X][init_Y] = value
                init_X -= 1
                value += 1
#-------循环控制条件
        if count < pow(num, 2):
            count += 1
        else:
#-------格式化打印输出
            for result_X in set_list:
                for result_Y in result_X:
                    print "%3s" %(result_Y),
                print
            break
#############################################
#-------函数调用
num_set(4)
