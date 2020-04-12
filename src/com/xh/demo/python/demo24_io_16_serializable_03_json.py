'''
Title: serializable_json
Description: 

方法:
    - 实例方法：使用实例对象访问, 默认使用参数 self, 自动赋值
    - 类方法：使用类对象访问, 默认使用参数 cls, 自动赋值
    - 静态方法：实例对象 & 类对象都可以访问. 可以有参, 也可以无参

Python中self和cls的区别：
    - self：表示一个具体的实例本身。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。
    - cls：表示这个类本身。类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self,即self是__new__的返回值

classmethod： 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。类方法（不需要实例化类就可以被类本身调用），但也可以实例 化后使用


dumps是将dict转化成str格式；
loads是将str转化成dict格式。
dump和load也是类似的功能，只是与文件操作结合起来了。

要想JSON化类的实例，应在dumps中指定可选参数default


getattr()：函数用于返回一个对象属性值。
isinstance()：函数来判断一个对象是否是一个已知的类型，类似 type()。
dir()：函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
__dict__：类的属性（包含一个字典，由类的数据属性组成）
    
参考地址：
    https://www.runoob.com/python/python-json.html
    https://www.runoob.com/python/python-object.html
    https://www.cnblogs.com/fengff/p/11008353.html
    https://www.cnblogs.com/geeklove01/p/8034456.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
from _datetime import datetime, date
import json


class Student:

    def __init__(self):
        pass
    
    def init(self, name, age, birth):
        self.name = name
        self.age = age
        self.birth = birth
    
    # 类方法（不需要实例化类就可以被类本身调用），cls：表示没用被实例化的类本身
    # classmethod： 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def columns(cls):
        print(str(cls))
        return set('name age birth'.split())


def toDict(obj):
    dict1 = {}
    # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
    # 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    for attr in dir(obj):
        # ignore __init__ & __class__ etc...
        if (attr not in obj.columns()):
            continue
        
        # print(attr, ":", getattr(obj, attr), ":", type(getattr(obj, attr)))
        # getattr()：函数用于返回一个对象属性值。
        value = getattr(obj, attr)
        # isinstance()：函数来判断一个对象是否是一个已知的类型，类似 type()。
        if isinstance(value, datetime):
            value = str(value)
        if isinstance(value, date):
            value = str(value)
        dict1[attr] = value
    return dict1
    
    
stu = Student()
stu.init('张三', 30, datetime.now())

# serialize
# default=<函数> 自定义JSON反序列化的类的实例
ret1 = json.dumps(stu, default=toDict)
print('ret1      :', ret1)
print('type(ret1):', type(ret1))
print()
   
# deserialize
ret2 = json.loads(ret1)
print('ret2      :', ret2)
print('type(ret2):', type(ret2))
print()
 
# 将字典转化为对象
stu = Student()
# __dict__：类的属性（包含一个字典，由类的数据属性组成）
stu.__dict__ = ret2;
# 打印重建的对象
print("stu       :", type(stu))
print("stu.age   :", stu.age)
print("stu.birth :", stu.birth)
print("stu.birth :", type(stu.birth))
