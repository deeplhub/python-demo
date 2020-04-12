'''
Title: 命名空间 - 全局变量
Description: 

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

global 和 nonlocal关键字：当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

参考地址：
    https://www.runoob.com/python3/python3-namespace-scope.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''

print(1, "全局变量和局部变量")
total = 0  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

 
# 调用sum函数
sum(10, 20)
print ("函数外是全局变量 : ", total)

print()

print(2, "修改全局变量")

num = 1

def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)


fun1()
print(num)
print()

print(3, "修改嵌套作用域变量")


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
print()

# 错误的定义，错误原因：错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。
# 修改 a 为全局变量，通过函数参数传递，可以正常执行输出结果为：
# a = 10
# def test():
#     a = a + 1
#     print(a)
# test()

# 正常
a = 10

def test(a):
    a = a + 1
    print(a)


test(a)
