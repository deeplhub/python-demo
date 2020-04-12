'''
Title: 反射
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/11
'''
import importlib

import importlib
import time
#
# pkg = "other.demo_test"
# obj = importlib.import_module(pkg)
# obj.Demo().my_print()

# package = __import__(pkg)
# temp_class = getattr(package, 'b')
# temp = temp_class()  # b()

# globals()['Demo']()

# module_name = "other.demo_test"
# def fun1():
#     # 使用__import__来实现动态加载
#     module1 = __import__(module_name)
#     module1.Demo()
#
#
# def fun2():
#     # 使用importlib，importlib相比__import__()，操作更简单、灵活，支持reload()
#     class_name = "Demo"
#     test_module = importlib.import_module(module_name)
#     # 使用getattr()获取模块中的类
#     test_class = getattr(test_module, class_name)
#     # 动态加载类test_class生成类对象
#     test_class()
#     test_obj.test()


def fun1():
    module_name = "other.demo_test"
    # 使用importlib，importlib相比__import__()，操作更简单、灵活，支持reload()
    class_name = "Demo"
    test_module = importlib.import_module(module_name)
    # 使用getattr()获取模块中的类
    test_class = getattr(test_module, class_name)
    # 动态加载类test_class生成类对象
    test_class()


#     test_obj.test()


if __name__ == '__main__':
    fun1()
