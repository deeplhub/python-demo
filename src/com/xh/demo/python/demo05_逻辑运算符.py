'''
Title: Python逻辑运算符
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

a = 10
b = 20

if (a and b ):
    print(" 1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 都为 false")

if (a or b ):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为true")
else:
    print("2 - 变量 a 和 b 都为 false")

a= 0
if not( a and b ):
    print("3 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("3 - 变量 a 和 b 都为true")