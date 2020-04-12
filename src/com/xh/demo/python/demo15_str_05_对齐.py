'''
Title: 字符串对齐
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== str 对齐 ==")
str1 = "I am ironman";

# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
str2 = str1.ljust(30)
print("1. ljust : ")
print(str2)

str2 = str1.ljust(30, "*")
print("2. ljust : ")
print(str2)

str2 = str1.ljust(3)
print("3. ljust : ")
print(str2)

# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
str2 = str1.rjust(30)
print("4. rjust : ")
print(str2)

str2 = str1.rjust(30, "*")
print("5. rjust : ")
print(str2)

# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
str2 = str1.center(30)
print("6. center : ")
print(str2)

str2 = str1.center(30, "*")
print("7. center : ")
print(str2)
