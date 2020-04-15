'''
Title: 程序应用环境初始化配置
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/12
'''
import inspect
import threading

from src.com.xh.demo.ioc.factory.bean_factory import BeanFactory
from src.com.xh.demo.utils.log import LogUtils

log = LogUtils("ApplicationContext").getLog()


class ApplicationContext():
    __instance = None

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__registry = {}  # dict 在单例中初始化
        return cls.__instance

    def initFactory(self):
        log.debug("ApplicationContext init...")
        BeanFactory()

    def registerService(self, serviceClass, serviceName=None, overwrite=False):
        """
        创建服务名称
        """
        if not serviceName:
            serviceName = self.__makeServiceName(serviceClass.__name__)
        else:
            serviceName = self.__makeServiceName(serviceName)

        # Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
        assert (overwrite or serviceName not in self.__registry or serviceClass == self.__registry[serviceName]), (
                u"Service named %s already registered with different type" % (serviceName,))

        log.debug("Create %s service." % serviceName)
        self.__registry[serviceName] = serviceClass()

    def __makeServiceName(self, className):
        """
        生成服务名
        """
        return className[:1].lower() + className[1:]

    def getService(self, service):
        """
        获取服务
        :param service:
        :return:
        """
        if inspect.isclass(service):
            serviceName = self.__makeServiceName(service.__name__)
        else:
            serviceName = self.__makeServiceName(service)

        if serviceName not in self.__registry:
            raise Exception('Service %s is not registered. Cannot create instance' % serviceName)

        log.debug("get %s service." % serviceName)
        return self.__registry[serviceName]
