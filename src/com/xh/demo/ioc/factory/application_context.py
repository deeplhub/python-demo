'''
Title: 程序应用环境初始化配置
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/12
'''
import inspect

from src.com.xh.demo.ioc.factory.bean_factory import BeanFactory
from src.com.xh.demo.utils.log import LogUtils

log = LogUtils("ApplicationContext").log()


class ApplicationContext():
    __instance = None

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__registry = {}  # dict 在单例中初始化
        return cls.__instance

    def init_factory(self):
        log.debug("ApplicationContext init_factory...")
        BeanFactory()

    def register(self, clazz, name=None, overwrite=False):
        """
        创建服务名称
        :param clazz: 注册类
        :param name: 服务名
        :param overwrite:
        :return:
        """
        if not name:
            service_name = self.__make(clazz.__name__)
        else:
            service_name = self.__make(name)

        # Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
        assert (overwrite or service_name not in self.__registry or clazz == self.__registry[service_name]), (
                u"Service named %s already registered with different type" % (service_name,))

        log.debug("Create %s service." % service_name)
        self.__registry[service_name] = clazz()

    def __make(self, class_name):
        """
        生成服务名
        :param class_name: 类名称
        :return:
        """
        return class_name[:1].lower() + class_name[1:]

    def get(self, service):
        """
        获取服务
        :param service: 服务名称
        :return:
        """
        if inspect.isclass(service):
            service_name = self.__make(service.__name__)
        else:
            service_name = self.__make(service)

        if service_name not in self.__registry:
            raise Exception('Service %s is not registered. Cannot create instance' % service_name)

        log.debug("get %s service." % service_name)
        return self.__registry[service_name]
