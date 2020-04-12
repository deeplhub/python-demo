'''
Title: 
Description: 

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "内建")
ls = ["Java", "PHP", "Python", "HTML", "JavaScript"]
en = enumerate(ls)
print(next(en))

print()
ls = ["Java", "PHP", "Python", "HTML", "JavaScript"]
en = enumerate(ls)
for i in en:
    print(i)
print()

en = enumerate(ls,2)
for i in en:
    print(i)
