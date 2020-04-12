'''
Title: 
Description: 

isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    - isinstance() 与 type() 区别：
    - type() 不会认为子类是一种父类类型，不考虑继承关系。
    - isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。

参考地址：
    https://www.runoob.com/python/python-func-isinstance.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/11
'''
from builtins import type

list2 = [1, 2, 3, 4, 5, 6, 7 ]

tup2 = (1, 2, 3, 4, 5)

sdict = {'a': 1, 'b': 2, 'b': ['boy', 'girl', 'children'], 'c': 3 }

set1 = {'a', 1, 'abc', 'kd', 'a', 1}

str1 = "123567590dhgj散热污染123"

print(type(list2))
print(isinstance(list2, list))

print("############")

print(type(tup2))
print(isinstance(tup2, tuple))

print("############")

print(type(sdict))
print(isinstance(sdict, dict))

print("############")

print(type(set1))
print(isinstance(set1, set))

print("############")

print(type(str1))
print(isinstance(str1, str))
