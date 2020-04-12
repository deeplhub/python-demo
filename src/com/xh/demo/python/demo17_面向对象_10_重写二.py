'''
Title: 重写
Description: 

多继承下的重写运行逻辑，此逻辑一定要弄清楚，多继承关系中，当多个父类具有同名的成员，子类调时该成员时先调用继承关系中的第一个声明的类的成员


@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Father1:

    def f(self):
        print("Father1.f ...")

    def run(self):
        print("Father1.run ...")


class Father2(Father1):

    def f2(self):
        print("Father2.f2 ...")

    def run(self):
        print("Father2.run ...")

        
class Father3:

    def f3(self):
        print("Father3.f3 ...")

    def run(self):
        print("Father3.run ...")


class Son(Father2, Father3):

    def f4(self):
        print("Son.f4 ...")


print("== 重写二 ==")
son = Son()
son.f() 
son.f3()
son.run()
# 打印继承结构
print(Son.__mro__)
