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


def Service(cls):
    """
    :note: 注册类
    :param cls:
    :return:
    """
    __registry_service().registerService(cls)
    return cls

def ServiceName(name):
    def inner_service(cls):
        __registry_service().registerService(cls, serviceName=name)
        return cls

    return inner_service

def Transaction():
    pass