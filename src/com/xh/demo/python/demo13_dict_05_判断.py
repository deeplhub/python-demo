'''
Title: 字典判断
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''

print("字典判断")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("sdict: ", sdict)

print("\n##################\n")

print("判断键")
print("Age" in sdict)
print("Age" not in sdict)

print("\n##################\n")

print("判断值")
print("7" in sdict.values())
print("7" not in sdict.values())

sdict = {'Name': 'Zara'}
print(len(sdict))
if sdict is not None and len(sdict) > 0:
    print("AAAAAAAA")

sdict = {}
print(len(sdict))

sdict = None
if sdict is not None and len(sdict) > 0:
    print("BBBBB")
