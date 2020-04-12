'''
Title: Python比较运算符
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
a = 21
b = 10
c = 0

if ( a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if ( a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")


if(a<b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")


if(a>b):
    print("3 - a 大于 b")
else:
    print("3 - a 小于等于 b")


a = 5
b = 20
if(a<=b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于 b")


if(a>=b):
    print("6 - a 大于等于 b")
else:
    print("6 - a 小于 b")