"""
Title: bean工厂
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/3/23
"""
import importlib
import os
from src.com.taiping.constants import cons
from src.com.taiping.utils.log import LogUtils

log = LogUtils("BeanFactory").getLog()


class BeanFactory():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        log.debug("BeanFactory init...")
        cur_path = os.path.abspath(os.path.dirname(__file__))
        self.__root_path = cur_path[:cur_path.find(cons.PROJECT_NAME) + len(cons.PROJECT_NAME)]  # 获取myProject，也就是项目的根路径
        self.__beanResource = dict()
        self.__context = dict()
        self.__scan(self.__root_path)
        self.__init()

    def __scan(self, filepath):
        # listdir: 返回path所有目录及文件列表，包括子目录
        file_names = os.listdir(filepath)
        for index in file_names:
            # join: 把目录和文件名合成一个路径
            file = os.path.join(filepath, index)
            # isdir: 判断路径是否为目录
            if os.path.isdir(file):
                self.__scan(file)
            else:
                if ("__pycache__" not in filepath) and ("." not in filepath) and not str(index).endswith(
                        '__init__.py') and (".py" in index):
                    # 把路径转换包路径形式
                    pkg = self.__getPackage(index, filepath)
                    self.__beanResource[pkg] = index
                #
            #
        #

    def __init(self):
        """
        @note: 初始化
        """
        for key, value in self.__beanResource.items():
            if str(key) == self.__root_path:
                continue
            # 绝对导入
            log.debug(key)
            importlib.import_module(key)
        #

    def __getPackage(self, key, value):
        """
        @note: 扫描包
        @param key: 文件名
        @param value: 文件路径
        """
        pkg = value.replace(self.__root_path + "\\", "").replace('\\', '.')
        if not pkg.endswith('.'):
            pkg = pkg + "."
        #
        return pkg + key.replace('.py', '')
