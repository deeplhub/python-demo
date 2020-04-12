'''
Title: function 变量作用域
Description: 
    改变局部变量的值不会影响到全局变量的值

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 变量作用域 ==")
# 全局变量
num = 100


def add(num1, num2):
    # 局部变量
    num = num1 + num2
    print("num3 : ", num)

    
add(10, 20)
print("num : ", num)
