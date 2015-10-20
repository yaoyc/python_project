#!/usr/bin/env python
#coding:utf-8
### exercise20151019_1.py
'''
一个螺旋数字矩阵，由外向里旋转
输入一个数字n，打印出如下数字：
  1   2   3   4   5   6
 20  21  22  23  24   7
 19  32  33  34  25   8
 18  31  36  35  26   9
 17  30  29  28  27  10
 16  15  14  13  12  11
这是输入6的情况。
'''

def num_set(num):
    set_list = [[0]*num for i in xrange(num)]   #矩阵模板
    init_Y = 0    #Y轴，行
    init_X = 0    #X轴，列
    value = 1       #初始值
    count = 1       #初始圈数
#---direction = ("E", "S", "W", "N")
#---方向操作    右、下、左、上
    direction = "E"     #初始化执行方向
    while True:
#-------向右走
        while direction == "E":
            set_list[init_X][init_Y] = value
            if init_Y > num - count - 1:
                direction = "S"
                continue
            else:
                init_Y += 1
                value += 1

#-------向下走
        while direction == "S":
            set_list[init_X][init_Y] = value
            if init_X > num - count - 1:
                direction = "W"
                continue
            else:
                init_X += 1
                value += 1

#-------向左走
        while direction == "W":
            set_list[init_X][init_Y] = value
            if init_Y < count:
                direction = "N"
                continue
            else:
                init_Y -= 1
                value += 1

#-------向上走
        while direction == "N":
            set_list[init_X][init_Y] = value
            if init_X < count + 1:
                direction = "E"
                continue
            else:
                init_X -= 1
                value += 1

#-------循环控制条件
        if value < pow(num, 2):
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
if __name__ == '__main__':
    for i in xrange(3,11,1):
        num_set(i)
        print
#num_set(5)
