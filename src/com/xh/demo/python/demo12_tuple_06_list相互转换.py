'''
Title: 元组与list相互转换
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''

print("== tuple & list 相互转换 ==")
print("list 转 tuple")
list1 = [1, 345, 456, "abx", "xyz"]
tup = tuple(list1)
print("tup:", type(tup))
print("value:", tup)

print("\n##################\n")

print("tuple 转 list")
list1 = list(tup)
print("list:", type(list1))
print("value:", list1)

print("\n##################\n")

list1 = list("深刻的回家")
print("list:", type(list1))
print("value:", list1)

print("\n##################\n")

tup = tuple(list1)
print("tup:", type(tup))
print("value:", tup)
