'''
Title: 多装饰器
Description: 

多个装饰器: 先装饰下面的, 再装饰上面的

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
import time


def make_bold(fn):
    print("1...")
    time.sleep(1)
    def inner():
        print("2...")
        tmp = "<b>" + fn() + "</b>"
        return tmp

    return inner


def make_italic(fn):
    print("3...")

    def inner():
        print("4...")
        tmp = "<i>" + fn() + "</i>"
        return tmp

    return inner


def func1():
    return "hello1"


@make_italic
@make_bold
def func2():
    return "hello2"


# @make_italic
# @make_bold
def func3():
    return "hello3"


print("开始执行方法：")
print("当前结果：", func2())
