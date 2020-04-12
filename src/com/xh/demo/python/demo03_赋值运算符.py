'''
Title: Python赋值运算符
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

a = 21
b = 10
c = 0

c = a+b
print("1 - c 的值为：",c)

c+=a
print("2 -（加法赋值运算符） c 的值为：", c)

c-=a
print("2 -（减法赋值运算符） c 的值为：", c)

c*=a
print("3 -（乘法赋值运算符） c 的值为：", c)

c/=a
print("4 -（除法赋值运算符） c 的值为：",c)

c = 2
c %= a 
print("5 -（取模赋值运算符） c 的值为：", c)

c **= a 
print("6 - （幂赋值运算符） c 的值为：",c )

c //= a 
print("7 - （取整除赋值运算符） c 的值为：", c )
