'''
Title: 元组修改
Description: 
    元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("修改元组")
tup1 = (12, 34.23)
print("tup1:", tup1)

# 以下修改元组元素操作是非法的。

try:
    tup1[0]= 10
    print("tup1:",tup1, "Not print at all")
except Exception as e:
    print("ERROR:", e)

tup2 = ("abc", "xyz")
print("tup2:", tup2)

# 创建一个新的元组
tup3 = tup1 + tup2
print("tup3", tup3)
