# coding:utf-8
#####################################################
### 石头-剪刀-布 游戏 ###############################
#####################################################
import random

def pc_choice():
    random_number = random.randint(1,3)
    return random_number
    
def compare(x,y):
    result = x - y
    if x == 1:
        if result == -1: print "你输了"
        elif result == -2: print "你赢了"
        else: print "平手"
    elif x == 2:
        if result == 1: print "你赢了"
        elif result == -1: print "你输了"
        else: print "平手"
    else:
        if result == 2: print "你输了"
        elif result == 1: print "你赢了"
        else: print "平手"

CMD_demo = {
1: "剪刀",
2: "石头",
3: "布"}

def showmenu():
    user_IN = '''
***请按以下提示输入选项***
1: 剪刀
2: 石头
3: 布
0: 退出游戏

Enter choice:'''
    while True:
        while True:
            pc_choice_tmp = pc_choice()
            try:
                user_input = int(raw_input(user_IN).strip())
            except (EOFError, KeyboardInterrupt, ValueError):
                user_input = 0
        
            if str(user_input) not in "0123":
                print "输入错误，重新输入"
            else:
                break
        if user_input == 0:
            break
        else:
            print '''\
系统输出的是： {0}
用户输出的是： {1}'''.format(CMD_demo[pc_choice_tmp],CMD_demo[user_input])

        compare(user_input,pc_choice_tmp)

if __name__ == "__main__":
    showmenu()
