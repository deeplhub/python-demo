'''
Title: 列表删除
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
ls = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-1 ==")
print("list：", ls)

del(ls[3])
print("del index 3：", ls)

print("\n#######################\n")

ls = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-2 ==")
print("ls：", ls)
ls.pop(3)  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print("pop index 3：", ls)

print("\n#######################\n")

ls = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-3 ==")
print("ls：", ls)
ls.pop()
print("pop :", ls)

print("\n#######################\n")

ls = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-3 ==")
print("ls：", ls)
ls.remove("chemistry")  # 移除列表中某个值的第一个匹配项
print("remove value 'chemistry' :", ls)

