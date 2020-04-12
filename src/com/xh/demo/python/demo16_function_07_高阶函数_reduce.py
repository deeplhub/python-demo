'''
Title: funtion 高阶函数 reduce
Description: 

    参考地址：https://www.cnblogs.com/yinzhengjie/p/10976621.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
import functools

print("匿名函数操作方式：")
arr_list = [1, 2, 3]
newfun = functools.reduce(lambda x, y:x + y, arr_list)
print(newfun)

newfun = functools.reduce(lambda x, y:x + y, arr_list, 10)
print(newfun)

print("\n#####################\n")

print("非匿名函数操作方式：")
def fun(x, y):
    return x + y 

newfun = functools.reduce(fun, arr_list)
print(newfun)
newfun = functools.reduce(fun, arr_list, 10)
print(newfun)
