'''
Title: 其他功能copy等
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 字典其他功能==")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict2 = sdict.copy()
print("sdict: ", sdict)
print("dict2: ", dict2)

# 在 Python 中一切都是对象，毫无例外整数也是对象，对象之间比较是否相等可以用==，也可以用is。
# ==和is操作的区别是：
# a. Is:比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。
# b. ==:比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。
print("dict2 is sdict: ", dict2 is sdict)
print("dict2 == sdict: ", dict2 == sdict)

print("\n##################\n")

# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
val = "abca"
dict2 = sdict.fromkeys(val)
print("dict.fromkeys-1, dict2: ", dict2)

print("\n##################\n")

arr_list = [1, 2, 3]
dict2 = sdict.fromkeys(arr_list, 0)
print("dict.fromkeys-2, dict2: ", dict2)

print("\n##################\n")

# 把字典dict2的键/值对更新到dict里
dict3 = {8:'xbox', 9:'xiaobawang'}
dict2.update(dict3)
print("update: ", dict2)
