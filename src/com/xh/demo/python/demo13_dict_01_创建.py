'''
Title: 创建字典
Description: 
    a. 字典是另一种可变容器模型，且可存储任意类型对象。
    b. 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
sdict = {'a': 1, 'b': 2, 'b': ['boy', 'girl', 'children'], 'c': 3 }
print("sdict: ", sdict)

print("\n##################\n")

# 键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
sdict = {'a': 1, 'b': 2, 'b': '3'}
print("访问字典里的值")
print("sdict['b']:", sdict['b'])

print("\n##################\n")

print("修改字典")
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
try:
    print("sdict['Age']:",sdict['Age'])
    # 如果用字典里没有的键访问数据，会输出错误
    print("sdict['School']: ", sdict['School'])
except Exception as ex:
    print("ERROR:", ex)

sdict["Age"] = 20
print("sdict['Age']:", sdict['Age'])
sdict['School'] = "School"
print("sdict:", sdict)

print("\n##################\n")

print("修改字典")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("sdict:", sdict)
del sdict["Name"]
print("删除sdict['Name']:", sdict)
sdict.clear()
print("清空所有字典：", sdict)

