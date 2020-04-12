'''
Title: set、list、tuple相互转换
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== set list tuple 相互转换 ==")
list1 = [i for i in range(10)] + [i for i in range(10)]
print("list1 :", list1)

set1 = set(list1)
print("1. list to set :", set1)

tup1 = tuple(list1)
print("2. list to tuple ： ", tup1)

list1 = list(set1)
print("3. set to list : ", list1)

tup1 = tuple(set1)
print("4. set to tuple : ", tup1)

list1 = list(tup1)
print("5. tuple to list : ", tup1)

set1 = set(tup1)
print("6. tuple to set : ", set1)
