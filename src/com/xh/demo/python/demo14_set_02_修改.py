'''
Title: 修改集合
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 无序列表修改 ==")
set1 = {'a', 'b', 'c'}
print("set1 : ", set1)

print("\n##################\n")

# 为集合添加元素
set1.add(1)
print("set1 add : ", set1)

print("\n##################\n")

# 给集合添加元素
set2 = {'computer', 'calulator'}
set1.update(set2)
print("set1 update: ", set1)
