'''
Title: 内建
Description: 

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

info = "1+2"
print(info)
print(eval(info))

stu = "{'name':'abc','age':12,'sex':'男'}"
ret = eval(stu)
print(type(ret))
print(ret.get("name"))
