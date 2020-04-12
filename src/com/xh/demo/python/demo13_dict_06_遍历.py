'''
Title: 字典遍历
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 字典遍历==")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# sdict = {}
for k in sdict:
    print(k, ":", sdict.get(k))

print("\n##################\n")

for k, v in sdict.items():
    print(k, ":", v)
else:
    print("遍历为空")
