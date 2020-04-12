'''
Title: 创建集合
Description: 
    a. 集合（set）是一个无序的不重复元素序列。
    b. 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
from builtins import set
print("== 无序列表创建 ==")
set1 = set()
set1.add(12)
print("1. set1 : ", set1)

print("\n##################\n")

# 自动去重
set1 = {'a', 1, 'abc', 'kd', 'a', 1}
print("2. set1 : ", set1)

print("\n##################\n")

sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
set1 = set(sdict)
print("3. set1 : ", set1)

print("\n##################\n")

sdict = {'a': 1, 'b': 2, 'b': ['boy', 'girl', 'children'], 'c': 3 }
set1 = set(sdict)
print("4. set1: ", set1)
