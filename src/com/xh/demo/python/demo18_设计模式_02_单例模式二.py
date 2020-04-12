'''
Title: 
Description: 

实现单例模式的几种方式：
    - 使用模块：
        -- Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
        -- 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
    - 使用装饰器，使用 @<单例类 > 的方式创建单例
    - 基于__new__方法实现（推荐使用，方便）
    - 基于metaclass方式实现，又称：元类 metaclass

    
参考地址：
    - https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_0
    - https://blog.csdn.net/qq_41359051/article/details/91469933
    - https://www.cnblogs.com/xiao-apple36/p/9398760.html#_label1_5

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''
import threading

print("实例1：使用模块")
class Singleton1(object):

    def foo(self):
        print("使用模块")


singleton1 = Singleton1()

# 将上面的代码保存在文件 xx.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# 使用示例（新建一个文件，贴入一下代码）：
# from demo.demo18_设计模式_02_单例模式二 import singleton1
# 
# obj1 = singleton1.foo()
# obj2 = singleton1.foo()
# print(obj1 == obj2)
# print(obj1 is obj2)

print("\n#########################\n")

print("实例2：使用装饰器")


def Singleton2(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton2
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1 == a2)
print(a1 is a2)

print("\n#########################\n")

print("实例3：基于__new__方法实现（推荐使用，方便）")
print("单线程")


class Singleton3(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


# 示例：
obj1 = Singleton3()
obj2 = Singleton3()
print(obj1 == obj2)
print(obj1 is obj2)

print("\n#########################\n")
print("多线程")


class SingletonThread3(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonThread3, "_instance"):
            with SingletonThread3._instance_lock:
                if not hasattr(SingletonThread3, "_instance"):
                    SingletonThread3._instance = object.__new__(cls)  
        return SingletonThread3._instance


obj1 = SingletonThread3()
obj2 = SingletonThread3()
print(obj1 == obj2)
print(obj1 is obj2)


# 验证用例
def task(arg):
    obj = SingletonThread3()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

print("\n#########################\n")

print("实例4：基于metaclass方式实现，又称：元类 metaclass")


class SigletonMetaClass(type):
    _instance = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)  # 断点1
    
    # __call__主要实现的是将类的对象当作函数直接调用
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance  # 断点2


class Singleton4(metaclass=SigletonMetaClass):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # 断点3


obj1 = Singleton4()
obj2 = Singleton4()
print(obj1 == obj2)
print(obj1 is obj2)
