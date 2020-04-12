'''
Title: 查询字段
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("查询字段")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
val = sdict["Name"]
print("1, sdict['Name'] :", val)

val = sdict.get("Name")
print("2, sdict.get('Name') :", val)

# 找不到key时，使用默认值
val = sdict.get("sex", "男")
print("3, sdict.get('sex', '男') ：", val)

print("\n##################\n")

keys = sdict.keys()
for key in keys:
    print("4, key : ", key)

print("\n##################\n")

vals = sdict.values()
for val in vals:
    print("5, val : ", val)

print("\n##################\n")

items = sdict.items()
for i, j in items:
    print(i, ":", j)
