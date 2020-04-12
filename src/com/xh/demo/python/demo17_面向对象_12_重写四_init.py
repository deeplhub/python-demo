'''
Title: 重写 init
Description: 

类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用

重写__init__方法：
    格式一：super(子类，self).__init__(参数1，参数2，....)
    格式二：父类名称.__init__(self,参数1，参数2，...)


参考地址：
    https://www.runoob.com/w3cnote/python-extends-init.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Father:

    def __init__(self, name):
        print("Father.f1 ...")
        self.name = name


class Son(Father):

    def __init__(self, name, age):
        print("Son.f2 ...")
        Father.__init__(self, name)
        self.age = age

        
print("== 重写四, 重写 __init__ ==")
son = Son('张三', 30)
print(son.age, son.name)    
