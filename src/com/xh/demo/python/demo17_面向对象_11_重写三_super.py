'''
Title: 重写 super
Description: 
多继承下的重写运行逻辑，此逻辑一定要弄清楚，多继承关系中，当多个父类具有同名的成员，子类调时该成员时先调用继承关系中的第一个声明的类的成员

super是一个类，这里调用会绑定当前类和该类的实例

在子类中访问父类被重写的方法：
    格式一：父类名.方法名(对象)
    格式二：super(本类名,对象).方法名（）
    格式三(推荐)：super().方法名（）
    
参考地址：
    https://www.cnblogs.com/sickle/p/10115734.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Father:

    def shout(self):
        print("Father ...")


class Mother:

    def shout(self):
        print("Mother...")


class Father3(Father, Mother):

    def shout(self):
        print("Father3.shout...")
        super().shout()

        
print("== 重写三 ==")
fa = Father3()
fa.shout()    
