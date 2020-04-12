'''
Title: 函数 def- function 可变不可变类型
Description: 

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。

函数(def)是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数(def)能提高应用的模块性，和代码的重复利用率。
你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

    可变不可变类型
    - 不可变类型
        float, int, None, bool, tuple, str, function
    - 可变类型
        list, dict, set

内置函数列表：
    https://www.runoob.com/python/python-built-in-functions.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== function 可变不可变类型 ==")
print("不可变类型")
def add(num):
    num = num + 10
    print("num : ", num)
    
num = 10
add(num)
print("num2 : ", num)

print("\n##########################\n")

print("可变类型")

def append(num):
    num.append(20)
    print("num3 : ", num)

num = [10]
append(num)
print("num4 : ", num)
