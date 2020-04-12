'''
Title: function 可变参数
Description: 要点：
函数形参：*args 和 **kwargs 主要用于函数定义。你可以将不定数量的参数传递给一个函数。
不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。
其实并不是必须写成 *args 和 **kwargs。  *args 和 **kwargs 只是一个通俗的命名约定，你也可以写成 *ar 和 **k ，*(星号) 才是必须的.。
    
python函数传递参数的方式有两种：位置参数、关键词参数。
    
*args 与 **kwargs 的区别，两者都是 python 中的可变参数：
    - *args:表示任何多个无名参数，它本质是一个 tuple
    - **kwargs:表示关键字参数，它本质上是一个 dict
    
如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前

函数实参
    - 果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用

参考地址：
    https://blog.csdn.net/yilovexing/article/details/80577510
    https://www.cnblogs.com/beiluowuzheng/p/8461518.html


@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print(1, " == 可变参数")


# 元组（tuple）
# 会把接收到的参数形成一个元组
def add(*args):  # 函数形参
    print(str(type(args)))
    print(args)
    print("sum : ", sum(args))


add(10, 20)
add(10, 20, 30)

# 如果我们希望将一个数组形成元组，需要在传入参数的前面 加上一个 *（星）
arr_list = [100, 200, 300]
add(*arr_list)

print("\n\n")
print(2, "可变参数")


# 字典（dict）
# 则会把接收到的参数存入一个字典
def add2(**kwarg):
    print(str(type(kwarg)))
    print(kwarg)


add2(num1=1, num2=2)

# 如果需要传入一个字典参数，需要在传入参数前面加上两个 **（星）
num = {"num1": 1, "num2": 2}
add2(**num)

print("\n\n")
print(3, "可变参数")


# 如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前
def add3(*args, **kwarg):
    print("args type : ", str(type(args)))
    print("kwarg type:", str(type(kwarg)))
    print("args :", args)
    print("kwarg:", kwarg)


add3(*arr_list, **num)

print("\n\n")
print(4, "可变参数")


# 函数实参：如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用
def add4(num1, num2, num3):
    print("num1 : ", num1)
    print("num2 : ", num2)
    print("num3 : ", num3)


# 元组
args = ("one", 2, 3)
add4(*args)

# 字典
kwargs = {"num1": "one", "num2": 2, "num3": 3}
add4(**kwargs)
