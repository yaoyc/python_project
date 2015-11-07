#!/usr/bin/env python
# coding: utf-8
### exercise20151107_2.py
"""
使用sqlalchemy连接数据库，SQL语句模式。可移植性差，不推崇使用
"""

from sqlalchemy import *

#连接数据库
db = create_engine("mysql://python:123456@192.168.119.160")
db.execute("use conference")    #指定使用conference库，没有则需要先创建
db.echo = False
metadata = MetaData(db)

#表内容
users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String(40)),
    )
users.create()  #创建表
i = users.insert()
i.execute(name='Mary', age=30, password='secret')
i.execute(
    {'name':'John', 'age':42},
    {'name':'Susan','age':57},
    {'name':'Carl', 'age':33}
    )

s = users.select()  #()内没有数据，查询所有
rs = s.execute()
row = rs.fetchone() #取出一个
print 'Id:', row[0]

print 'Name:', row['name']
print 'Age:' , row.age
print 'password:', row[users.c.password]

for row in rs:
    print row.name, 'is', row.age, 'years old'
