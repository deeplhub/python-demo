'''
Title: 多继承
Description: 
    一个类同时继承多个类，称为多继承
    多继承关系中，当多个父类具有同名的成员，子类调时该成员时先调用继承关系中的第一个声明的类的成员

参考地址：
    https://www.cnblogs.com/sickle/p/10115734.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Father:

    def f(self):
        print("Father.f ...")


class Mother:

    def m(self):
        print("Mother.m ...")


class Son(Father, Mother):

    def s(self):
        print("Son.s ...")
    
    # 子类调用父类
    def s2(self):
        # 方法一：
        self.f()
        self.m()
        print()
        # 方法二：
        Father.f(self)
        Mother.m(self)


print("== 多继承 ==")
son = Son()
son.f()   
son.m()  
son.s()
print()
print()
son.s2()
