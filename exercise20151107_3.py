#!/usr/bin/env python
# coding: utf-8
### exercise20151107_3.py
"""
使用sqlalchemy连接数据库，ORM模式。可移植性好，推荐使用
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

db = create_engine("mysql://www:123456@localhost") #初始化数据库连接
db.execute("use conference")    #使用conference库
Base = declarative_base()   #声明映射，创建对象的基类

class User(Base):   #定义User对象
    __tablename__ = 'users' #指定表名，users映射为User
    #指定数据库表结构
    user_id = Column(Integer, primary_key = True)   #指定为主键
    name = Column(String(49))
    fullname = Column(String(40))
    password = Column(String(40))
    
    # 调试，方便最后打印回显
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" %(self.name, self.fullname, self.password)

Base.metadata.create_all(db)    #在会话中创建数据库表（上面指定的格式）
user = User(name='dc', fullname='DengChao', password='iampassword') #指定数据
print user.name
Session = sessionmaker(bind=db) #绑定到连接服务，创建Session类型
session = Session() #初始化会话，创建session对象
session.add(user)   #添加数据
session.commit()    #提交数据，刷新写入（实时生效）
user = session.query(User).filter(User.user_id==1).one()    #创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
print user.name
print user
session.close() #关闭session
