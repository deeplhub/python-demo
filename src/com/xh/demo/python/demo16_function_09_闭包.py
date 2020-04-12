'''
Title: 闭包
Description: 
什么叫闭包：
    - 定义：在外部函数里面定义一个内部函数，并且这个内部函数用到了外部函数的变量，那么将这个内部函数和用到的一些变量统称为闭包。
    - 定义：如果一个函数定义在另一个函数的作用域内，并且引用了外层函数的变量，则该函数称为闭包。

闭包是Python所支持的一种特性，它让在非global scope定义的函数可以引用其外围空间中的变量，这些外围空间中被引用的变量叫做这个函数的环境变量。
环境变量和这个非全局函数一起构成了闭包。

闭包特点：一个函数返回的函数对象，这个函数对象执行的话依赖非函数内部的变量值，这个时候，函数返回的实际内容如下：
    - 函数对象
    - 函数对象需要使用的外部变量和变量值


闭包必须嵌套在一个函数里，必须返回一个调用外部变量的函数对象，才是闭包

通俗理解就是：里面函数执行  ，需要用到外面函数的一个变量 ，所以，就把外面变量和里面这个函数合到一块，合到一块的这两个东西就是闭包

外部函数里面定义一个内部函数，当里内部函数执行需要用到外面函数的变量，把外面变量和里面这个函数合到一块，合到一块的这两个东西就是闭包



闭包语法
    - 在函数内部定义了一个新的函数, 并且内部函数引用了外部函数的局部变量, 外部函数将内部函数返回
    
闭包和函数的区别：
    - 闭包：在闭包中，既有函数，又有数据，而且数据是闭包里面独有的数据，与外界无影响；
    - 函数：函数中，需要使用的全局变量，在一定程度上是受到限制的，因为全局变量不仅仅是一个函数使用，其他的函数也可能会使用到，一旦修改会影响到其他函数使用全局变量，所以全局变量不能随便修改从而在函数的使用中受到一定局限性。

闭包的格式：
    - 下面用伪代码进行闭包格式的描述：
    def 外层函数(参数):
        def 内层函数():
            print("内层函数执行", 参数)
    
    return 内层函数
    内层函数的引用 = 外层函数("传入参数")
    内层函数的引用()

闭包的用途：Python中，闭包的主要用途就是用于装饰器的实现

参考地址：
    https://blog.csdn.net/gymaisyl/article/details/83019368
    https://www.cnblogs.com/xiaxiaoxu/p/9785687.html


@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "闭包")


def fun1(num1):
    def inner(num2):
        return num1 + num2

    return inner


ret = fun1(10)
print(ret(10))

print("\n\n")
print(2, "闭包")


def func2(a, b):
    def line(x):
        return a * x - b

    return line


line = func2(2, 3)
print(line(5))
print("\n\n")

print(3, "闭包 - 修改外部函数中的变量")


def func3(a, b):
    def line(x):
        nonlocal a
        a = 3
        return a * x - b

    return line


line = func3(2, 3)
print(line(5))
print("\n\n")

print(4, "闭包")


def func4():
    loc_list = []

    def inner_func(name):
        loc_list.append(len(loc_list) + 1)
        print('%s loc_list = %s' % (name, loc_list))

    return inner_func


fun = func4()
fun('A')
fun('B')
fun('C')
print("\n\n")

print(5, "闭包")


def func5(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):  # 包装函数
        # 字典 copy() 函数返回一个字典的浅复制。
        # dict2 = dict1          # 浅拷贝: 引用对象
        # dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
        newkeywords = keywords.copy()
        # update函数把字典fkeywords的键/值对更新到newkeywords里
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)

    newfunc.func = func  # 保留原函数
    newfunc.args = args  # 保留原函数的位置参数
    newfunc.keywords = keywords  # 保留原函数的关键字参数参数
    return newfunc


def add(x, y):
    return x + y


foo = func5(add, 4)
print(foo(5))
