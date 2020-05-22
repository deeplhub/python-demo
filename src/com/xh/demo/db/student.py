"""
Title: 
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Student(base):
    # 指定数据库表名
    __tablename__ = "student"

    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    id = Column(Integer, primary_key=True, name="id")
    name = Column(String, name="name")
    sex = Column(String, name="sex")
    age = Column(Integer, name="age")
