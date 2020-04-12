'''
Title: 查询列表
Description: https://www.runoob.com/python3/python3-list.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("list1[0]  : ", list1[0])
print("list2[1:5]: ", list2[1:5])

print("== 根据列表中的值找下标 ==")
print("index : ", list1.index(1997))
print("count1: ", list1.count(1997))  # 存在
print("count2: ", list1.count(5))  # 不存在
try:
    print("not in: ", list1.index(5))
except Exception as es:
    print(es)
