'''
Title: 定义构造方法
Description: 

    pass 是空语句，是为了保持程序结构的完整性，不做任何事情，一般用做占位语句。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''


class Student:

    # 定义构造方法
    def  __init__(self, name):
        print("初始化构造方法")
        self.name = name
        pass
        
    def eat(self):
        print("eat.....")
        
    def gotoClass(self):
        print("go to class...")

    
# 创建对象
s1 = Student("Abc")
s1.eat()
s1.gotoClass()
print(s1)
