"""
Title: bean工厂
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/3/23
"""
import importlib
import os

from src.com.xh.demo.ioc import cons


class BeanFactory():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        cur_path = os.path.abspath(os.path.dirname(__file__))
        assert cons.PROJECT_NAME is not None, "未知的项目名称"
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
                    self.__beanResource[index] = filepath

    def __init(self):
        """
        @note: 初始化
        """
        for key, value in self.__beanResource.items():
            if str(value) == self.__root_path:
                continue
            pkg = self.__getPackage(key, value)
            # 绝对导入
            importlib.import_module(pkg)

    def __getPackage(self, key, value):
        """
        @note: 扫描包
        @param key: 文件名
        @param value: 文件路径
        """
        pkg = value.replace(self.__root_path + "\\", "").replace('\\', '.')
        if not pkg.endswith('.'):
            pkg = pkg + "."
        return pkg + key.replace('.py', '')
