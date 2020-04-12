'''
Title: 单例模式
Description: 
__new__和__init__是很容易搞混的

在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法

__new__和__init__魔法函数区别（两个魔法函数是最容易混淆，面试官也经常会问到的知识点）：
    - __new__是在__init__之前执行
    - new的功能是在生成对象之前所做的动作，接受的参数是cls 类
    - init是在对象生成之后完善对象的属性 它接受的是self 对象
    - 对象生成是在 new 里面 return （返回一个对象）

__new__() 方法的特性：
    - __new__() 方法是在类准备将自身实例化时调用。
    - __new__() 方法始终都是类的静态方法，即使没有被加上静态方法装饰器
    
类的私有属性： __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时  self.__private_attrs。

Python中self和cls的区别：
    self：表示一个具体的实例本身。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。
    cls：表示这个类本身。类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self,即self是__new__的返回值
    

实现单例模式的几种方式：
    - 使用模块：
        -- Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
        -- 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
    - 使用装饰器
    - 使用类
    - 基于__new__方法实现（推荐使用，方便）


参考地址：
    https://blog.csdn.net/qq_34979346/article/details/83744950?depth_1-utm_source=distribute.pc_relevant.none-task
    https://www.cnblogs.com/chvv/p/9950837.html
    

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''

class Singleton:
    
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __instance = None
    
    # __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
    # __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
    # __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
    def __new__(cls, *args, **kwargs):
        print("new...")
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, num):
        print("init...")
        self.num = num

        
s1 = Singleton(10)
s2 = Singleton(20)
print(s1 == s2)
print(s1 is s2)

