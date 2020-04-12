'''
Title: 遍历列表
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
ls = [1, 2, 3, 4, 5, 6, 7]

print("== 遍历列表-1 ==")
count = 0
length = len(ls)
while count < length:
    print(ls[count])
    count = count + 1

print("\n###################\n")

print("== 遍历列表-2 ==")
for index in ls:
    print(index)
