'''
Title: 字符串转换列表
Description: 

python去掉字符串中空格的方法
    - strip()：把头和尾的空格去掉
    - lstrip()：把左边的空格去掉
    - rstrip()：把右边的空格去掉
    - replace('c1','c2')：把字符串里的c1替换成c2。故可以用replace(' ','')来去掉字符串里的所有空格
    - split()：通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''

str1 = "11, 22, 33, 44, 55"
ls = str1.split(",")
for index in ls:
    print(index.strip())

print("#####################")
str1 = "11"
ls = str1.split(",")
for index in ls:
    print(index.strip())

print("#####################")
str1 = None
ls = str1.split(",")
for index in ls:
    print(index.strip())
