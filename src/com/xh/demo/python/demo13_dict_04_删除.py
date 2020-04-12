'''
Title: 删除字典元素
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("删除字典元素")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("sdict:", sdict)

del sdict["Name"]
print("del sdict['Name']:", sdict)

sdict.pop("Age")
print("pop sdict['Age']:", sdict)

sdict.clear()
print("清空字典：", sdict)

