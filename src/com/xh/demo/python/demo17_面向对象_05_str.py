'''
Title: 打印类信息
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Student:

    def __init__(self, name):
        print("__init__")
        self.name = name
        pass
    
    #  当我们在调用print(类)时,系统会先查找__str__或者__repr__方法,如果有这两种方法的一个,则打印方法返回的值.
    def __str__(self):
        return self.name + ", " + str(id(self))
    
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")


# 创建对象
s1 = Student('张三')
s1.eat()
s1.gotoClass()  

# 这里触发调用 __str__
print(s1)     
