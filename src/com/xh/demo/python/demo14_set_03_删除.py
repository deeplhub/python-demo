'''
Title:  删除集合
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 无序列表删除==")
set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
print("set1 : ", set1)

# discard & remove 区别:
# - 遇到空值: 
#     discard 不报错
#     remove 报错

# 删除集合中指定的元素
set1.discard("b")
set1.discard("z")

set1.remove('a')
print("set1 remove('a'): ", set1)

try:
    set1.remove('z')
except Exception as ex:
    print("ERROR: ", ex)

# 随机移除元素
set1.pop()
print("set1 pop : ", set1)

# 移除集合中的所有元素
set1.clear()
print("set1 clear : ", set1)

