#!/usr/bin/env python
# coding:utf-8
### 图书馆系统
### 添加书籍、删除书籍、查询书库、查询用户借阅、借阅书籍(后续将完善书架)
### library_sys.py

class library(object):
	def __init__(self):
		self.SN_dict = {123:'python', 234:'python'}	#唯一性SN编号与书名
		self.persion_dict = {'zhangsan':[123, 234]}	#借阅者与借阅列表

	def add_book(self, sn, new_book):	#添加书籍
		self.SN_dict[sn] = new_book
	
	def del_book(self, old_sn):	#删除书籍
		self.SN_dict.pop(old_sn)
	
	def find_book(self, index):	#查询书库，按索引条件
		if isinstance(index, int) == True:	#按 SN编号 查找
			if index not in self.SN_dict.keys():
				return "SN编号不存在"
			result = self.SN_dict[index]
			return "SN编号:{0} 对应的书籍为:《{1}》".format(index, result)
		book_num = self.SN_dict.values().count(index)	#按 书名 查找
		if book_num == 0:
			return "没有《{0}》".format(index)
		else:
			tmp_sn = []
			for key,value in self.SN_dict.iteritems():	#根据书名 搜索 SN编号
				if value == index:
					tmp_sn.append(key)
			return "《{0}》对应的所有SN编号列表为:{1}".format(index, tmp_sn)

	def find_user(self, name):	#查询用户借阅书籍
		if (name in self.persion_dict.keys()) == True:
			tmp_sn_book = {}
			tmp_sn = self.persion_dict[name]
			for sn in tmp_sn:
				tmp_sn_book[sn] = self.SN_dict[sn]
			return "{0} 已借阅 {1}".format(name, tmp_sn_book)
		return "{0} 没有借书"
	
	def borrow_book(self, sn, name):	#借阅书籍
		self.persion_dict[name].append(sn)
		tmp_sn_book = {}
		tmp_sn_book[sn] = self.SN_dict[sn]
		return "{0} 成功借阅《{1}》".format(name, tmp_sn_book)

print library().find_book("python")
print library().find_user("zhangsan")
library().add_book(1234,'shell')
print library().find_book(123)
