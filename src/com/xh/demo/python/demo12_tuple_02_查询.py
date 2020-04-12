'''
Title: 元组查询
Description: 
    元组可以使用下标索引来访问元组中的值

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
# 列表有的查询功能，元组都有,只是不能修改
print("访问元组")

tup1 = ('physics', 'chemistry', 1997, 2000)

print("tup1[0]  : ", tup1[0])
print("tup1[1:3]: ", tup1[1:3])
print("tup1.index('physics'): ", tup1.index('physics'))
print("tup1.index(1997)     : ", tup1.index(1997))
# 报错
print("tup1.index('123'): ", tup1.index('123'))
