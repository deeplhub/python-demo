'''
Title: 无序列表判断
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 无序列表判断 ==")
set1 = {'a', 'b', 'c'}
set2 = {'a', 'b' }
set3 = {'z', 'v' }

#     判断指定集合是否为该方法参数集合的子集。
print("set2.issubset(set1)  :", set2.issubset(set1))
# 判断该方法的参数集合是否为指定集合的子集
print("set1.issuperset(set2):", set1.issuperset(set2))

# 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print("set1.isdisjoint(set2):", set1.isdisjoint(set2))
print("set1.isdisjoint(set3):", set1.isdisjoint(set3))

print("a in set1:", 'a' in set1)
print("x in set1:", 'x' in set1)
