'''
Title: funtion 高阶函数 partial
Description: 
    functools的常见函数：其中最常见的自然是functools.partial
        functools.partial
        functool.update_wrapper
        functool.wraps
        functools.reduce
        functools.cmp_to_key
        functools.total_ordering

    参考地址：https://www.jianshu.com/p/710a3ad32a1a
        https://www.cnblogs.com/yinzhengjie/p/10976621.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
import functools

# 二进制
print(int('110', 2))
print(int('111', 2))
print(int('101010', 2))
print(int('101011', 2))

print(int('10001000', 2))
print(int('10001000', 10))

print("\n#######################\n")

int2 = functools.partial(int, base=2)
print(int2('110'))
print(int2('111'))
print(int2('101010'))
print(int2('101011'))
print(int2('10001000'))

print("\n#######################\n")


def fun1(num1, num2):
    return num1 + num2

newfun = fun1(50, 50)
print(newfun)
newfun = functools.partial(fun1, num2=50)
print(newfun(2))
print(newfun(2, num2=5))
print(newfun(num1=5, num2=4))

print("\n#######################\n")


# partial函数本质
# *args:表示任何多个无名参数，它本质是一个 tuple
# **kwargs:表示关键字参数，它本质上是一个 dict
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords): # 包装函数
        newkeywords = keywords.copy()
        # update函数把字典fkeywords的键/值对更新到newkeywords里
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    
    newfunc.func = func # 保留原函数
    newfunc.args = args # 保留原函数的位置参数
    newfunc.keywords = keywords # 保留原函数的关键字参数参数
    return newfunc


def add(x,y):
    return x + y

foo = partial(add,4)
print(foo(5))
