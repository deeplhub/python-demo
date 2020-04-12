'''
Title: Python算术运算符
Description: https://www.runoob.com/python3/python3-basic-operators.html#ysf1

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 -（取模 - 返回除法的余数） c 的值为：", c)


# 修改变量
a = 2
b = 3
c = a ** b
print("6 -（幂 - 返回x的y次幂） c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 -（取整除 - 向下取接近除数的整数） c 的值为：", c)