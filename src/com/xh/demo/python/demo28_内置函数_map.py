'''
Title: Python 内置函数 map
Description: 

map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map() 函数语法：map(function, iterable, ...)

参考地址：
    https://www.runoob.com/python/python-built-in-functions.html
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''


def fun(num):
    return num * 2


ls = [1, 2, 3, 4]
mv = map(fun, ls)
print(mv)
print(type(mv))
print(list(mv))

print("\n##########################\n")

vals = map(lambda x:x + 1, ls)
for index in vals:
    print(index)

print("\n##########################\n")

vals = list(map(lambda x:x * 2, ls))
print(vals)

print("\n##########################\n")

# 匿名函数
vals = list(map(lambda x, y, z:x + y + z, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
print(vals)
# 等价于
# 非匿名函数
def fun2(x, y, z):
    return x + y + z


mv = map(fun2, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
print(list(mv))

