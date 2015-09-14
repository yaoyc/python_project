# coding:utf-8
###########################################################
### 链表反转 ### Python 有[::-1]和reverse()命令直接反转 ###
###########################################################
init_list = [1, 2, 3, 4, 5]
for i in xrange(len(init_list)):
	init_list.insert(i, init_list.pop(-1))
print init_list
