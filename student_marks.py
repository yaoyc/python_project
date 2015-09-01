#coding:utf-8

student_marks = {
'tom':{'yuwen':80,'shuxue':89,'english':87},
'dennis':{'yuwen':90,'shuxue':78,'english':89},
'jack':{'yuwen':79,'shuxue':96,'english':99}}

def sum_marks(chengjidan,kemu):
	sum = 0
	for chengji in chengjidan.values():
		sum += chengji[kemu]
	return sum

def max_marks(chengjidan,kemu):
	a_list = []
	for chengji in chengjidan.values():
		a_list.append(chengji[kemu])
	return max(a_list)

def min_marks(chengjidan,kemu):
	a_list = []
	for chengji in chengjidan.values():
		a_list.append(chengji[kemu])
	return min(a_list)

def avg_marks(chengjidan,kemu):
	return sum_marks(chengjidan,kemu) / len(chengjidan)

if __name__ == '__main__':
	print sum_marks(student_marks,'yuwen')
