'''
Title: Python3 __call__方法
Description: 

Python3 __call__方法
关于 __call__ 方法，不得不先提到一个概念，就是可调用对象（callable），我们平时自定义的函数、内置函数和类都属于可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable。如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象，

__call__ 方法是 Python 类中一个非常特殊的实例方法，即 __call__()。可以让类的实例的行为表现的像函数一样
该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。主要实现的是将类的对象当作函数直接调用。



    
参考地址：
    - https://www.cnblogs.com/SBJBA/p/11355412.html
    - http://c.biancheng.net/view/2380.html
    - https://www.jianshu.com/p/e1d95c4e1697


@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''

print("实例1：")
# 主要实现的是将类的对象当作函数直接调用， 需要注意的是：只有当在类中定义了 def __call__() 方法后，才可以实现这个功能，否则会出现语法错误，就是文档中解释的 if this method is defined 的意思。
class Demo(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_print(self,):
        print("a = ", self.a, "b = ", self.b)

    def __call__(self, *args, **kwargs):
        self.a = args[0]
        self.b = args[1]
        print("call: a = ", self.a, ", b = ", self.b)


demo = Demo(10, 20)
demo.my_print()

demo(50, 60)

print("\n#############################\n")
print("实例2：")


class CLanguage:

    # 定义__call__方法
    def __call__(self, name, add):
        print("调用__call__()方法", name, add)


clangs = CLanguage()
clangs("C语言中文网", "http://c.biancheng.net")

print("\n#############################\n")
print("实例3：")


class Entity:
    '''调用实体来改变实体的位置。'''
    
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size
    
    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = x, y


e = Entity(1, 2, 3)  # 创建实例
print(e.size)
print(e.y)
print(e.y)
print()

e(4, 5)  # 实例可以象函数那样执行，并传入x y值，修改对象的x y 
print(e.size)
print(e.x)
print(e.y)

print("\n#############################\n")
print("实例4：")


def say():
    print("Python教程：http://c.biancheng.net/python")

say()
say.__call__()
