'''
Title: 多态
Description: 

多态：
    -一个对象不同场景下, 有不同的形态
好处:
    - 开闭原则. 对修改关闭, 对扩展开放
    - 增加可扩展性

Python类型判断有两种：type()和isinstance()
两者的区别：
    - 在判断子类上这两个函数不一样。type()不会认为子类是父类的类型，不考虑继承关系；isinstance()会认为子类是父类的类型，考虑继承关系。

isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
sinstance() 与 type() 区别：
    - type()：不会认为子类是一种父类类型，不考虑继承关系。
    - isinstance()： 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。

语法：isinstance(object, classinfo)
参数
    - object：实例对象。
    - classinfo：可以是直接或间接类名、基本类型或者由它们组成的元组。

参考地址：
    https://www.runoob.com/python/python-func-isinstance.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Animal:

    def run(self):
        pass
    
class Dog(Animal):
    def run(self):
        print("Dog.run...")
    
    def eat(self):
        print("Dog.eat...")
        
class Cat(Animal):

    def run(self):
        print("Cat.run...")
    
    def eat(self):
        print("Cat.eat...")

    
print("== 多态 ==")
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(dog, object))
print(isinstance(cat, object))

print("\n##########################\n")


# 多态应用场景
def run(animal):
    # 强类型校验
    if isinstance(animal, Animal):
        animal.run()

        
def eat(animal):
    animal.eat()

run(dog)    
run(cat)    
eat(dog)    
eat(cat)  
