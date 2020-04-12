'''
Title: 无序列表交集并集差集
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 无序列表交集并集差集==")
set1 = {'a', 'b', 'c'}
set2 = {'c', 'e', 'f'}

#     返回两个集合的并集
set3 = set1.union(set1)
print("1. set3 union : ", set3)

set3 = set1 | set2
print("2. set1 | set2 : ", set3)

# 返回集合的交集
set3 = set1.intersection(set2)
print("3. set3 intersection: ", set3)

set3 = set1 & set2
print("4. set1 & set2 : ", set3)

# 返回多个集合的差集
set3 = set1.difference(set2)
print("5. set3 difference : ", set3)

set3 = set1 - set2
print("6. set1 - set2 : ", set3)
