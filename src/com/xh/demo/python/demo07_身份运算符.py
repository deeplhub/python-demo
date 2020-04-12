'''
Title: Python身份运算符
Description: 
身份运算符用于比较两个对象的存储单元

在 Python 中一切都是对象，毫无例外整数也是对象，对象之间比较是否相等可以用==，也可以用is。
==和is操作的区别是：
    a. Is:比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。
    b. ==:比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print ("2 - a 和 b 有相同的标识")
else:
    print ("2 - a 和 b 没有相同的标识")

b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
