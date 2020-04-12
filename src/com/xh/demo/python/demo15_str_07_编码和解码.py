'''
Title: 字符串编码和解码
Description: 
    编码 encode
            字符 --> 字节
    解码 decode
        字节 --> 字符

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== str 编码 & 解码 ==")
str1 = "我是钢铁侠";

ret1 = str1.encode("UTF-8")
print("ret1 UTF-8: ", type(ret1))
print("ret1 UTF-8: ", ret1)

ret2 = str1.encode("GBK")
print("ret2 GBK: ", type(ret2))
print("ret2 GBK: ", ret2)

str2 = ret1.decode("UTF-8")
print("str2 : ", str2)

str3 = ret2.decode("GBK")
print("str3 : ", str3)

