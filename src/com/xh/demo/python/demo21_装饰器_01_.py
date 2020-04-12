'''
Title: 装饰器
Description: 

装饰器
    - 在不修改源代码的情况下, 增加一些功能, 比如权限的验证 & 日志等等

简单地说：他们是修改其他函数的功能的函数。

使用装饰器方法：
    - 闭包的形式
    - 使用 @<mether> 方式

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "装饰器")


def login(func):
    print("1...")

    def inner():
        print("2...")
        func()

    return inner


def add():
    print("add ...")


def delete():
    print("delete ...")


def update():
    print("update ...")


@login  # 当程序加载时执行 login 函数，如果使用闭包的方式需要去掉
def select():
    print("select ...")


print("闭包实现")
# 闭包实现
ret = login(add)
ret()
# 等同于
# login(add)()

print("装饰器实现")
select()

print("无装饰器")
# 无装饰器
update()
print("\n\n")

print(2, "装饰器 - 日志")


def logig(fun):
    def show(*args, **kwargs):
        temp = fun(*args, **kwargs)

        print("Current method", fun.__name__ + "()", ":", temp)
        return fun(*args, **kwargs)

    return show


@logig
def add2(x, y):
    return x + y


res = add2(1, 2)
print("res=", res)
