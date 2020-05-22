'''
Title: mysql_sqlalchemy
Description: 

SQLAlchemy本身无法操作数据库，其必须通过pymysql等第三方插件

使用sqlalchemy进行数据库操作，首先我们需要建立一个指定数据库的链接引擎对象，而建立引擎对象的方式被封装在了sqlalchemy.create_engine函数中，通过指定的数据库连接信息即可创建

create_engine()：用来初始化数据库连接。格式：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'。
示例：初始化数据库链接：
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
    我使用了mysql数据库，数据库连接框架用的是mysqlconnector，用户名为root，密码是123456，端口号是localhost（127.0.0.1），端口号是3306（mysql服务器默认端口号），test是数据库的名字。

参考地址：
    https://www.jianshu.com/p/0ad18fdd7eed
    https://www.jianshu.com/p/3942d4d1a7c5
    https://www.cnblogs.com/wj-1314/p/10627828.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative.api import declarative_base
from src.com.xh.demo.utils.json import JsonUtils

# 生成orm基类

base = declarative_base()


class Student(base):
    __tablename__ = "student"  # 表名
    __table_args__ = {
        # 'schema': 'Code'    #数据库架构名
        'mysql_charset': 'utf8'
    }

    # 表结构
    sid = Column(Integer, primary_key=True, name="sid")
    name = Column(String(50), name="name")

    # 构造方法
    def __init__(self):
        pass

    def set(self, sid, name):
        self.sid = sid
        self.name = name

    # 非实例化方法
    @classmethod
    def columns(cls):
        # print(cls.__name__)
        return set('sid name'.split())


# 1. 创建连接
# demo: mysql+pymysql：//username+password@host:prot/databas
url = 'mysql+pymysql://root:admini@localhost:3306/test?charset=utf8'
engine = create_engine(
    url,
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
    pool_timeout=30  # 池中没有线程最多等待的时间，否则报错
)
# 创建表结构,已存在表则无需执行
# base.metadata.create_all(engine)  

# 2. 创建与数据库的会话, class, 不是实例
print("== 实现方式(一) ==")
# 使用thread local storage技术, 使 session 线程隔离
SessionFactory = sessionmaker(bind=engine)
# 生成session实例, 单例模式, 与线程绑定
session = scoped_session(SessionFactory)

# # print("== 实现方式(二) ==")
# Session = sessionmaker(bind=engine)
# # 生成session实例, 每次生成一个新的
# session = Session() 

# 3. add
# stu = Student(1, "abc")
# # 把要创建的数据对象添加到这个session里 
# session.add(stu)
# # 提交，使前面修改的数据生效
# session.commit()
# print("add OK")

# 4.1 查询所有
stu = session.query(Student).all()
for row in stu:
    print("type(row)", type(row))
    print(row.sid, row.name)
    jsonStr = JsonUtils.to_json_string(row)
    print("jsonStr", jsonStr)
    print("type(jsonStr)", type(jsonStr))

    dict2 = JsonUtils.to_object(Student(), jsonStr)
    print("type(dict2)", type(dict2))
    print(dict2.name)

# 4.2. query one    
row = session.query(Student).filter(Student.sid == 2).first()
print("query one:", JsonUtils.to_json_string(row))
print("\n\n")

# 4.3. update
row.name = 'sfd'
session.commit()
print("update OK")
print("\n\n")

# 4.4. delete
# session.query(Student).filter(Student.sid == 2).delete()
# session.commit()
# print("delete OK")

# 将连接交还给连接池
try:
    session.remove()
    print("== 实现方式(一) ==")
except:
    print("== 实现方式(二) ==")
    session.close()
