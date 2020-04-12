'''
Title: 嵌套函数
Description: 

python允许创建嵌套函数。也就是说我们可以在函数里面定义函数，而且现有的作用域和变量生存周期依旧不变。

嵌套函数与闭包的不同之处：
    - 外部函数里面定义一个内部函数，当里内部函数执行需要用到外面函数的变量，把外面变量和里面这个函数合到一块，合到一块的这两个东西就是闭包
    
参考地址：
    https://www.cnblogs.com/xiaxiaoxu/p/9785687.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "嵌套函数 - 函数作为变量")
def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def nestedFun1(func, x, y):
    return func(x,y)


print("nestedFun1(add,2,1):", nestedFun1(add, 2, 1))
print("nestedFun1(sub,2,1):", nestedFun1(sub, 2, 1))
print("\n\n")

print(2, "嵌套函数 - 函数作为变量")


def nestedFun2(func, x, y):
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y
    
    return func(x, y)


print("nestedFun2(add,2,1):", nestedFun2(add, 2, 1))
print("nestedFun2(sub,2,1):", nestedFun2(sub, 2, 1))
print("\n\n")

print(3, "嵌套函数 - 函数作为变量")


def nestedFun3(func):

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    # return内层函数时不加括号，只返回函数的地址
    return func


print("nestedFun3(add):", nestedFun3(add)(2, 1))
print("nestedFun3(sub):", nestedFun3(sub)(2, 1))
