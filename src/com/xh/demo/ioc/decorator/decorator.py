"""
Title: 注册服务
Description:

@author H.Yang
@email xhaimail@163.com
@date 2020/3/23
"""
from src.com.xh.demo.ioc.factory.application_context import ApplicationContext

__registry = None


def __registry_service():
    """
    :note: 初始化
    :return:
    """
    global __registry
    if not __registry:
        __registry = ApplicationContext()
    return __registry


def service(cls):
    """
    注册类
    :param cls: 当前对象
    :return:
    """
    __registry_service().register(cls)
    return cls


def service_name(name):
    """
    注册类
    :param name: 当前名称
    :return:
    """
    def inner_service(cls):
        __registry_service().register(cls, name=name)
        return cls

    return inner_service