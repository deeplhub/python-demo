'''
Title: 属性和方法
Description: 

方法:
    - 实例方法：使用实例对象访问, 默认使用参数 self, 自动赋值
    - 类方法：使用类对象访问, 默认使用参数 cls, 自动赋值
    - 静态方法：实例对象 & 类对象都可以访问. 可以有参, 也可以无参

Python中self和cls的区别：
    - self：表示一个具体的实例本身。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。
    - cls：表示这个类本身。类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self,即self是__new__的返回值

classmethod： 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。类方法（不需要实例化类就可以被类本身调用），但也可以实例 化后使用
staticmethod： 返回函数的静态方法，该方法不强制要求传递参数。静态方法无需实例化，但也可以实例化后调用

参考地址：
    https://www.cnblogs.com/chenliang0309/p/10091983.html
    https://www.runoob.com/python/python-func-classmethod.html

内置函数：https://www.runoob.com/python/python-built-in-functions.html



@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''

class Dog:
    # 属性默认为类属性（可以给直接被类本身调用）
    name = ""
    age = 0
    
    # 实例id内存地址
    # 实例化方法（必须实例化类之后才能被调用），self：表示实例化类后的地址id
    def showSelfId(self):
        print("id : ", id(self))
        
    # 类id（内存地址）
    # 类方法（不需要实例化类就可以被类本身调用），cls：表示没用被实例化的类本身
    # classmethod： 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def showClsId(cls):
        return id(cls)
    
    @classmethod
    def setName(cls, name):
        print("cls id : ", id(cls))
        cls.name = name
    
    # 返回函数的静态方法，该方法不强制要求传递参数。静态方法无需实例化，但也可以实例化后调用
    @staticmethod
    def howl(words):
        print("words : ", words)
        
    # 错误使用
#     def func3():
#         print("func3")
#         print(Dog.name)  # 属性是可以直接用类本身调用的

# Dog.showSelfId() # 这样调用是会报错：因为 showSelfId()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的

dog1 = Dog()
print("dog1.name : ", dog1.name)
print("dog1.age : ", dog1.age)
dog1.showSelfId()

dog2 = Dog()
print("dog2.name : ", dog2.name)
print("dog2.age : ", dog2.age)
dog2.showSelfId()

print("\n##########################\n")

# 添加实例属性, 只有该实例本身可以使用
dog1.gender = 1
print("dog1.gender: ", dog1.gender)
# 报错
# print("dog2.gender: ", dog2.gender)

print("\n##########################\n")

# 添加类属性, 所有实例对象都可以访问
Dog.color = 'white'
print("dog1.color: ", dog1.color)
print("dog2.color: ", dog2.color)

print("\n##########################\n")

Dog.setName("旺财")
print("Dog.name :", Dog.name)
print("dog1.name:", dog1.name)
print("dog2.name:", dog2.name)

# 调用类方法（不需要实例化类就可以被类本身调用）
print("Dog.showCls():", Dog.showClsId())
print("Dog.showCls():", Dog.showClsId())
# 但也可以实例化后使用
print("dog1.showCls():", dog1.showClsId())
print("dog2.showCls():", dog2.showClsId())

print("\n##########################\n")

# 返回函数的静态方法，该方法不强制要求传递参数。静态方法无需实例化，但也可以实例化后调用
dog1.howl('dog1: 旺旺旺!')
dog2.howl('dog2: 旺旺!')
Dog.howl('Dog : 旺!')
