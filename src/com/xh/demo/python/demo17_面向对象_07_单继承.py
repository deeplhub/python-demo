'''
Title: 单继承
Description: 
继承表达式：class Cat(Anaimal),继承可以让子类从父类获取特征（属性和方法）

注意：
    使用print(son.f1())会多输出一个None，而你打印出none的原因是因为在类的方法中直接打印了字符串（def my.f1(self)）没有返回值, 将方法中的pring改成return即可
    子类可以添加父类没有的成员
    父类私有成员不可被继承
    
super是一个类，这里调用会绑定当前类和该类的实例
    
　　

参考地址：
    https://www.runoob.com/python3/python3-class.html
    https://www.runoob.com/w3cnote/python-extends-init.html
    https://www.cnblogs.com/JerryZao/p/9657055.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Father:
    
    def __init__(self):
        print("Father...")
    
    def f1(self):
        print("I am a father")

    def f2(self):
        return "I am a father"


class Son(Father):
    
    def __init__(self):
        # 以下是调用父类的构造函数，任选其一
        # Father.__init__(self)
        super(Son, self).__init__()
        
        # super是一个类，这里调用会绑定汪前类该类的实例
        # super().f1()
    
    def s1(self):
        print("Son.s1")
        print(self.f2())


print("单继承")
son = Son()
print(son.s1())
print()
print(son.f2())
# print(son.f2())
