'''
Title: 面向对象
Description: 

在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法

类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用

self代表类的实例，而非类。类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''


class Student:

    def  __init__(self):
        print("初始化构造方法")
        
    def eat(self):
        print("eat.....")
        
    def gotoClass(self):
        print("go to class...")

# 创建对象 
stu1 = Student()
stu1.eat()
stu1.eat()

stu2 = Student()
stu2.eat()
stu2.eat()

# ==和is操作的区别是：
#     a. Is:比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。
#     b. ==:比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。
print(stu1 == stu2)
print(stu1 is stu2)
print(id(stu1) == id(stu2))

# 赋值
stu1.name = "ABC"
stu1.age = 12
print(stu1.name)
print(stu1.age)
