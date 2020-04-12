"""
Title: 
Description: 

Sqlalchemy官网：https://docs.sqlalchemy.org/en/13/

session.close()与session.remove()区别：
1. session.close() 只是释放对表的控制权，并不是断开连接(connect)，所以close() 之后依然可以执行查询。
2. 使用scoped_session() 之后获得的session，如果不执行session.remove(),所获得的session都是同一个session。
    session.remove() 并不会，执行close()，所以正常的顺序应该是
        session = scoped_session(session_factory)
        s1 = session()
        s1.add(jessica)
        s1.commit()
        s1.close()
        session.remove()
    如果没有执行 session.remove() 不需要执行 s1.close()，应为同一个 session不需要释放，就可以提交。

    参考地址：http://rhel.cc/2016/07/14/sqlalchemy-session/


参考地址：
    sqlalchemy 学习
        https://www.jianshu.com/p/a33f48387efa
        https://segmentfault.com/a/1190000016767008
        https://www.cnblogs.com/runshulan/p/11606231.html
        https://www.cnblogs.com/lsdb/p/9835894.html
        https://www.cnblogs.com/ybjourney/p/11832045.html
    
    SQlALchemy session详解
        https://zhuanlan.zhihu.com/p/92233555
    
    SQlALchemy 打印SQLy语句
        https://blog.csdn.net/mrqingyu/article/details/82683744

    SQL各种复杂条件查询及关键字用法
        https://www.jianshu.com/p/196b7892cf38
        https://blog.csdn.net/u013027996/article/details/27083565
        https://juejin.im/post/5bf741886fb9a049fa0f671e
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
"""
from sqlalchemy import exists
from sqlalchemy.engine import create_engine
import threading
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
import traceback

from src.com.xh.demo.utils.log import LogUtils

thread_local = threading.local()
log = LogUtils("DatabaseDao").getLog()

DB_MASTER_URL = "mysql+pymysql://root:admini@127.0.0.1:3306/test?charset=utf8mb4"


class Database():
    __instance = None

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        """初始化变量"""
        self.engine = None

    def init(self):
        """初始化方法"""
        self.createEngine(DB_MASTER_URL, 0, 30, 30)
        if self.engine is not None:
            log.info("Database init OK!")

    def createEngine(self, db_master_url, max_overflow, pool_size, pool_timeout, echo=False):
        """
        初始化数据库连接
        :param db_master_url: 数据库地址
        :param max_overflow: 超过连接池大小外最多创建的连接
        :param pool_size: 连接池大小
        :param pool_timeout: 池中没有线程最多等待的时间，否则报错
        :param echo: echo=True 打印SQLy语句
        :return:
        """
        self.engine = create_engine(
            db_master_url,
            max_overflow=max_overflow,
            pool_size=pool_size,
            pool_timeout=pool_timeout,
            echo=echo
        )

    def createSession(self):
        """创建session，并绑定线程"""
        try:
            if self.engine is None:
                self.init()

            if hasattr(thread_local, "session"):
                session = thread_local.session
                return session

            # 使用thread local storage技术, 使 session 线程隔离
            SessionFactory = sessionmaker(bind=self.engine)
            # 生成session实例, 单例模式, 与线程绑定
            session = scoped_session(SessionFactory)
            thread_local.session = session
            return session
        except Exception as ex:
            log.error("创建 session 异常！")
            raise ex
        finally:
            log.debug("Create session：" + str(id(session)))

    def destroySession(self):
        """释放连接，交还连接池"""
        if not hasattr(thread_local, "session"):
            return
        #
        session = thread_local.session
        # 将连接交还给连接池
        if session != None:
            # session.close() 只是释放对表的控制权，但不是断开连接
            # session.remove() 不会执行close()
            # 详情参考顶部
            session.remove()
            log.debug("Destroy session：" + str(id(session)))
        #

    def load(self, clazz, *args):
        """
        查询数据
        @param clazz: 实体类
        @param args: 查询条件（dict）
        @return: 返回列表
        """
        try:
            # 执行查询
            return self.createSession().query(clazz).filter(*args).all()
        except Exception as ex:
            log.error("load 查询数据异常！")
            raise traceback.format_exc()
        finally:
            self.destroySession()

    def getByField(self, clazz, *args):
        """
        @note: 单条查询
        @param clazz: 实体类
        @param args: 查询条件（dict）
        @return: 返回实体
        """
        try:
            return self.createSession().query(clazz).filter(*args).first()
        except Exception as ex:
            log.error("getByField 查询数据异常！")
            raise ex
        finally:
            self.destroySession()

    def exists(self, clazz, *args):
        """
        @note: 判断数据是否存在
        :param args:
        :return: 返回的结果是True或False
        """
        try:
            session = self.createSession()
            return session.query(session.query(clazz).filter(*args).exists()).scalar()
        except Exception as ex:
            log.error(traceback.format_exc())
            raise traceback.format_exc()
        finally:
            self.destroySession()

    def existByField(self, *args):
        """
        @note: 判断数据是否存在
        :param args:
        :return: 返回的结果是True或False
        """
        try:
            return self.createSession().query(exists().where(*args)).scalar()
        except Exception as ex:
            log.error(traceback.format_exc())
            raise ex
        finally:
            self.destroySession()

    def getCount(self, clazz, *args):
        """
        统计数量
        :param clazz: 实体类
        :param args: 条件
        :return: 返回 int 类型
        """
        try:
            session = self.createSession()
            return session.query(clazz).filter(*args).count()
        except Exception as ex:
            log.error("getCount 统计异常")
            raise traceback.format_exc()
        finally:
            self.destroySession()

    def saveOrUpdate(self, obj):
        """
        @note: 保存或更新数据
        @param clazz: 实体类
        """
        try:
            # 保存数据
            self.createSession().add(obj)
        except Exception as ex:
            log.error("保存或更新数据异常！")
            raise traceback.format_exc()

    def batchSaveOrUpdate(self, objs):
        """
        @note: 批量保存或批量更新数据
        @param clazz: 实体类
        """
        try:
            session = self.createSession()
            if len(objs) <= 0:
                return objs

            session.add_all(objs)
        except Exception as ex:
            log.error("批量保存或批量更新数据异常！")
            raise ex

    def delete(self, clazz, *args):
        """
        @note: 删除数据
        @param clazz: 实体类
        @param args: 删除条件（dict）
        """
        try:
            self.createSession().query(clazz).filter(*args).delete()
        except Exception as ex:
            log.error("删除数据异常！")
            raise ex

    def transaction(self):
        """持久化"""
        try:
            self.createSession().commit()
        except Exception as ex:
            self.createSession().rollback()
            raise ex
        finally:
            self.destroySession()
