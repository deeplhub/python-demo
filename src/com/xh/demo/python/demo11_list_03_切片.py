'''
Title: 列表切片
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
list1 = ['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4]
print("== 列表切片 ==")
print("list1  :", list1)

list2 = list1[0:3] 
print("list2-1:", list2)

list2 = list1[0:2] 
print("list2-2:", list2)

list2 = list1[1:3] 
print("list2-3:", list2)

list2 = list1[:3]  # 和 list1[0:3]一样
print("list2-4:", list2)

list2 = list1[:]  # 全部复制，值一样但是地址(引用)不一样
print("list2-5:", list2)

list2 = list1[::1]  # 全部复制，值一样但是地址(引用)不一样
print("list2-6:", list2)
print("值一样                      : list1 == list2,", list1 == list2)
print("地址(引用)不一样: list1 is list2,", list1 is list2)

list2 = list1[::2]  # 间隔，取 2，4，6，8
print("list2-7:", list2)

list2 = list1[::-1]  # 倒序
print("list2-8:", list2)
