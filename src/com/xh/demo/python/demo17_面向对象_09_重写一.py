'''
Title: 重写
Description: 

在子类中访问父类被重写的方法
    格式一：父类名.方法名(对象)
    格式二：super(本类名,对象).方法名（）
    格式三(推荐)：super().方法名（）

多继承关系中，当多个父类具有同名的成员，子类调时该成员时先调用继承关系中的第一个声明的类的成员

参考地址：
    https://www.cnblogs.com/sickle/p/10115734.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''

print("单继承重写")

class Anaimal:

    def shout(self):
        print('Animal')


class Cat(Anaimal):

    def shout(self):
        # 以下是对父类方法的调用，任选其一
        # super(Cat, self).shout()
        super().shout()
        
        print('miao')


# a = Anaimal()
# a.shout()
c = Cat()
c.shout()

print("\n#############################\n")

print("多继承重写")


class Father:

    def shout(self):
        print("Father...")


class Mother:

    def shout(self):
        print("Mother...")


# 多继承关系中，当多个父类具有同名的成员，子类调时该成员时先调用继承关系中的第一个声明的类的成员
class Son(Father, Mother):

    def s1(self):
        print("Son...")


print("== 重写一 ==")
son = Son()
son.shout()  
son.s1()
# 使用Python内置属性__mro__可以查看继承关系
print(Son.__mro__)

