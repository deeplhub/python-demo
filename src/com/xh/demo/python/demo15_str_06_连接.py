'''
Title: 字符串连接
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== str 连接 ==")
str1 = "I am ironman";

split = str1.split()
print("1. split : ", split)

str2 = "".join(split)
print("2. join : ", str2)

str2 = "/".join(split)
print("3. join : ", str2)

str2 = "   ".join(split)
print("4. join : ", str2)
