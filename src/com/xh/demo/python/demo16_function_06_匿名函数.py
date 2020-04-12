'''
Title: function 匿名韩函数
Description: 
    python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

    语法：lambda [参数 [,参数2,.....参数n]]:表达式
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 匿名函数 ==")
f1 = lambda x:x + 1
f2 = lambda x:x * x 

print(f1(1))
print(f2(2))
print(f2(4))

print("\n#########################\n")

arr_list = [2, 3, 4, 5, 6]
# map 根据提供的函数对指定序列做映射
val = list(map(lambda x:x * x, arr_list))
print(val)

print("\n#########################\n")

arr_list2 = [3, 5, 7]
val = list(map(lambda x, y:x * y, arr_list, arr_list2))
print(val)

print("\n#########################\n")


# 附：
# 关于 map 的操作说明
# 语法：map(function, iterable, ...)
# 参考地址：https://www.runoob.com/python/python-func-map.html
def fun(num):
    return num * 2

arr_list = [1, 2, 3, 4]
map_val = map(fun, arr_list)
print(map_val)
print(type(map_val))
print(list(map_val))

val = list(map(lambda x:x * 2, arr_list))
print(val)

# 匿名函数
val = list(map(lambda x, y, z:x + y + z, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
print(val)
# 等价于

# 非匿名函数
def fun2(x, y, z):
    return x + y + z
map_val = map(fun2, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
print(list(map_val))
