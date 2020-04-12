'''
Title: function 必选参数
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== 参数-必选参数 ==")

def add(num1, num2):
    num3 = num1 + num2
    print("num3 : ", num3)

add(10, 20)
# 报错
add(10)
