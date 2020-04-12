'''
Title: 类的私有和公有方法
Description: 
公有：在类的内外部都可以访问
私有：在类的内部访问
    
如果想获取私有属性，可以给一个调用方法 如：getage 返回 self.__age，或者使用属性装饰器property，从而不需要知道隐藏属性的真是名称，直接访问

在 定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法

类的私有属性： __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时  self.__private_attrs。
类的私有方法 ：__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods

类的方法（公有）：在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数

定义私有方法需要在方法名加上两个下划线，如：__mether(self)

类中下划线使用方式：
    xx：公有变量
    _x：单前置下划线,私有化属性或方法,from somemodule import * 禁止导入,类对象和子类可以访问
    __xx：用于定义私有方法，私有方法无法在外部直接访问(名字重整所以访问不到)
    __xx__：类的专有方法，又称类空间的魔法对象或属性,例如:__init__
    xx_：单后置下划线,用于避免与Python关键词的冲突

参考地址：
    https://blog.csdn.net/u013372487/article/details/51729260?depth_1-utm_source=distribute.pc_relevant.none-task
    https://blog.csdn.net/chuan403082010/article/details/83897234
    https://www.cnblogs.com/huiyichanmian/p/11286339.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''

class Student:
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __privateCount = 0  # 私有变量
    publicCount = 0  # 公开变量
    
    def __init__(self, name):
        print("__init__")
        # 公有
        self.name = name
        
    def setAge(self, age):
        # 私有属性
        self.__age = age
    
    def getAge(self):
        # 私有属性
        return self.__age
    
    # 私有方法
    # 定义私有方法需要在方法名加上两个下划线，如：__mether(self)
    def __foo(self):  
        print('这是私有方法')
    
    def __str__(self):
        return self.name + ", " + str(id(self))
    
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")

        
s1 = Student("张三")
s1.eat()
s1.setAge(20)
print(s1)

print("age : ", s1.getAge())

print(s1.publicCount)
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问私有属性
print(s1._Student__privateCount)

# 报错
# print(s1.age)

