#coding:utf-8
##########################################################################
### List-Tuple-Dict convert ###
###########################################################################
init_List = ['a', 'b', 'c', 1, 2, 3 ]
init_Tuple = ('one', 'two', 'three', '4', '5', '6')
init_Dict = {
'x': 'bj',
'y': 'cn',
'z': 'hm'}
###########################################################################
def list_con_tuple(x_list = init_List):
	con_tuple = tuple(x_list)
	print "初始化列表: {0}\n转换后元祖: {1}".format(x_list, con_tuple)
	print "-"*50

def tuple_con_list(y_tuple = init_Tuple):
	con_list = list(y_tuple)
	print "初始化元祖: {0}\n转换后列表: {1}".format(y_tuple, con_list)
	print "-"*50

def tuple_list_con_dict(y_tuple = init_Tuple, x_list = init_List):
	con_dict = {}
	try:
		for i in xrange(len(y_tuple)):
			con_dict[y_tuple[i]] = x_list[i]
	except (IndexError):
		print "** 警告！长度不一致，末尾匹配丢失 **"
	print "初始化元祖: {0}\n初始化列表: {1}\n转换后字典: {2}".format(y_tuple, x_list, con_dict)
	print "-"*50

def dict_con_tuple_list(z_dict = init_Dict):
	key_list = []
	value_list = []
	for key in z_dict:
		key_list.append(key)
		value_list.append(z_dict[key])
	con_tuple = tuple(key_list)
	con_list = value_list
	print "初始化字典: {0}\n转换后元祖: {1}\n转换后列表: {2}".format(z_dict, con_tuple, con_list)
	print "-"*50
###########################################################################
rule_choice = {
1: list_con_tuple,
2: tuple_con_list,
3: tuple_list_con_dict,
4: dict_con_tuple_list}

CMDs = {
1: "列表->元祖",
2: "元祖->列表",
3: "元祖+列表->字典",
4: "字典->元祖+列表", }
###########################################################################
def showmenu():
	view = '''*** 列表、元祖、字典相互转换规则 ***
1: 列表->元祖
2: 元祖->列表
3: 元祖+列表->字典
4: 字典->元祖+列表
0: 退出

确认选择: '''
	while True:
		while True:
			try:
				user_input  = int(raw_input(view).strip())
			except (EOFError, KeyboardInterrupt):
				user_input = 0
			if str(user_input) not in "01234":
				print "输入错误，重新输入"
			else:
				break
		if user_input == 0:
			print "用户已退出"
			break
		else:
			print "用户选择的转换规则是：{0}".format(CMDs[user_input])
		rule_choice[user_input]()
###########################################################################
if __name__ == "__main__":
	showmenu()
