'''
Title: 字符串分割
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== str 分割 ==")
str1 = "a-b-c";
split = str1.split("-")
print("1. split : ", split)
print("2. type(split) : ", type(split))

split = str1.split("-", 1)
print("3. split - 1:", split)

split = str1.split(";")
print("4. split ; :", split)

str1 = "a b c    d";
split = str1.split()
print("5. split:", split)

str1 = "a\nb\tc\n\rp\r    d";
split = str1.split()
print("6. split:", split)

str1 = "a-b-c";
partition = str1.partition("-")
print("7. partition:", partition)
