'''
Title: 列表判断
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
ls = [1, 2, 3, 4, 5, 6, 7]

print(str(ls))

# 避免下标越界
print("== 遍历判断 ==")
print("5 in list ：", 5 in ls)
print("5 not is list：", 5 not in ls)

ls = [1, 7]
print(len(ls))

ls = []
print(len(ls))
