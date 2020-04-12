'''
Title: 方法初始化及实例化时调用
Description: 
__new__和__init__是很容易搞混的

在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写
cls代表当前类

__new__和__init__魔法函数区别（两个魔法函数是最容易混淆，面试官也经常会问到的知识点）：
    - __new__是在__init__之前执行
    - new的功能是在生成对象之前所做的动作，接受的参数是cls 类
    - init是在对象生成之后完善对象的属性 它接受的是self 对象
    - 对象生成是在 new 里面 return （返回一个对象）
    
__new__() 方法的特性：
    - __new__() 方法是在类准备将自身实例化时调用。
    - __new__() 方法始终都是类的静态方法，即使没有被加上静态方法装饰器
    
参考地址：
    https://blog.csdn.net/qq_34979346/article/details/83744950?depth_1-utm_source=distribute.pc_relevant.none-task
    https://www.cnblogs.com/chvv/p/9950837.html
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
class Student:
    def __init__(self, name):
        print("初始化构造方法")
        self.name = name
    
    # 当我们在调用print(类)时,系统会先查找__str__或者__repr__方法,如果有这两种方法的一个,则打印方法返回的值.
    def __str__(self):
        # 返回一个对象的描述信息
        return self.name + ", " + str(id(self))
    
    # 如果要得到当前类的实例，应当在当前类中的 __new__() 方法语句中调用当前类的父类的 __new__() 方法。
    # 例如：如果当前类是直接继承自 object，那当前类的 __new__() 方法返回的对象应该为：object.__new__(cls)
    # __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
    # __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
    # __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
    def __new__(cls, *args, **kwargs):
        print("new...")
        return object.__new__(cls)
    
    def eat(self):
        print("eat.....")
        
    def gotoClass(self):
        print("go to class...")


# 实例化对象是谁取决于__new__方法,__new__返回什么就是什么
print(type(Student("Abc")))
# 创建对象
s1 = Student("Abc")
s1.eat()
s1.gotoClass()
print(s1)
