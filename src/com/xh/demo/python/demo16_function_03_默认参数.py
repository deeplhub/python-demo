'''
Title: function 默认参数
Description: 
    必选参数: 默认已经赋值, 如果没有传值, 就使用 默认值; 如果赋值了, 就使用赋值的

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 参数-默认参数 ==")


def add(num1, num2=1):
    num3 = num1 + num2
    print("num3 : ", num3)


add(10, 20)
add(10)
