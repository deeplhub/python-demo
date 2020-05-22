"""
Title: 日志
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/09
"""
import logging
import sys

DEFAULT_FORMATTER = "%(asctime)s [%(threadName)s] - [%(levelname)s] %(filename)s:%(lineno)d [%(funcName)s()] : %(message)s"
# DEFAULT_FORMATTER = "[%(levelname)s] %(filename)s:%(lineno)d [%(funcName)s()] : %(message)s"
FILE_PATH = "D:/test.log"


class LogUtils():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, loggerName):
        # 创建一个logging对象，如果参数为空则返回root logger
        self.__logger = logging.getLogger(loggerName)
        # 指定日志的最低输出级别，默认为warn级别
        self.__logger.setLevel(logging.DEBUG)
        self.__console_log()
        self.__file_log()

    def __console_log(self):
        # 创建日志输出格式
        formatter = logging.Formatter(DEFAULT_FORMATTER)
        # 控制台日志
        #     console_handler = logging.StreamHandler(sys.stdout)
        console_handler = logging.StreamHandler(sys.stderr)
        # console_handler.formatter = formatter
        console_handler.setFormatter(formatter)
        # 为logger添加的日志处理器
        self.__logger.addHandler(console_handler)
        # 指定控制台日志级别
        console_handler.setLevel(logging.DEBUG)

    def __file_log(self):
        # 创建日志输出格式
        formatter = logging.Formatter(DEFAULT_FORMATTER)
        # 指定输出的文件路径
        file_handler = logging.FileHandler(FILE_PATH, encoding="UTF-8")
        # 设置文件处理器，加载处理器格式
        file_handler.setFormatter(formatter)
        # 为logger添加的日志处理器
        self.__logger.addHandler(file_handler)
        # 指定日志文件级别
        file_handler.setLevel(logging.WARNING)

    def log(self):
        return self.__logger


if __name__ == '__main__':
    log1 = LogUtils("A").log()
    log1.info("AAAAAAAAAAAAAAAAAa")

    log2 = LogUtils("B").log()
    log2.info("BBBBBBBBBBBBBBBBB")

    log3 = LogUtils("C").log()
    log3.info("CCCCCCCCCCCCCCCCC")
