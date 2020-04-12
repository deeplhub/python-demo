'''
Title: Python成员运算符
Description: 测试实例中包含了一系列的成员，包括字符串，列表或元组。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

a = 10
b = 20

list = [1,2,3,4,5]

if (a in list ):
    print("1 - 变量 a 在给定的列表中")
else:
    print("1 - 变量 a 不在给定的列表中")

if ( b not in list):
    print("2 - 变量 a 不在给定的列表中")
else:
    print("2 - 变量 a 在给定的列表中")
    
a = 2
if (a in list ):
    print("1 - 变量 a 在给定的列表中")
else:
    print("1 - 变量 a 不在给定的列表中")