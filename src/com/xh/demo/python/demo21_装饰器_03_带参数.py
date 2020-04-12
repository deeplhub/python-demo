'''
Title: 装饰器带参数
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "装饰器")


def outer(fun):
    print("1...", type(fun))

    def inner(*args, **kwargs):
        print("2...")
        return fun(*args, **kwargs)

    return inner


@outer
def fun1():
    print("fun1...")


@outer
def fun2():
    return "fun2"


@outer
def fun3(x, y):
    #     return "fun3..."
    return x + y


# 没有返回值
print("没有返回值")
fun1()

# 有返回值
print("有返回值")
print(fun2())

# 有参数
print("有参数")
print(fun3(2, 3))
